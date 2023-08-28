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


class TestGildedRoseUpdateBrie(unittest.TestCase):
    def update_brie(self, sell_in, quality):
        items = [Item("Aged Brie", sell_in, quality)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_brie(gilded_rose.items[0])
        return gilded_rose.items[0]

    def test_decreases_sell_in_by_one(self):
        item = self.update_brie(0, 0)
        self.assertEqual(item.sell_in, -1)

    def test_increases_quality_by_two_for_negative_sell_in(self):
        item = self.update_brie(-1, 0)
        self.assertEqual(item.quality, 2)

    def test_increases_quality_by_two_for_zero_sell_in(self):
        item = self.update_brie(0, 0)
        self.assertEqual(item.quality, 2)

    def test_increases_quality_by_one_for_positive_sell_in(self):
        item = self.update_brie(1, 0)
        self.assertEqual(item.quality, 1)

    def test_does_not_increase_quality_beyond_limit_if_lower_than_limit(self):
        item = self.update_brie(0, 49)
        self.assertEqual(item.quality, 50)

    def test_does_not_increase_quality_beyond_limit_if_equal_to_limit(self):
        item = self.update_brie(1, 50)
        self.assertEqual(item.quality, 50)

    def test_does_not_increase_quality_beyond_limit_if_bigger_than_limit(self):
        item = self.update_brie(1, 60)
        self.assertEqual(item.quality, 60)


if __name__ == '__main__':
    unittest.main()
