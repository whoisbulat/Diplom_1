from unittest.mock import Mock
import pytest
from bun import Bun



class TestBun:
    @pytest.mark.parametrize('name', ["",None])
    def test_init_bun_name(self, name):
        mock_bun = Mock()
        mock_bun.price = 1.5
        bun = Bun(name, mock_bun.price)
        assert bun.get_name() == name

    @pytest.mark.parametrize('price', [1.5, None])
    def test_init_bun_price(self, price):
        mock_bun = Mock()
        mock_bun.name = 'Mock Bun'
        bun = Bun(mock_bun.name, price)
        assert bun.get_price() == price

    @pytest.mark.parametrize("name, price", [("name", 224), ("Имя", 213.13)])
    def test_get_name(self, name, price):
        bun = Bun(name, price)
        assert bun.get_name() == name

    @pytest.mark.parametrize("name, price", [("name", 224), ("Имя", 213.13)])
    def test_get_price(self, name, price):
        bun = Bun(name, price)
        assert bun.get_price() == price






