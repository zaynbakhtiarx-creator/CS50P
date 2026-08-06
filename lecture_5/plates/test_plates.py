from plates import is_valid


def test_valid():
    assert is_valid("CS50")
    assert is_valid("HELLO")
    assert is_valid("AA123")


def test_too_short():
    assert not is_valid("A")
    assert not is_valid("A1")


def test_too_long():
    assert not is_valid("ABCDEFG")


def test_start_with_number():
    assert not is_valid("50CS")


def test_zero_rule():
    assert not is_valid("CS01")
    assert not is_valid("CS0")


def test_numbers_after_letters():
    assert is_valid("CS50")
    assert not is_valid("CS5A")


def test_invalid_characters():
    assert not is_valid("CS-50")
    assert not is_valid("CS 50")
    assert not is_valid("CS.50")
