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

Pull request titles are not always clear on their own, so DESCRIPTION_OVERRIDES
below can replace the description of any pull request, keyed by repository and
PR number.  Overrides are written in RST (e.g. ``module_name``), and are used
both for standard library PRs and for PR bullet points in cosmosis release notes.
"""
# Replacement descriptions for pull requests whose titles are unclear.
# Keys are repository name, then PR number. Values are RST text.
DESCRIPTION_OVERRIDES = {
    "cosmosis": {
        11: "Fix sampler chaining failing when an output file is used, and add a test for it",
        13: "Build the CosmoSIS core library when installing in developer mode with ``pip install -e``",
        17: "Fix ``cosmomc`` output format to put the posterior in the second column instead of the last",
        32: "Fix the default of the ``no_2d`` postprocessing option in interactive mode and simplify imports from ``cosmosis.postprocessing``",
        33: "Fix saving vector-valued extra output quantities as multiple columns in the output file",
        35: "Fix ``zeus`` sampler tuning never ending when ``patience`` is larger than ``nsteps``",
        36: "Add ``--ports`` option to ``cosmosis-configure`` to print environment settings for MacPorts",
        38: "Add trace plots for MCMC samplers to ``cosmosis-postprocess``, add ``dynesty`` postprocessing, and allow ``sample=auto`` in ``dynesty``",
        50: "Add ``COSMOSIS_NO_SUBPROCESS`` environment variable to skip pre/post-run scripts and other subprocess launches",
        56: "Raise a Python exception instead of crashing when ``DataBlock`` put/get is used with the wrong array type",
        63: "Add ``covmat_sample_start`` option to the ``metropolis`` sampler to draw the starting point from the covariance matrix",
        66: "Improve error messages when a pipeline module file is missing or has an unrecognised suffix, and add tests",
        71: "Fix ``multinest`` and ``polychord`` output of vector-valued extra quantities",
        82: "Fix ``dynesty`` and ``nautilus`` samplers using the posterior instead of the likelihood",
        83: "Expose new run options from ``nautilus`` 0.6 in the ``nautilus`` sampler",
        86: "Allow passing new priors to the ``run_cosmosis`` function",
        87: "Add corner plots to ``cosmosis-postprocess`` and switch to a faster, more accurate KDE method by default",
        90: "Update the ``nautilus`` sampler interface: remove ``n_jobs``, share one parallel pool, and raise default live points to 2000",
        94: "Add postprocessing plots for the ``apriori`` sampler and allow it to resume",
        95: "Fix values passed to ``run_cosmosis`` (e.g. by the campaign tool) being ignored when running under MPI",
        98: "Add a ``from_likelihood_function`` method to build a pipeline directly from a single likelihood function",
        99: "Fix bugs in the pipeline ``from_likelihood_function`` method",
        110: "Avoid crashing when git revision metadata for output headers cannot be read",
        117: "Check for duplicate keys in ``cosmosis-campaign`` YAML files",
        121: "Fix CI workflow failure caused by missing ``gfortran``",
        125: "Fix inheritance of components and environment variables from parent files and runs in ``cosmosis-campaign``",
        133: "Expose the ``n_steps`` parameter for the ``pocomc`` sampler",
        143: "Fix the getdist branch of postprocessing statistics to also report the automatically found max-like and max-post samples",
        156: "Pass the Hessian from the ``bobyqa`` method to the ``maxlike`` sampler so it can save covariance outputs",
        171: "Fix a crash when totalling pipeline call counts at the end of runs using the SMP process pool",
        172: "Add a numeric index to output file names when the same sampler appears more than once in a chained ``sampler`` list",
        176: "Stop errors reading module attribution (``module.yaml``) files from crashing runs",
        183: "Fix a ``DataBlock`` logging bug when storing string arrays",
        184: "Use a more robust fix for the ``DataBlock`` logging crash with long type names",
        188: "Make ``cosmosis-campaign`` use the ``output_name`` setting for ``test``, ``multinest`` and ``polychord`` output files",
        191: "Fix malformed Fortran format strings in ``polychord`` progress and stats output that caused crashes",
        196: "Allow the documented ``smooth`` method to be used when running the ``fisher`` sampler",
        206: "Add a ``cosmopower_train`` sampler for training CosmoPower emulators, and a ``latin_hypercube`` sampler",
        210: "Simplify use of ``hermitian=True`` when inverting covariance matrices in ``GaussianLikelihood``, falling back for older numpy",
        212: "Fix ``Inifile.items`` interpolation with newer Python versions",
        219: "Add methods to quickly serialize and deserialize a ``DataBlock`` to a binary file",
        251: "Change ``multinest`` and ``polychord`` Fortran wrappers and build flags so the libraries do not need an executable stack on Linux",
    },
    "cosmosis-standard-library": {
        2: "Add DES Y3 example pipelines and data, the ``tatt`` intrinsic alignment and Y3 shear-ratio modules, and eBOSS likelihoods; update ``2pt_like`` and ``save_2pt``",
        3: "Add ``get-planck-data.sh`` to download the Planck 2018 likelihood data, and a CI test of the ``planck2018`` likelihood",
        4: "Update the ``project_2d`` documentation and remove unused parameters",
        6: "Fix all demos for CosmoSIS 2.0.3+, including fixes to ``isitgr``, ``extrapolate_power``, ``camb`` D(z) and f(z) outputs, and PPF shear in ``project_2d``",
        9: "Update the ``class`` module to use CLASS v3.2.0, and use the same neutrino and ``TCMB`` parameter names as ``camb``",
        10: "Fix the ``delta_tot_de`` power spectrum name in the ``camb`` module and a section name in ``mf_tinker``",
        12: "Fix building the ``planck2018`` likelihood on Apple Silicon by removing some compiler flags",
        13: "Add MacOS to the conda CI tests and fix the ``class`` build on MacOS",
        14: "Fix loading the GSL cblas library in ``project_2d`` on NERSC",
        15: "Fix the theta-to-H0 conversion in the ``consistency`` module for curved models (``omega_k``) and speed it up",
        16: "Fix the ``gunzip`` command in the ``class`` module Makefile for older systems",
        17: "Fix a crash in one mode of the ``boss_dr12`` likelihood",
        18: "Add a WMAP9 data download script, fix the RPATH in the ``wmap9`` likelihood Makefile, and add a CI test",
        19: "Add the ``EuclidEmulator2`` non-linear matter power spectrum emulator module and an example pipeline",
        21: "Add a ``log_w_model`` module for a logarithmic w(z) dark energy model, with an example pipeline",
        22: "Remove remaining Python 2 compatibility code from ``2pt`` and ``cl_to_xi_fullsky``, and an unused ``extrapolate`` step from the DES Y3 example",
        25: "Add a cache for P(k, chi) interpolation in ``project_2d`` to speed up C_ell calculations",
        26: "Fix setting HMCode parameters for ``mead2020`` and ``mead2020_feedback`` in the ``camb`` module",
        27: "Fix the name of the ``accurate_massive_neutrino_transfers`` parameter in the ``camb`` module",
        28: "Add the ``cosmic_emu_2022`` module for the 2022 Mira-Titan emulator, with a DES Y3 example pipeline",
        32: "Restore the ``save_kernels`` option in ``project_2d`` to save the Limber integral kernels to the block",
        33: "Save the linear CDM+baryon power spectrum (``cdm_baryon_power_lin``) in the ``class`` module",
        34: "Fix the header of the ``logPkRatio_TNG100.dat`` data file in the ``baryon_power_scaling`` module",
        35: "Replace ``cl_to_corr`` with a new version that works with modern scipy and with ``2pt_like``",
        36: "Fix OpenMP compiler flags in the ``planck2018`` likelihood Makefile on MacOS",
        37: "Add a ``do_bao`` option to the ``camb`` module to skip BAO quantities for speed, and use it in demos",
        44: "Add the option to sample ``sigma_8_input`` instead of ``A_s`` in the ``camb`` module",
        48: "Fix the ``theta_H0_range`` option in the ``camb`` module",
        50: "Add a DES Y3 example using ``class``, fixing ``class`` P(k) ordering, distances and massive neutrinos, and ``fast_pt`` grid handling",
        52: "Generalize the DES Y3 ``shear_ratio`` likelihood to read the number of ratios per lens bin from its data files",
        56: "Fix the D(z) growth calculation in the ``camb`` module, which may have affected BAO",
        57: "Speed up the Pantheon example by using ``astropy_background`` instead of ``camb``",
        59: "Add the DES+SPT/Planck Y3 6x2pt example pipeline, with CMB lensing updates to ``project_2d``, ``2pt_like`` and related modules",
        63: "Change the download URL for Planck likelihood data in ``get-planck-data.sh``",
        65: "Add the missing scale-cuts file for the DES Y3 6x2pt example",
        66: "Add the DES Y3 6x2pt example to the CI tests",
        67: "Fix magnification in the DES Y3 6x2pt example and a message condition in ``add_magnification``",
        69: "Add a BAO example pipeline and CI test, and fix the eBOSS DR16 BAO likelihoods",
        71: "Remove a generated source file from the ``EuclidEmulator2`` module from version control",
        73: "Add the DES Y3 BAO likelihood (``des-y3-bao``)",
        75: "Fix the FAST-PT bias calculation in ``project_2d`` (``fastpt_tools.py``), including swapped ``sig3nl`` and ``sig4`` terms",
        76: "Remove a claim in a ``save_2pt.py`` comment that its real-space covariance is not accurate enough for inference",
        81: "Allow ``project_2d`` to pair a tracer-matter cross spectrum with different source tomographic bins",
        82: "Fix the build of the ``class`` and ``EuclidEmulator2`` modules by installing their Python packages with pip",
        84: "Add the mean of the shifted n(z) as an output of the ``photoz_bias`` module",
        86: "Speed up sampling of ``sigma_8`` in the ``camb`` module by computing the transfer function only once",
        87: "Add the ACT DR6 CMB lensing likelihood and example pipeline",
        88: "Update demos and example pipelines for CosmoSIS 3 (``verbosity`` replaces ``quiet``) and patch ``fast_pt`` for newer NumPy",
        91: "Allow sampling in ``S_8`` in the ``consistency`` module",
        92: "Improve the ``consistency`` module documentation on relations files and add an ``extra_relations`` option",
        96: "Add metadata keys to the backup GG-only shear section created by ``add_intrinsic``",
        97: "Cache Planck and WMAP data in the CI tests to avoid repeated downloads",
        98: "Add the DES Y3 + KiDS-1000 hybrid analysis: example pipeline, data file, ``correlated_priors`` module and ``cosebis`` module",
        99: "Add a KiDS-1000 COSEBIs-only example pipeline",
        101: "Restore Gaussian priors on Planck nuisance parameters in the Planck example pipelines",
        103: "Raise an error in ``camb`` if the ``consistency`` module's ``cosmomc_theta`` conversion is used with a tabulated w(a)",
        104: "Require the ``act_dr6_lenslike`` package from PyPI in the ACT DR6 lensing likelihood instead of bundling it",
        105: "Add the HSC Y3 cosmic shear likelihood and example pipelines, with related ``sacc`` likelihood updates",
        108: "Use plik-lite in the Planck example pipelines to reduce the parameter space",
        110: "Replace nonstandard ``#elseif`` with ``#elif`` in the Planck 2018 likelihood C code",
        111: "Add the Planck NPIPE likelihood and example pipeline",
        112: "Raise an error in ``project_2d`` when ``zmax`` is too low for CMB lensing",
        113: "Fix low-k extrapolation with the ``kmin`` option in the ``camb`` module and respect ``zmid`` in redshift sampling",
        118: "Save the transfer function to the data block in the ``camb`` module",
        119: "Document the TDCOSMO likelihood and rename its example files",
        121: "Remove an import of the removed ``scipy.zeros`` from the eBOSS DR16 ELG likelihood",
        124: "Add Python 3.12 to the CI tests",
        129: "Skip the ``baccoemu`` tests on Python 3.12 or newer",
        132: "Add the DESI DR1 BAO likelihood and DESI example pipelines",
        133: "Update ``class``, ``gaussian_window``, ``nz_multirank``, ``add_gammat_point_mass`` and ``baccoemu`` for newer SciPy",
        136: "Fix a bug reading section options in the ``sacc`` likelihood",
        137: "Add a ``candl`` likelihood interface for ACT and SPT CMB likelihoods",
        138: "Alias ``scipy.integrate.trapz`` to ``trapezoid`` in the ``fast_pt`` modules for newer SciPy",
        141: "Add galaxy density and galaxy-shear Cl data types and a ``flip`` option to the ``sacc`` likelihood",
        142: "Add the ``amod`` module for the ``A_mod`` suppression of non-linear power (Amon & Efstathiou 2022)",
        143: "Take the growth rate f(z) for RSD in ``project_2d`` from the data block instead of a spline fit",
        145: "Update CI tests to use CosmoSIS 3.13 and the latest SciPy",
        146: "Support NumPy 2: update the ``class`` module to CLASS 3.2.5, remove ``interp2d`` usage, drop Python 3.7 and 3.8",
        147: "Fix the ``class`` module build to use the configured Python and update CI setup",
        148: "Add a DES Y3 + Planck example pipeline and update the DES Y3 shear ratio likelihood for newer NumPy",
        149: "Fix the Makefile for CLASS 3.2.5 in the ``class`` module",
        150: "Fix ``astropy_background`` for newer astropy and the Planck 2018 likelihood build at NERSC",
        151: "Update the NERSC test script",
        152: "Allow saving CMB kappa Fourier-space spectra in the ``2pt`` likelihood files",
        153: "Save effective ell values for plotting in the ``planck_py`` (Planck-lite) likelihood",
        155: "Add the DESI DR2 BAO likelihood and example pipelines",
        156: "Allow setting the mean of a correlated prior in the ``correlated_priors`` module",
        158: "Add a ``random_fail`` utility module for testing failure handling, and update CI runners",
        160: "Add a DES Y6 shear ratio likelihood that uses only the two geometric ratios",
        164: "Pass extra reionization parameters to the tanh reionization model in the ``camb`` module",
        166: "Fix per-bin IA amplitude parameter names in ``add_intrinsic`` so ``a1_1`` is not confused with the power-law ``a1`` parameter",
        170: "Add a background-only mode and improved parameter handling to the ``class`` module, with a new ``desi_dr2_class.ini`` example",
        171: "Pin the ``candl`` likelihood to candl 1.x and add DES Y3 Euclid-emulator and DES Y5 supernova example files",
        173: "Update the ``candl`` likelihood interface for candl 2.0",
        174: "Add DES Y6 BAO likelihood modules, including a 5-bin version, and update the BAO example",
        175: "Add Python 3.12 and 3.13 to the continuous-integration tests",
        176: "Update the second CI workflow job to test Python 3.10 to 3.13, dropping 3.9",
        177: "Rename the misnamed DES Y3 ``6x2pt`` example to ``5x2pt`` and add a genuine DES Y3 6x2pt example pipeline",
        178: "Update imports in ``fast_pt`` and the ``project_2d`` FAST-PT tools to support FAST-PT v4",
        181: "Fix a two-multipole offset in the ACT DR6 and ACT DR6 lite likelihood interfaces and expand their documentation",
        185: "Fix the z=0 index of the transfer function output by the ``camb`` module",
        189: "Add a DECam13k likelihood example pipeline and test",
        190: "Fix bugs in the ``add_colours``, ``flexible_grid`` and ``la_model_higher_order`` intrinsic alignment modules",
        191: "Remove a repeated call to ``load_kernels`` in ``project_2d``",
        195: "Generalise the HSC, one-point and real-space two-point parts of the ``sacc`` likelihood and add a ``delta_window`` n(z) module",
        201: "Speed up the Limber integration in ``project_2d`` when there are many tomographic bins",
        202: "Add the ``project_1d`` module for one-point statistics (stellar mass and luminosity functions)",
        207: "Implement bin averaging with SACC weights for one-point statistics in the ``sacc`` likelihood",
        208: "Fix the ``lollipop`` likelihood interface to use unscaled C_ell values, which biased tau",
        209: "Fix the ``consistency`` module when ``cosmomc_theta`` is used as input in non-Lambda dark energy models",
        212: "Save the data covariance and inverse covariance in the ``candl`` likelihood so it can be used with the Fisher sampler",
        213: "Add the TDCOSMO 2025 lensing time-delay likelihood and example pipelines",
        214: "Replace the deprecated pandas ``delim_whitespace`` argument in the ``pantheon_plus_shoes`` likelihood",
        223: "Add a ``onepower`` interface module and support for it in ``project_1d``",
        224: "Fix the non-Limber calculation in ``project_2d`` when kernels have zero overlap",
        231: "Update the ``camb`` module for CAMB v2 (e.g. ``lens_output_margin``), with related fixes to ``candl``, ``cluster_evs`` and ``spk``",
        236: "Correct matter power units and output documentation in the ``camb`` and ``class`` module metadata",
        244: "Remove the ``-m64`` compiler flag on aarch64 in the ``planck2018`` likelihood build",
        248: "Add the DES Y6 3x2pt likelihood, data and examples, plus new modules from the DES internal fork such as ``photoz_uz``, ``ia_marg`` and ``hmcode2020emu``",
        250: "Fix the continuous-integration workflow with conda package caching, a pinned CosmoSIS 3.27.1 and a reduced macOS test matrix",
        251: "Update the ``camb`` module for CAMB 2.0.5 by setting non-linear lensing explicitly, and test against it in CI",
    },
}

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


PR_BULLET = re.compile(
    r"^(?P<indent>\s*(?:[*-]\s+)?)(?P<text>.*?)(?P<rest>(?:\s+by)?\s+(?:@\S+\s+)?in\s+"
    r"https://github\.com/[\w.-]+/cosmosis/pull/(?P<num>\d+).*)$"
)


def override_pr_bullet(line):
    """Swap the description in a release-note PR bullet for its override, if any.

    Returns the line, with the override marked by a placeholder so it is not
    passed through the markdown conversion (overrides are already RST).
    """
    m = PR_BULLET.match(line)
    if not m or "made their first contribution" in line:
        return line, None
    override = DESCRIPTION_OVERRIDES["cosmosis"].get(int(m.group("num")))
    if override is None:
        return line, None
    return f"{m.group('indent')}\x00{m.group('rest')}", override


def release_body_to_rst(body):
    body = (body or "").replace("\r", "")
    out = []
    prev_kind = None  # "list" or "para" or None
    for raw in body.split("\n"):
        line, override = override_pr_bullet(raw.rstrip())
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
            text = inline_md_to_rst(item.group(2).strip())
            if override is not None:
                text = text.replace("\x00", override)
            out.append("  " * level + "* " + text)
            prev_kind = "list"
            continue
        if prev_kind == "list":
            out.append("")
        if prev_kind != "para":
            out.append("")
        text = inline_md_to_rst(line.strip())
        if override is not None:
            text = text.replace("\x00", override)
        out.append(text)
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
            title = DESCRIPTION_OVERRIDES["cosmosis-standard-library"].get(p["number"])
            if title is None:
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
