import pytest
from katas.gilded_rose import (
    NewGildedRose,
    Item,
    dispatch_updater,
    Catalog,
    SULFURAS_DEFAULT_QUALITY,
)
from katas.gilded_rose_legacy import Item as LegacyItem, GildedRose as LegacyGildedRose
from katas.gilded_rose_proxy import ProxyGildedRose


def test_brie():
    item = Item(Catalog.BRIE, 2, 25)
    updater = dispatch_updater(item.name)
    updater(item)
    assert item.sell_in == 1
    assert item.quality == 26

    updater(item, 2)
    assert item.sell_in == -1
    assert item.quality == 29


def test_old_brie():

    item = Item(Catalog.BRIE, 2, 55)
    updater = dispatch_updater(item.name)
    updater(item)
    assert item.quality == 50
    assert item.sell_in == 1


def test_conjured_brie():
    item = Item(Catalog.PREFIX + Catalog.BRIE, 2, 25)
    updater = dispatch_updater(item.name)
    updater(item)
    assert item.quality == 27
    assert item.sell_in == 1
    updater(item, 2)
    assert item.quality == 33
    assert item.sell_in == -1


def test_passes():
    item = Item(Catalog.PASSES, 7, 25)
    updater = dispatch_updater(item.name)
    updater(item)
    assert item.sell_in == 6
    assert item.quality == 27

    updater(item, 4)
    assert item.sell_in == 2
    assert item.quality == 39


def build_items(days, quality):
    return [
        LegacyItem(Catalog.SULFURAS, days, SULFURAS_DEFAULT_QUALITY),
        LegacyItem(Catalog.BRIE, days, quality),
        LegacyItem(Catalog.PASSES, days, quality),
    ]


def compare_two_items(one, two):
    assert one.sell_in == two.sell_in, (one, two)
    assert one.quality == two.quality, (one, two)
    return True


def run_base_try(days, quality, new_shop_class):
    items = build_items(days, quality)
    same_items = build_items(days, quality)

    legacy = LegacyGildedRose(items)
    legacy.update_quality()

    new = new_shop_class(same_items)
    new.update_quality()

    return legacy, new


@pytest.mark.parametrize("new_shop_class", (NewGildedRose, ProxyGildedRose))
def test_gilded_rose_10_days(new_shop_class):

    legacy_shop, new_shop = run_base_try(10, 25, new_shop_class)
    for index in range(3):
        assert compare_two_items(new_shop.items[index], legacy_shop.items[index])


@pytest.mark.parametrize("new_shop_class", (NewGildedRose, ProxyGildedRose))
def test_gilded_rose_with_legacy(new_shop_class):
    legacy_shop, new_shop = run_base_try(-5, 25, new_shop_class)
    for index in range(3):
        assert compare_two_items(new_shop.items[index], legacy_shop.items[index])


@pytest.mark.parametrize("new_shop_class", (NewGildedRose, ProxyGildedRose))
def test_high_quality(new_shop_class):
    legacy_shop, new_shop = run_base_try(2, 50, new_shop_class)
    for index in range(3):
        assert compare_two_items(new_shop.items[index], legacy_shop.items[index])


@pytest.mark.parametrize("new_shop_class", (NewGildedRose, ProxyGildedRose))
def test_low_quality(new_shop_class):
    legacy_shop, new_shop = run_base_try(2, 0, new_shop_class)
    for index in range(3):
        assert compare_two_items(new_shop.items[index], legacy_shop.items[index])
