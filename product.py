from dataclasses import dataclass


@dataclass
class Product:
    id: int
    name: str
    category: str
    price: int
    stock: int

    def info(self):
        return (
            f"{self.id} | {self.name} | {self.category} | "
            f"{self.price}円 | 在庫 {self.stock}個"
        )
