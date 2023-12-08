from unittest.mock import MagicMock

import pytest


class ProductionClass:
    def m1(self):
        print("m1")

    def m2(self):
        print("m2")


@pytest.fixture()
def prod_class():
    pc = ProductionClass()
    pc.m1 = MagicMock(return_value="123")
    pc.m2 = MagicMock(return_value="321")
    return pc


def test_pc(prod_class):
    assert prod_class.m1() == "123"
    assert prod_class.m2() == "321"
