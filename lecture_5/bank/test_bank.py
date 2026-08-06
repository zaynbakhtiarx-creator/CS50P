from bank import fine


def test_hello():
    assert fine("hello") == "$0"


def test_hello_with_extra_words():
    assert fine("hello there") == "$0"


def test_h():
    assert fine("hi") == "$20"


def test_h_uppercase():
    assert fine("HEY") == "$20"


def test_other():
    assert fine("good morning") == "$100"


def test_empty():
    assert fine("") == "$100"
