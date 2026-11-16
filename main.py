from inventory import Inventory
from storage import load_products


def show_products(products):
    if not products:
        print("該当する商品はありません。")
        return

    for product in products:
        print(product.info())


def main():
    inventory = Inventory(load_products())

    while True:
        print("\n商品管理")
        print("1: 商品一覧")
        print("0: 終了")
        choice = input("選択: ").strip()

        if choice == "1":
            show_products(inventory.get_all())
        elif choice == "0":
            print("終了します。")
            break
        else:
            print("メニューの番号を入力してください。")


if __name__ == "__main__":
    main()
