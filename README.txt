cd into pipspack and `git clone https://github.com/spack/spack.git`
in this directory: python -m build
this generates
  dist/pipspack-0.1.0.tar.gz
now you can
  activate a venv
  pip install <that-dist-file>
  spack --help
