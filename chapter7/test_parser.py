import pytest
import sys
import cli

def test_help_output_is_generated(capsys):
    sys.argv = ["cli.py", "-h"]

    with pytest.raises(SystemExit):
        cli.main()

    stdout, stderr = capsys.readouterr()

    assert "usage: cli [-h] [--foo FOO]" in stdout
    assert "--foo FOO   the foo option!" in stdout
