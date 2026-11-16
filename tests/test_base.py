from inventory import Inventory
from product import Product
from storage import load_products


def test_product_info():
    product = Product(1, "ノート", "文房具", 250, 8)

    assert product.info() == "1 | ノート | 文房具 | 250円 | 在庫 8個"


def test_load_catalog():
    products = load_products()

    assert len(products) == 10
    assert products[0].name == "ノート"
    assert products[0].price == 250
    assert products[0].stock == 8
    assert products[-1].id == 10


def test_get_all_keeps_catalog_order():
    inventory = Inventory(load_products())
    products = inventory.get_all()

    assert products[0].id == 1
    assert products[-1].id == 10


def test_get_all_returns_separate_list():
    inventory = Inventory(load_products())

    displayed_products = inventory.get_all()
    displayed_products.pop()

    assert len(displayed_products) == 9
    assert len(inventory.get_all()) == 10


def test_empty_inventory():
    inventory = Inventory([])

    assert inventory.get_all() == []
