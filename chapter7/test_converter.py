import pytest
import converter

class TestStrToBool(object):
    @pytest.mark.parametrize("user_input", ["y", "Y", "yes", "YES", "1", 1])
    def test_true_values(self, user_input):
        assert converter.strtobool(user_input) is True

