from product import Product
from search import search_products


def test_partial_match_preserves_order():
    products = [
        Product(1, "青いペン", "文房具", 120, 2),
        Product(2, "ノート", "文房具", 250, 8),
        Product(3, "赤いペン", "文房具", 120, 1),
    ]

<<<<<<< HEAD
    assert search_products(products, "ペン") == [products[0], products[2]]


def test_keyword_surrounding_spaces():
    product = Product(1, "ノート", "文房具", 250, 8)

    assert search_products([product], " ノート ") == [product]
=======
    found = search_products(products, "ペン")

    assert found == [products[0], products[2]]
    assert len(products) == 3


def test_keyword_surrounding_spaces():
    products = [Product(1, "ノート", "文房具", 250, 8)]

    assert search_products(products, " ノート ") == products
>>>>>>> feature/search


def test_no_matching_name():
    products = [Product(1, "ノート", "文房具", 250, 8)]

    assert search_products(products, "電池") == []


def test_empty_keyword():
    products = [Product(1, "ノート", "文房具", 250, 8)]

    assert search_products(products, "   ") == []
