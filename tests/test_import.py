import mcap


def test_import_and_version() -> None:
    assert isinstance(mcap.__version__, str)
    assert len(mcap.__version__) > 0
