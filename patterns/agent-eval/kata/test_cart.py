import unittest

from cart import add_item, apply_coupon, total


class CartTests(unittest.TestCase):
    def test_empty_cart_is_zero(self):
        self.assertEqual(total({}), 0.0)

    def test_empty_cart_with_coupon_is_zero(self):
        cart = {}
        apply_coupon(cart, "SAVE10")
        self.assertEqual(total(cart), 0.0)

    def test_qty_zero_is_noop(self):
        cart = {}
        add_item(cart, "A", 0, 10.0)
        add_item(cart, "A", -1, 10.0)
        self.assertEqual(total(cart), 0.0)

    def test_single_item_below_shipping_threshold(self):
        cart = {}
        add_item(cart, "A", 1, 10.0)
        # merch 10, ship 5, tax 8.25% of 15 = 1.2375 -> final 16.2375 -> 16.24
        self.assertEqual(total(cart), 16.24)

    def test_single_item_at_shipping_threshold(self):
        cart = {}
        add_item(cart, "A", 1, 50.0)
        # merch 50, ship 0, tax 8.25% of 50 = 4.125 -> 54.125 -> 54.13
        self.assertEqual(total(cart), 54.13)

    def test_save10_reduces_merchandise(self):
        cart = {}
        add_item(cart, "A", 1, 20.0)
        apply_coupon(cart, "SAVE10")
        # merch 18, ship 5, tax 8.25% of 23 = 1.8975 -> 24.8975 -> 24.90
        self.assertEqual(total(cart), 24.90)

    def test_save10_is_case_insensitive(self):
        cart = {}
        add_item(cart, "A", 1, 20.0)
        apply_coupon(cart, "save10")
        self.assertEqual(total(cart), 24.90)

    def test_bogo_two_items(self):
        cart = {}
        add_item(cart, "A", 2, 10.0)
        apply_coupon(cart, "BOGO")
        # pay 1 * 10 = 10, ship 5, tax 8.25% of 15 -> 16.24
        self.assertEqual(total(cart), 16.24)

    def test_bogo_three_items(self):
        cart = {}
        add_item(cart, "A", 3, 10.0)
        apply_coupon(cart, "BOGO")
        # pay 2 * 10 = 20, ship 5, tax 8.25% of 25 = 2.0625 -> 27.0625 -> 27.06
        self.assertEqual(total(cart), 27.06)

    def test_freeship(self):
        cart = {}
        add_item(cart, "A", 1, 10.0)
        apply_coupon(cart, "FREESHIP")
        # merch 10, ship 0, tax 8.25% of 10 = 0.825 -> 10.825 -> 10.83
        self.assertEqual(total(cart), 10.83)

    def test_unknown_coupon_has_no_effect(self):
        cart = {}
        add_item(cart, "A", 1, 10.0)
        apply_coupon(cart, "NOTREAL")
        self.assertEqual(total(cart), 16.24)

    def test_later_coupon_replaces_earlier(self):
        cart = {}
        add_item(cart, "A", 1, 10.0)
        apply_coupon(cart, "SAVE10")
        apply_coupon(cart, "FREESHIP")
        self.assertEqual(total(cart), 10.83)

    def test_two_lines_accumulate(self):
        cart = {}
        add_item(cart, "A", 1, 10.0)
        add_item(cart, "B", 1, 10.0)
        # merch 20, ship 5, tax 8.25% of 25 = 2.0625 -> 27.06
        self.assertEqual(total(cart), 27.06)


if __name__ == "__main__":
    unittest.main()
