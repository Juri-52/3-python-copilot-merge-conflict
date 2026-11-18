from product import Product
from sorting import sort_products


def test_price_order_keeps_original_list():
    expensive = Product(1, "ノート", "文房具", 250, 8)
    cheap = Product(2, "消しゴム", "文房具", 80, 1)
    products = [expensive, cheap]

    assert sort_products(products) == [cheap, expensive]
    assert products == [expensive, cheap]


def test_same_price_keeps_original_order():
    first = Product(1, "クリアファイル", "文房具", 100, 3)
    second = Product(2, "ミネラルウォーター", "飲料", 100, 0)

    assert sort_products([first, second]) == [first, second]


def test_empty_products():
    assert sort_products([]) == []
