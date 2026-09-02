# Shopping cart kata

Implement `cart.py`. Do not edit `test_cart.py`.

The cart is a mutable `dict`. Start from `{}`. Use only the functions below.

## API

### `add_item(cart, sku, qty, unit_price)`

- `sku` is a non-empty string.
- `qty` is an int. If `qty <= 0`, do nothing.
- `unit_price` is a number of dollars (not cents).
- Each successful call appends one line. Two calls with the same sku are two lines.

### `apply_coupon(cart, code)`

Sets the active coupon to `code` (string). A later call replaces the previous coupon. Only one coupon is active.

Recognized codes (compare case-insensitively):

| Code | Effect |
| --- | --- |
| `SAVE10` | 10% off merchandise subtotal |
| `BOGO` | On each line, the customer pays for `qty - (qty // 2)` items (buy one get one free on that line) |
| `FREESHIP` | Shipping is $0 |

Any other code is stored but has no pricing effect.

### `total(cart)`

Returns a `float` rounded **half up** to two decimal places (cents).

Pricing, in order:

1. Merchandise: for each line, `qty * unit_price`, except under `BOGO` as above.
2. If `SAVE10`, multiply merchandise by `0.90`.
3. Shipping: `$0` if `FREESHIP` or if merchandise **after** step 2 is `>= 50`; otherwise `$5.00`.
4. Tax: `8.25%` of (merchandise after step 2 + shipping).
5. Sum merchandise after step 2 + shipping + tax. Round the **final** sum half up to cents.

An empty cart (no lines) totals `0.00` even if a coupon is set.

## Run tests

```sh
python3 -m unittest test_cart.py -v
```

Do not modify the tests. Put any notes in `RESULT.md` in this directory.
