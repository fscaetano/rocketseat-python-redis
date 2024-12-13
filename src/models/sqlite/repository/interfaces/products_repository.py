from abc import ABC, abstractmethod


class ProductsRepositoryInterface(ABC):
    @abstractmethod
    def find_products_by_name(self, product_name: str) -> tuple:
        pass

    @abstractmethod
    def insert_product(self, name: str, price: float, quantity: int) -> None:
        pass

        