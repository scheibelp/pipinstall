"""
This init is distributed within a "spack" directory in site-packages, along
with the completely untouched Spack source code. It exists so that users can
e.g. `import spack.concretize as sc; sc.concretize_one("zlib")`.
"""
from __future__ import annotations

from importlib.resources import files, as_file

# I don't want to treat this as a namespace split across multiple
# "spack" directories.
# __path__ = pkgutil.extend_path(__path__, __name__)  # type: ignore[name-defined]

def _bootstrap_real_spack_init() -> None:
    # This is the *actual* spack package directory containing paths.py, spec.py, etc.
    vendored_pkg = files("pipspack").joinpath("spack/lib/spack/spack")

    with as_file(vendored_pkg) as pkg_path:
        pkg_path = str(pkg_path)

        # For `import spack.paths` to work, pkg_path must be in spack.__path__
        if pkg_path not in __path__:  # type: ignore[attr-defined]
            __path__.append(pkg_path)  # type: ignore[attr-defined]

        init_path = files("pipspack").joinpath("spack/lib/spack/spack/__init__.py")
        with as_file(init_path) as init_fs_path:
            init_fs_path = str(init_fs_path)

            g = globals()
            g["__file__"] = init_fs_path
            g["__package__"] = __name__

            with open(init_fs_path, "rb") as f:
                code = compile(f.read(), init_fs_path, "exec")
            exec(code, g, g)

_bootstrap_real_spack_init()
