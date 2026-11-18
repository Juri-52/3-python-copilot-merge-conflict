from inventory import Inventory
from main import show_products
from storage import load_products


def test_show_all_products(capsys):
    inventory = Inventory(load_products())

    show_products(inventory.get_all())

    output = capsys.readouterr().out
    lines = output.splitlines()
    assert len(lines) == 10
    assert lines[0].startswith("1 | ノート |")
    assert lines[-1].startswith("10 | ごみ袋 |")


def test_show_products_reports_no_matches(capsys):
    show_products([])

    assert capsys.readouterr().out == "該当する商品はありません。\n"
