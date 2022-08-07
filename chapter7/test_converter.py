from distutils.util import strtobool
import converter

class TestStrToBool(object):
    def test_y_is_true(self):
        assert converter.strtobool("y") is True

    def test_1_is_true(self):
        assert converter.strtobool("1") is True
    
    def test_Y_is_true(self):
        assert converter.strtobool("Y") is True

    def test_yes_is_true(self):
        assert converter.strtobool("yes") is True

    def test_YES_is_true(self):
        assert converter.strtobool("YES") is True
