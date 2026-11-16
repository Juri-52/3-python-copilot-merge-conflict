import json

from product import Product


def load_products(filename="data/products.json"):
    # JSONの辞書をProductのインスタンスに変える
    with open(filename, encoding="utf-8") as file:
        rows = json.load(file)

    products = []
    for row in rows:
        product = Product(
            row["id"],
            row["name"],
            row["category"],
            row["price"],
            row["stock"],
        )
        products.append(product)
    return products
