import unittest

from approvaltests.combination_approvals import verify_all_combinations

from app.gilded_rose import Item, GildedRose


class TestGildedRoseUpdateQuality(unittest.TestCase):
    def update_quality(self, name, sell_in, quality):
        items = [Item(name, sell_in, quality)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        return gilded_rose.items[0]

    def test_updates_quality(self):
        names = ["name", "Aged Brie", "Backstage passes to a TAFKAL80ETC concert", "Sulfuras, Hand of Ragnaros"]
        sell_ins = [-1, 0, 2, 6, 11]
        qualities = [0, 1, 49, 50]
        verify_all_combinations(self.update_quality, [names, sell_ins, qualities])


if __name__ == '__main__':
    unittest.main()
