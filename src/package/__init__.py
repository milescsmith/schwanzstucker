from importlib.metadata import PackageNotFoundError, version

from package import func_to_make_available

try:
    if isinstance(__package__, str):
        __version__ = version(__package__)
    else:
        __version__ = "unknown"
except PackageNotFoundError:  # pragma: no cover
    __version__ = "unknown"

__all__: list[str] = ["func_to_make_available"]