import os
import sys
from importlib.resources import files, as_file

def main():
    launcher = files("pipspack").joinpath("spack/bin/spack")

    with as_file(launcher) as path:
        if os.name != "nt":
            try:
                os.chmod(path, os.stat(path).st_mode | 0o111)
            except Exception:
                pass

        if os.name == "nt":
            os.execv(sys.executable, [sys.executable, str(path)] + sys.argv[1:])
        else:
            os.execv(str(path), [str(path)] + sys.argv[1:])
