from typing import List

from .gilded_rose import Item, dispatch_updater


class ItemProxy:
    def __init__(self, item: Item):
        self.original_item = item

    @property
    def name(self):
        return self.original_item.name

    @property
    def sell_in(self):
        return self.original_item.sell_in

    @sell_in.setter
    def sell_in(self, value):
        self.original_item.sell_in = value

    @property
    def quality(self):
        return self.original_item.quality

    @quality.setter
    def quality(self, value):
        self.original_item.quality = value

    def update_quality(self):
        updater = dispatch_updater(self.name)
        self.quality = updater(self.original_item)

    def __repr__(self):
        return self.original_item.__repr__()


class ProxyGildedRose:
    def __init__(self, items: List[Item]):
        self.proxies = [ItemProxy(item) for item in items]

    @property
    def items(self):
        return [proxy.original_item for proxy in self.proxies]

    def update_quality(self):
        for item in self.proxies:
            item.update_quality()
