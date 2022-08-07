import config

def test_is_verbose_fails(tmpdir):
    path = tmpdir.mkdir("etc").join("app.conf")
    path.write("[main]")

    assert config.is_verbose(path.strpath) is True
