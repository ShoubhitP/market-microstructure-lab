from engine.order import Order
from engine.order_book import OrderBook


def test_spread_and_midprice():
    book = OrderBook()

    book.add_order(Order(1, "BUY", 100, 99.95, 1))
    book.add_order(Order(2, "SELL", 100, 100.05, 2))

    assert book.best_bid() == 99.95
    assert book.best_ask() == 100.05
    assert round(book.spread(), 10) == 0.10
    assert book.midprice() == 100.00


def test_spread_and_midprice_missing_side():
    book = OrderBook()

    book.add_order(Order(1, "BUY", 100, 99.95, 1))

    assert book.spread() is None
    assert book.midprice() is None