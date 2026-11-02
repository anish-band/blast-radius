from pathlib import Path

from blast_radius.imports import build_import_table

FIXTURES = Path(__file__).parent / "fixtures"


def test_import_alias():
    src_code = (FIXTURES / "import_alias.py").read_bytes()

    names, star_modules = build_import_table(src_code)

    assert names == {"np": "numpy"}
    assert star_modules == []


def test_import_plain():
    src_code = (FIXTURES / "import_plain.py").read_bytes()

    names, star_modules = build_import_table(src_code)

    assert names == {"numpy": "numpy"}
    assert star_modules == []


def test_from_import():
    src_code = (FIXTURES / "from_import.py").read_bytes()

    names, star_modules = build_import_table(src_code)

    assert names == {"float_": "numpy.float_"}
    assert star_modules == []


def test_from_import_alias():
    src_code = (FIXTURES / "from_import_alias.py").read_bytes()

    names, star_modules = build_import_table(src_code)

    assert names == {"f": "numpy.float_"}
    assert star_modules == []


def test_import_submodule_alias():
    src_code = (FIXTURES / "import_submodule_alias.py").read_bytes()

    names, star_modules = build_import_table(src_code)

    assert names == {"la": "numpy.linalg"}
    assert star_modules == []


def test_import_submodule():
    src_code = (FIXTURES / "import_submodule.py").read_bytes()

    names, star_modules = build_import_table(src_code)

    assert names == {"numpy": "numpy"}
    assert star_modules == []


def test_from_import_star():
    src_code = (FIXTURES / "from_import_star.py").read_bytes()

    names, star_modules = build_import_table(src_code)

    assert names == {}
    assert star_modules == ["numpy"]


def test_comment_and_string():
    src_code = (FIXTURES / "comment_and_string.py").read_bytes()

    names, star_modules = build_import_table(src_code)

    assert names == {"np": "numpy"}
    assert star_modules == []
