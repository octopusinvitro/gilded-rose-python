from enum import Enum


class ItemTypes(Enum):
    AGED_BRIE = "Aged Brie"
    BACKSTAGE_PASS = "Backstage passes to a TAFKAL80ETC concert"
    SULFURAS = "Sulfuras, Hand of Ragnaros"


class GildedRose(object):
    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:
            item.update_quality()


class Item:
    @classmethod
    def create(cls, name, sell_in, quality):
        klass = {
            ItemTypes.AGED_BRIE.value: AgedBrie,
            ItemTypes.BACKSTAGE_PASS.value: BackstagePass,
            ItemTypes.SULFURAS.value: Item
        }.get(name, Default)

        return klass(name, sell_in, quality)

    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def update_quality(self):
        return

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)


class AgedBrie(Item):
    def update_quality(self):
        self.sell_in = self.sell_in - 1
        if self.quality > 50:
            return

        self._increase_quality()
        if self.sell_in < 0:
            self._increase_quality()

    def _increase_quality(self):
        if self.quality < 50:
            self.quality = self.quality + 1


class BackstagePass(Item):
    def update_quality(self):
        self.sell_in = self.sell_in - 1
        if self.sell_in < 0:
            self.quality = 0
            return

        self._increase_quality()

        if self.sell_in < 10:
            self._increase_quality()

        if self.sell_in < 5:
            self._increase_quality()

    def _increase_quality(self):
        if self.quality < 50:
            self.quality = self.quality + 1


class Default(Item):
    def update_quality(self):
        self.sell_in = self.sell_in - 1
        self.quality = self.quality - 1

        if self.quality < 1:
            self.quality = 0
            return

        if self.sell_in < 0:
            self.quality = self.quality - 1
