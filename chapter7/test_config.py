import pytest
import config

@pytest.fixture
def c(tmpdir):
    template = """
[main]
verbose = {verbose_value}
    """

    def apply(verbose_value=True):
        path = tmpdir.mkdir("etc").join("app.conf")
        path.write(template.format(verbose_value=verbose_value))

        return path.strpath

    return apply

def test_is_verbose_fails(tmpdir):
    path = tmpdir.mkdir("etc").join("app.conf")
    path.write("[main]")

    assert config.is_verbose(path.strpath) is True

def test_is_verbose_succeeds_false(c):
    config_path = c(verbose_value=False)

    assert config.is_verbose(config_path) is False

def test_is_verbose_succeeds_true(c):
    config_path = c()

    assert config.is_verbose(config_path) is True
