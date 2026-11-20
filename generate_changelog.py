"""
Generate help/changelog.rst from GitHub.

The cosmosis section is built from the GitHub release notes of
cosmosis-developers/cosmosis, one section per release.

The cosmosis-standard-library section is built from the merged pull requests
of cosmosis-developers/cosmosis-standard-library, grouped by month.

This needs network access, so it is not run as part of the normal build.
Re-run it by hand to refresh the page:

    python generate_changelog.py

Set GITHUB_TOKEN to avoid the unauthenticated API rate limit.
"""
import datetime
import json
import os
import re
import urllib.request
from collections import OrderedDict

API = "https://api.github.com/repos/cosmosis-developers"
GITHUB = "https://github.com"
OUTPUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "help", "changelog.rst")


def fetch_all(url):
    headers = {"Accept": "application/vnd.github+json"}
    token = os.environ.get("GITHUB_TOKEN")
    if token:
        headers["Authorization"] = f"Bearer {token}"
    results = []
    page = 1
    while True:
        sep = "&" if "?" in url else "?"
        req = urllib.request.Request(f"{url}{sep}per_page=100&page={page}", headers=headers)
        with urllib.request.urlopen(req) as f:
            data = json.load(f)
        if not data:
            return results
        results.extend(data)
        page += 1


# Releases of cosmosis with a major version below this are left out
MIN_COSMOSIS_MAJOR = 2


def major_version(tag):
    m = re.match(r"[vV]?(\d+)", tag)
    return int(m.group(1)) if m else -1


def underline(text, char):
    return f"{text}\n{char * len(text)}\n"


# --- Markdown -> RST conversion for release notes ---------------------------

def inline_md_to_rst(text):
    # Code spans: `x` -> ``x``
    text = re.sub(r"(?<!`)`([^`]+)`(?!`)", r"``\1``", text)
    # Markdown links [text](url) -> `text <url>`__
    text = re.sub(r"\[([^\]]+)\]\((https?://[^)]+)\)", r"`\1 <\2>`__", text)
    # Pull request / issue URLs -> short links
    text = re.sub(
        r"https://github\.com/([\w.-]+)/([\w.-]+)/(pull|issues)/(\d+)",
        lambda m: f"`#{m.group(4)} <{m.group(0)}>`__",
        text,
    )
    # @user -> link to profile (not inside emails)
    text = re.sub(
        r"(?<![\w/@])@([A-Za-z0-9](?:[A-Za-z0-9-]*[A-Za-z0-9])?)",
        lambda m: f"`@{m.group(1)} <{GITHUB}/{m.group(1)}>`__",
        text,
    )
    return text


def release_body_to_rst(body):
    body = (body or "").replace("\r", "")
    out = []
    prev_kind = None  # "list" or "para" or None
    for raw in body.split("\n"):
        line = raw.rstrip()
        if not line.strip():
            prev_kind = None
            continue
        # "Full Changelog" links duplicate the release link, and are sometimes wrong
        if line.startswith("**Full Changelog**"):
            continue
        heading = re.match(r"^#+\s*(.*)$", line)
        bold_heading = re.match(r"^\*\*([^*]+)\*\*$", line.strip())
        if heading or bold_heading:
            title = (heading or bold_heading).group(1).strip()
            # Every release has these changes; the heading adds nothing
            if title.lower() in ("what's changed", "changes"):
                prev_kind = None
                continue
            out.append("")
            out.append(f"**{inline_md_to_rst(title)}**")
            out.append("")
            prev_kind = None
            continue
        item = re.match(r"^(\s*)[*-]\s+(.*)$", line)
        if item:
            indent = len(item.group(1).expandtabs(4))
            level = 1 if indent >= 2 else 0
            if prev_kind != "list" or (level == 1 and out and not out[-1].startswith("  ")):
                out.append("")
            elif level == 0 and out and out[-1].startswith("  "):
                out.append("")
            out.append("  " * level + "* " + inline_md_to_rst(item.group(2).strip()))
            prev_kind = "list"
            continue
        if prev_kind == "list":
            out.append("")
        if prev_kind != "para":
            out.append("")
        out.append(inline_md_to_rst(line.strip()))
        prev_kind = "para"
    return "\n".join(out).strip("\n")


# --- Page sections -----------------------------------------------------------

def cosmosis_section():
    releases = fetch_all(f"{API}/cosmosis/releases")
    releases = [r for r in releases if not r["draft"] and major_version(r["tag_name"]) >= MIN_COSMOSIS_MAJOR]
    releases.sort(key=lambda r: r["published_at"] or r["created_at"], reverse=True)
    lines = [underline("CosmoSIS", "-")]
    lines.append(
        "Changes to the core ``cosmosis`` package, taken from the "
        f"`release notes <{GITHUB}/cosmosis-developers/cosmosis/releases>`_.\n"
    )
    for r in releases:
        tag = r["tag_name"]
        date = (r["published_at"] or r["created_at"])[:10]
        lines.append(underline(tag, "~"))
        lines.append(f"*Released {date}* — `release page <{r['html_url']}>`__\n")
        body = release_body_to_rst(r["body"])
        lines.append((body or "No release notes.") + "\n")
    return "\n".join(lines)


def standard_library_section():
    pulls = fetch_all(f"{API}/cosmosis-standard-library/pulls?state=closed")
    pulls = [p for p in pulls if p["merged_at"] and p["base"]["ref"] == "main"]
    pulls.sort(key=lambda p: p["merged_at"], reverse=True)

    by_month = OrderedDict()
    for p in pulls:
        d = datetime.datetime.strptime(p["merged_at"][:10], "%Y-%m-%d")
        by_month.setdefault(d.strftime("%B %Y"), []).append(p)

    lines = [underline("CosmoSIS Standard Library", "-")]
    lines.append(
        "The standard library is released less often, so changes are listed by the month in which "
        "they were merged, taken from the "
        f"`merged pull requests <{GITHUB}/cosmosis-developers/cosmosis-standard-library/pulls?q=is%3Apr+is%3Amerged>`_.\n"
    )
    for month, prs in by_month.items():
        lines.append(underline(month, "~"))
        for p in prs:
            title = p["title"].strip()
            # Escape characters that RST would otherwise interpret
            title = title.replace("\\", "\\\\").replace("*", r"\*").replace("`", r"\`").replace("_", r"\_").replace("|", r"\|")
            user = p["user"]["login"]
            lines.append(
                f"* {title} (`#{p['number']} <{p['html_url']}>`__, "
                f"`@{user} <{GITHUB}/{user}>`__, {p['merged_at'][:10]})"
            )
        lines.append("")
    return "\n".join(lines)


def main():
    today = datetime.date.today().isoformat()
    header = underline("Changelog", "=")
    intro = (
        "This page lists changes to the two CosmoSIS repositories: the core "
        f"`cosmosis <{GITHUB}/cosmosis-developers/cosmosis>`_ package and the "
        f"`cosmosis-standard-library <{GITHUB}/cosmosis-developers/cosmosis-standard-library>`_.\n\n"
        f"It is generated from GitHub by ``generate_changelog.py`` and was last updated on {today}.\n\n"
        ".. contents::\n   :local:\n   :depth: 1\n"
    )
    text = "\n".join([header, intro, cosmosis_section(), standard_library_section()])
    with open(OUTPUT, "w") as f:
        f.write(text.rstrip() + "\n")
    print(f"Wrote {OUTPUT}")


if __name__ == "__main__":
    main()
