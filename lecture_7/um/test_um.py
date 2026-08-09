from um import count


def test_basic():
    assert count("um") == 1
    assert count("hello, um, world") == 1


def test_case_insensitive():
    assert count("Um") == 1
    assert count("UM") == 1
    assert count("uM") == 1


def test_punctuation():
    assert count("um?") == 1
    assert count("Um, thanks, um...") == 2


def test_not_part_of_word():
    assert count("yummy") == 0
    assert count("album") == 0
    assert count("umbrella") == 0


def test_multiple():
    assert count("um, um, um") == 3
