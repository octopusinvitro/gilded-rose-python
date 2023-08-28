import unittest

from approvaltests.combination_approvals import verify_all_combinations

from app.gilded_rose import AgedBrie, BackstagePass, Default, Item, GildedRose


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


class TestGildedRoseUpdateBackstagePasses(unittest.TestCase):
    def update_backstage_passes(self, sell_in, quality):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", sell_in, quality)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_backstage_passes(gilded_rose.items[0])
        return gilded_rose.items[0]

    def test_decreases_sell_in_by_one(self):
        item = self.update_backstage_passes(0, 0)
        self.assertEqual(item.sell_in, -1)

    def test_sets_quality_to_zero_for_negative_sell_in(self):
        item = self.update_backstage_passes(-1, 1)
        self.assertEqual(item.quality, 0)

    def test_sets_quality_to_zero_for_zero_sell_in(self):
        item = self.update_backstage_passes(0, 1)
        self.assertEqual(item.quality, 0)

    def test_increases_quality_by_three_for_sell_in_below_first_limit(self):
        item = self.update_backstage_passes(5, 0)
        self.assertEqual(item.quality, 3)

    def test_increases_quality_by_two_for_sell_in_below_second_limit(self):
        item = self.update_backstage_passes(6, 0)
        self.assertEqual(item.quality, 2)

    def test_increases_quality_by_one_for_sell_in_beyond_second_limit(self):
        item = self.update_backstage_passes(11, 0)
        self.assertEqual(item.quality, 1)

    def test_does_not_increase_quality_beyond_limit_if_lower_than_limit(self):
        item = self.update_backstage_passes(6, 49)
        self.assertEqual(item.quality, 50)

    def test_does_not_increase_quality_beyond_limit_if_equal_to_limit(self):
        item = self.update_backstage_passes(11, 50)
        self.assertEqual(item.quality, 50)

    def test_does_not_increase_quality_beyond_limit_if_bigger_than_limit(self):
        item = self.update_backstage_passes(5, 60)
        self.assertEqual(item.quality, 60)


class TestGildedRoseUpdateSulfuras(unittest.TestCase):
    def update_sulfuras(self, sell_in, quality):
        items = [Item("Sulfuras, Hand of Ragnaros", sell_in, quality)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_sulfuras(gilded_rose.items[0])
        return gilded_rose.items[0]

    def test_leaves_item_unchanged(self):
        item = self.update_sulfuras(0, 0)
        self.assertEqual(item.sell_in, 0)
        self.assertEqual(item.quality, 0)


class TestGildedRoseUpdateDefault(unittest.TestCase):
    def update_default(self, sell_in, quality):
        items = [Item("name", sell_in, quality)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_default(gilded_rose.items[0])
        return gilded_rose.items[0]

    def test_decreases_sell_in_by_one(self):
        item = self.update_default(0, 0)
        self.assertEqual(item.sell_in, -1)

    def test_sets_quality_to_zero_for_zero_quality(self):
        item = self.update_default(-1, 0)
        self.assertEqual(item.quality, 0)

    def test_sets_quality_to_zero_for_quality_equal_to_one(self):
        item = self.update_default(0, 1)
        self.assertEqual(item.quality, 0)

    def test_decreases_quality_by_two_for_quality_bigger_than_one_and_negative_sell_in(self):
        item = self.update_default(-1, 4)
        self.assertEqual(item.quality, 2)

    def test_decreases_quality_by_two_for_quality_bigger_than_one_and_zero_sell_in(self):
        item = self.update_default(0, 4)
        self.assertEqual(item.quality, 2)

    def test_decreases_quality_by_two_for_quality_bigger_than_one_and_positive_sell_in(self):
        item = self.update_default(1, 3)
        self.assertEqual(item.quality, 2)


class TestItemCreate(unittest.TestCase):
    def test_creates_an_aged_brie(self):
        item = Item.create("Aged Brie", 0, 0)
        self.assertIsInstance(item, AgedBrie)

    def test_creates_a_backstage_pass(self):
        item = Item.create("Backstage passes to a TAFKAL80ETC concert", 0, 0)
        self.assertIsInstance(item, BackstagePass)

    def test_creates_a_sulfuras(self):
        item = Item.create("Sulfuras, Hand of Ragnaros", 0, 0)
        self.assertIsInstance(item, Item)

    def test_creates_a_default(self):
        item = Item.create("irrelevant", 0, 0)
        self.assertIsInstance(item, Default)


if __name__ == '__main__':
    unittest.main()
