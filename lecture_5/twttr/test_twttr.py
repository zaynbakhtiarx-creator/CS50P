from twttr import shorten


def test_lowercase():
    assert shorten("hello") == "hll"


def test_uppercase():
    assert shorten("HELLO") == "HLL"


def test_no_vowels():
    assert shorten("rhythm") == "rhythm"


def test_all_vowels():
    assert shorten("aeiouAEIOU") == ""


def test_numbers_symbols():
    assert shorten("hello123!") == "hll123!"
