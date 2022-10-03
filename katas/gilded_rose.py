"""Function dispatcher approach"""

from functools import partial
from typing import List, Callable
from enum import Enum


MIN_QUALITY = 0
MAX_QUALITY = 50
SULFURAS_DEFAULT_QUALITY = 80


class Catalog(str, Enum):
    PREFIX = "Conjured"
    BRIE = "Aged Brie"
    PASSES = "Backstage passes to a TAFKAL80ETC concert"
    SULFURAS = "Sulfuras, Hand of Ragnaros"


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in  # I do not like sell in, what about sell_in_day, expiry ...
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)


class NewGildedRose:
    def __init__(self, items: List[Item]):
        self.items = items

    def update_quality(self):
        for item in self.items:
            item.quality = dispatch_updater(item.name)(item)


def cap_quality(quality: int):
    return max(min(MAX_QUALITY, quality), MIN_QUALITY)


def sulfuras_updater(conjured, item):
    """Keeps sell_in and quality equal"""
    return item.quality


def brie_updater(conjured, item):
    """Increase quality over time"""
    item.sell_in -= 1
    multiplier = 2 if conjured else 1

    quality_addition = 1 if item.sell_in > -1 else 2
    return cap_quality(item.quality + multiplier * quality_addition)


def passes_updater(conjured, item):
    """Increase quality until the concert date, then zero"""
    item.sell_in -= 1
    if item.sell_in <= 0:
        return 0

    multiplier = 2 if conjured else 1

    quality_addition = 1
    quality_addition = 2 if 6 < item.sell_in < 11 else quality_addition
    quality_addition = 3 if item.sell_in < 6 else quality_addition
    return cap_quality(item.quality + multiplier * quality_addition)


def dispatch_updater(name) -> Callable:
    conjured = False
    base_name = name
    if name.startswith(Catalog.PREFIX):
        conjured = True
        base_name = name[len(Catalog.PREFIX):]
    updater = {
        Catalog.BRIE: brie_updater,
        Catalog.SULFURAS: sulfuras_updater,
        Catalog.PASSES: passes_updater,
    }[base_name]
    return partial(updater, conjured)  # We already attached the first parameter
