from utils.dicts import get_val

data = {"english": "hello", "turkiye": "merhaba", "italiya": "buongiorno"}

def test_get_val():
    assert get_val(data, "turkiye", "git") == "merhaba"
    assert get_val(data, "italiya", "привет") == "buongiorno"
    assert get_val(data, "russiya", "finish") == "finish"
    assert get_val({}, "english") == "git"