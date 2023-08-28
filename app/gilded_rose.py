class GildedRose(object):
    def __init__(self, items):
        self.items = items

    def update_brie(self, item):
        item.sell_in = item.sell_in - 1
        if item.quality > 50:
            return

        self.increase_quality(item)
        if item.sell_in < 0:
            self.increase_quality(item)

    def update_backstage_passes(self, item):
        item.sell_in = item.sell_in - 1
        if item.sell_in < 0:
            item.quality = 0
            return

        self.increase_quality(item)

        if item.sell_in < 10:
            self.increase_quality(item)

        if item.sell_in < 5:
            self.increase_quality(item)

    def update_sulfuras(self, item):
        return

    def update_default(self, item):
        item.sell_in = item.sell_in - 1
        item.quality = item.quality - 1

        if item.quality < 1:
            item.quality = 0
            return

        if item.sell_in < 0:
            item.quality = item.quality - 1

    def increase_quality(self, item):
        if item.quality < 50:
            item.quality = item.quality + 1

    def update_quality(self):
        for item in self.items:
            if item.name == "Aged Brie":
                return self.update_brie(item)

            if item.name == "Backstage passes to a TAFKAL80ETC concert":
                return self.update_backstage_passes(item)

            if item.name == "Sulfuras, Hand of Ragnaros":
                return self.update_sulfuras(item)

            return self.update_default(item)


class Item:
    @classmethod
    def create(cls, name, sell_in, quality):
        if name == "Aged Brie":
            return AgedBrie(sell_in, quality)

        if name == "Backstage passes to a TAFKAL80ETC concert":
            return BackstagePass(sell_in, quality)

        if name == "Sulfuras, Hand of Ragnaros":
            return Item(name, sell_in, quality)

        return Default(name, sell_in, quality)

    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)


class AgedBrie(Item):
    def __init__(self, sell_in, quality):
        super().__init__("Aged Brie", sell_in, quality)


class BackstagePass(Item):
    def __init__(self, sell_in, quality):
        super().__init__("Backstage passes to a TAFKAL80ETC concert", sell_in, quality)


class Default(Item):
    def __init__(self, name, sell_in, quality):
        super().__init__(name, sell_in, quality)
