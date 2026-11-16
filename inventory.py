class Inventory:
    def __init__(self, products):
        self.products = products

    def get_all(self):
        # 呼び出し側が一覧を並べ替えても元の順番を残す
        return self.products.copy()
