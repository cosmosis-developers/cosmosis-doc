---
name: update-changelog
description: Refresh help/changelog.rst from GitHub, reviewing any new cosmosis / cosmosis-standard-library pull requests and writing clearer descriptions for the unclear ones. Use when asked to update, refresh or regenerate the changelog.
---

# Update the CosmoSIS changelog

`generate_changelog.py` builds `help/changelog.rst` from:
- the GitHub release notes of `cosmosis-developers/cosmosis` (one section per release, v2.0 onwards), and
- the merged pull requests (into `main`) of `cosmosis-developers/cosmosis-standard-library`, grouped by month.

At the top of the script, two dictionaries record which PRs have already been reviewed:
- `DESCRIPTION_OVERRIDES[repo][number]`: a clearer RST description that replaces the original title or release-note text.
- `REVIEWED_UNCHANGED[repo]`: PRs whose original description was already clear.

A PR in neither dictionary has not been reviewed yet. Your job is to review those PRs, record the results, and regenerate the page.

## Environment

`gh`, Sphinx and docutils are in the `cosmosis` conda env:

```bash
source ~/miniforge3/etc/profile.d/conda.sh && conda activate cosmosis
export GITHUB_TOKEN=$(gh auth token)   # avoids the 60/hour unauthenticated API limit
```

## Steps

1. **List the unreviewed PRs.**

   ```bash
   python generate_changelog.py --unreviewed
   ```

   Output is tab-separated: repo, PR number, release tag or merge date, current description. If it prints nothing, go to step 4.

2. **Review each PR.** Decide whether a reader of the changelog can tell what changed and where. If you can't tell, look at the PR:

   ```bash
   gh pr view N -R cosmosis-developers/<repo> --json title,body,files
   gh pr diff N -R cosmosis-developers/<repo> | head -300
   ```

   The changed-file list is usually the quickest way to see which module or sampler is affected. If there are more than about 30 PRs, split them across a few parallel sub-agents. Give each one these criteria and ask it to write a JSON list of `{number, old, new, reason}` to a scratchpad file. Check those files exist before using them, and spot-check any surprising rewrites against the PR.

   A description needs an override when:
   - it doesn't say which module, sampler or tool is affected ("Fix bug", "Testing CI Fixes", "Camb 2.0.5");
   - it uses a branch name or internal jargon ("Residual Y3 changes", "Merge dev");
   - it misstates or leaves out the main thing the PR did;
   - it has a typo that hurts the meaning.

   Don't rewrite clear descriptions for style alone.

   Style for overrides:
   - one line, ideally under ~25 words, no trailing full stop, starting with a verb ("Fix …", "Add …", "Update …");
   - name the module or sampler, e.g. "the ``camb`` module", "the ``emcee`` sampler", "``cosmosis-campaign``";
   - write RST, not markdown: put identifiers, file names, options and anything containing `_` or `*` in ``double backticks``;
   - state only what the PR shows, without inventing a motivation.

3. **Record the results** in `generate_changelog.py`. Add each override to `DESCRIPTION_OVERRIDES` under its repo, keeping the numbers sorted. Add every other reviewed PR number to `REVIEWED_UNCHANGED`. When you finish, `python generate_changelog.py --unreviewed` should print nothing.

4. **Regenerate and validate.**

   ```bash
   python generate_changelog.py
   docutils --halt=5 --report=2 help/changelog.rst /dev/null && echo OK
   ```

   Fix any RST warnings. They usually come from an unescaped `_`, `*` or backtick in an override. Then check with `git diff help/changelog.rst` that the only changes are the new entries, the changed descriptions and the date.

5. **Report back.** Say how many PRs were new, which ones got overrides (old → new), and any you weren't sure about. Point out very large PRs whose summary covers only the main changes, and CI-only changes the user might drop. Don't commit unless the user asks.

## Notes

- Release-note text that has no PR link (e.g. "Fix a bug when running the Minuit sampler") can't be overridden and isn't listed by `--unreviewed`.
- PR numbers in old cosmosis release notes point at `joezuntz/cosmosis`. The numbers are the same in `cosmosis-developers/cosmosis`.
- If a PR's text appears in several releases (e.g. v2.1.1 and v2.1.3), one override covers all of them.
