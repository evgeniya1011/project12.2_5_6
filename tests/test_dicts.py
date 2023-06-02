from utils.dicts import get_val


def test_get_val(dicts_fixture):
    assert get_val(dicts_fixture, "turkiye", "git") == "merhaba"
    assert get_val(dicts_fixture, "italiya", "привет") == "buongiorno"
    assert get_val(dicts_fixture, "russiya", "finish") == "finish"
    assert get_val({}, "turkiye") == "git"