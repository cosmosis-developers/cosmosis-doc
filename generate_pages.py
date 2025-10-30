import generate_sampler_pages
import generate_module_pages
import tempfile
import os
import shutil

def shallow_clone(repo, dest):
    cmd = "git clone --depth 1 {} {}".format(repo, dest)
    os.system(cmd)

def main():
    os.makedirs("reference/standard_library", exist_ok=True)
    os.makedirs("reference/samplers", exist_ok=True)

    cosmosis_dir = 'cosmosis'
    shallow_clone('https://github.com/cosmosis-developers/cosmosis', cosmosis_dir)
    generate_sampler_pages.main(cosmosis_dir)
    shutil.copy(f"{cosmosis_dir}/cosmosis/version.py", "./cosmosis_version.py")


    # We don't need to keep CSL source files, so use a temp dir
    with tempfile.TemporaryDirectory() as tmpdir:

        csl_dir = os.path.join(tmpdir, 'cosmosis-standard-library')
        shallow_clone('https://github.com/cosmosis-developers/cosmosis-standard-library', csl_dir)
        generate_module_pages.main(csl_dir)

if __name__ == '__main__':
    main()
