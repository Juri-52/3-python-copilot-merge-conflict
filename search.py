def search_products(products, keyword):
    keyword = keyword.strip()
    if keyword == "":
        return []

    found = []
    for product in products:
        if keyword in product.name:
            found.append(product)
    return found
