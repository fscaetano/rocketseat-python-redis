import pytest
from src.models.sqlite.settings.connection import SqliteConnectionHandler
from .products_repository import ProductsRepository

conn_handler = SqliteConnectionHandler()
conn = conn_handler.connect()


@pytest.mark.skip(reason="db interation")
def test_insert_product():
    repo = ProductsRepository(conn)

    name = "something"
    price = 12.34
    quantity = 8

    repo.insert_product(name, price, quantity)


@pytest.mark.skip(reason="db interation")
def test_find_product():
    repo = ProductsRepository(conn)

    name = "something"

    response = repo.find_products_by_name(name)
    print()
    print(response)
    print(type(response))
