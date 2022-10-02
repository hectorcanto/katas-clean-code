from typing import List

from .gilded_rose import Item, dispatch_updater


class ItemProxy:
    def __init__(self, item: Item):
        self._item = item

    @property
    def name(self):
        return self._item.name

    @property
    def sell_in(self):
        return self._item.sell_in

    @sell_in.setter
    def sell_in(self, value):
        self._item.sell_in = value

    @property
    def quality(self):
        return self._item.quality

    @quality.setter
    def quality(self, value):
        self._item.quality = value

    def update_quality(self):
        updater = dispatch_updater(self.name)
        self.quality = updater(self._item)

    def __repr__(self):
        return self._item.__repr__()


class ProxyGildedRose:
    def __init__(self, items: List[Item]):
        self._proxy = [ItemProxy(item) for item in items]

    @property
    def items(self):
        return [proxy._item for proxy in self._proxies]

    def update_quality(self):
        for item in self.items:
            item.update_quality()
