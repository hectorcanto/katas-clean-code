import logging


logger = logging.getLogger(__name__)


class AuxCoolDict(dict):
    """Returns an int if the key is missing"""

    def __missing__(self, key):
        return int(key)


STRIKE = "X"
SPARE = "/"
MISS = "-"
SYMBOL_LOOKUP = AuxCoolDict({STRIKE: 10, SPARE: 10, None: 0, MISS: 0})
REGULAR_ROLLS = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
ROLLS = REGULAR_ROLLS + [STRIKE, SPARE, MISS]


class Frame:

    first_throw = second_throw = None
    is_last = False

    def __init__(self, first: str):
        self.validate_roll(first)
        self.first_throw = first

    @staticmethod
    def validate_roll(first: str):
        if first not in ROLLS or first == SPARE:
            raise ValueError(f"Invalid first throw {first}")

    def num_rolls(self):
        all_rolls = [self.first_throw, self.second_throw]
        return sum((1 if roll is not None else 0 for roll in all_rolls))

    def score_without_bonus(self):
        if self.second_throw == SPARE:
            return 10
        return SYMBOL_LOOKUP[self.first_throw] + SYMBOL_LOOKUP[self.second_throw]

    def score(self, next_frame=None, another_frame=None):
        if self.first_throw == STRIKE and next_frame:
            if next_frame and next_frame.first_throw == STRIKE:
                if next_frame.is_last:  # discovered by tests
                    return (
                        10 + next_frame.score_without_bonus() + SYMBOL_LOOKUP[next_frame.extra_one]
                    )
                if another_frame:
                    return 10 + 10 + SYMBOL_LOOKUP[another_frame.first_throw]
            return 10 + next_frame.score_without_bonus()

        if self.second_throw == SPARE and next_frame:
            return 10 + SYMBOL_LOOKUP[next_frame.first_throw]
        return self.score_without_bonus()

    @property
    def closed(self):
        """Regular throws are done, maybe in bonus"""
        if self.first_throw == STRIKE or self.first_throw and self.second_throw:
            return True
        return False


class LastFrame(Frame):

    is_last = True
    extra_one = extra_two = None

    def num_rolls(self):
        all_rolls = [self.first_throw, self.second_throw, self.extra_one, self.extra_two]
        return sum((1 if roll is not None else 0 for roll in all_rolls))

    def score(self, next_frame=None, another_frame=None):
        return (
            self.score_without_bonus()
            + SYMBOL_LOOKUP[self.extra_one]
            + SYMBOL_LOOKUP[self.extra_two]
        )

    def set_bonus(self, pins):
        if self.extra_one is not None:
            self.extra_two = pins
        self.extra_one = pins


class Game(object):
    def __init__(self):
        self._frames = []

    def game_from_line(self, line):
        """A sort of factory"""
        for symbol in line:
            if symbol == " ":
                continue
            self.roll(symbol)

    def in_bonus_balls(self):
        return len(self._frames) == 10 and self._frames[-1].closed

    def roll(self, pins):
        if self.in_bonus_balls():
            self._frames[-1].set_bonus(pins)
        elif not self._frames or self._frames[-1].closed:
            if len(self._frames) == 9:
                self._frames.append(LastFrame(pins))
            else:
                self._frames.append(Frame(pins))
        else:
            self._frames[-1].second_throw = pins

    def total_score(self):
        score = 0
        for index, frame in enumerate(self._frames):
            look_ahead = [None]
            if index < 8:
                look_ahead = [self._frames[index + 1], self._frames[index + 2]]
            elif index == 8:
                look_ahead = [self._frames[index + 1]]

            next_score = frame.score(*look_ahead)
            logger.debug(f"frame {index}: {next_score} ")
            score += next_score
        return score

    def total_rolls(self):
        return sum(frame.num_rolls() for frame in self._frames)
