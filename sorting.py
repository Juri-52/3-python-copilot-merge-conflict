def get_price(product):
    return product.price


def sort_products(products):
    # sortedは新しいリストを返すため、元の一覧の順番を変えない
    return sorted(products, key=get_price)
