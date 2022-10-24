import pytest
from katas.bowling import SYMBOL_LOOKUP, STRIKE, SPARE, Frame, Game, MISS, LastFrame


@pytest.mark.parametrize(
    "param, expected",
    (
        (STRIKE, 10),
        (SPARE, 10),
        ("1", 1),
        (MISS, 0),
        # (None, 0)
    ),
)
def test_symbol_lookup(param, expected):
    assert SYMBOL_LOOKUP[param] == expected


@pytest.mark.parametrize(
    "rolls",
    (
        (MISS, MISS),
        (MISS, "/"),
        (MISS, "9"),
        ("1", "/"),
        ("X", None),
        ("5", "4"),
        ("1", 2),
    ),
)
def test_validate_rolls(rolls):
    Frame(rolls[0])


def test_bonus_two():
    frame = LastFrame(STRIKE)
    frame.extra_one = STRIKE
    frame.extra_two = STRIKE
    assert frame.score() == 30


def test_bonus_one():
    frame = LastFrame("5")
    frame.second_throw = SPARE
    frame.extra_one = STRIKE
    assert frame.score() == 20


@pytest.mark.parametrize(
    "line, expected, num_rolls",
    (
        ("-- -- -- -- -- -- -- -- -- -- ", 0, 20),  # All misses
        ("X X X X X X X X X X X X", 300, 12),  # All strikes
        ("9- 9- 9- 9- 9- 9- 9- 9- 9- 9-", 90, 20),  # All nines and misses
        ("9- 5/ 9- 9- 9- 9- 9- 9- 9- 9-", 100, 20),
        ("9- X 5/ 9- 9- 9- 9- 9- 9- 9-", 72 + 20 + 19, 19),
        ("5/ 5/ 5/ 5/ 5/ 5/ 5/ 5/ 5/ 5/5", 150, 21),  # All  fives
    ),
)
def test_rolls(line, expected, num_rolls):
    game = Game()
    game.game_from_line(line)

    assert game.total_rolls() == num_rolls
    assert game.total_score() == expected
