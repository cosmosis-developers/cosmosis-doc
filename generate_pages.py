import generate_sampler_pages
import generate_module_pages
import tempfile
import os
import shutil
import argparse

def shallow_clone(repo, dest):
    cmd = "git clone --depth 1 {} {}".format(repo, dest)
    os.system(cmd)

def update_or_clone(repo, dest):
    if os.path.isdir(dest):
        cmd = f"git -C {dest} pull --ff-only"
        os.system(cmd)
    else:
        shallow_clone(repo, dest)

def main(here=False):
    os.makedirs("reference/standard_library", exist_ok=True)
    os.makedirs("reference/samplers", exist_ok=True)
    if here:
        tmpdir = "_cosmosis_build"
        os.makedirs(tmpdir, exist_ok=True)

        cosmosis_dir = os.path.join(tmpdir, 'cosmosis')
        update_or_clone('https://github.com/cosmosis-developers/cosmosis', cosmosis_dir)
        generate_sampler_pages.main(cosmosis_dir)
        shutil.copy(f"{cosmosis_dir}/cosmosis/version.py", "./cosmosis_version.py")

        csl_dir = os.path.join(tmpdir, 'cosmosis-standard-library')
        update_or_clone('https://github.com/cosmosis-developers/cosmosis-standard-library', csl_dir)
        generate_module_pages.main(csl_dir)
    else:
        with tempfile.TemporaryDirectory() as tmpdir:
            cosmosis_dir = os.path.join(tmpdir, 'cosmosis')
            shallow_clone('https://github.com/cosmosis-developers/cosmosis', cosmosis_dir)
            generate_sampler_pages.main(cosmosis_dir)
            shutil.copy(f"{cosmosis_dir}/cosmosis/version.py", "./cosmosis_version.py")

            csl_dir = os.path.join(tmpdir, 'cosmosis-standard-library')
            shallow_clone('https://github.com/cosmosis-developers/cosmosis-standard-library', csl_dir)
            generate_module_pages.main(csl_dir)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--here",
        action="store_true",
        help="Use persistent local _cosmosis_build directory instead of a temporary one",
    )
    args = parser.parse_args()
    main(here=args.here)
