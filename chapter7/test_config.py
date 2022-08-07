import config

def test_is_verbose_fails(tmpdir):
    path = tmpdir.mkdir("etc").join("app.conf")
    path.write("[main]")

    assert config.is_verbose(path.strpath) is True

def test_is_verbose_succeeds_false(tmpdir):
    path = tmpdir.mkdir("etc").join("app.conf")
    path.write("[main]\nverbose = 0")

    assert config.is_verbose(path.strpath) is False

def test_is_verbose_succeeds_true(tmpdir):
    path = tmpdir.mkdir("etc").join("app.conf")
    path.write("[main]\nverbose = 1")

    assert config.is_verbose(path.strpath) is True
