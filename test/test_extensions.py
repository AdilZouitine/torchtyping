import pathlib
import pytest
import sys

_here = pathlib.Path(__file__).resolve().parent
sys.path.append(str(_here / ".." / "examples"))


import extensions


def test_extensions():
    extensions.valid_foo()
    with pytest.raises(TypeError):
        extensions.invalid_foo()