from engine.matching_engine import MatchingEngine
from engine.order import Order


def test_buy_crosses_sell():
    engine = MatchingEngine()

    engine.submit_order(
        Order(
            order_id=1,
            side="SELL",
            quantity=100,
            price=50.0,
            timestamp=1,
        )
    )

    trades = engine.submit_order(
        Order(
            order_id=2,
            side="BUY",
            quantity=100,
            price=50.0,
            timestamp=2,
        )
    )

    assert len(trades) == 1

    trade = trades[0]

    assert trade.price == 50.0
    assert trade.quantity == 100

    assert engine.book.best_ask() is None

def test_partial_fill():
    engine = MatchingEngine()

    engine.submit_order(
        Order(1, "SELL", 100, 50.0, 1)
    )

    trades = engine.submit_order(
        Order(2, "BUY", 50, 50.0, 2)
    )

    assert len(trades) == 1
    assert trades[0].quantity == 50

    assert engine.book.best_ask() == 50.0
    assert engine.book.best_ask_order().quantity == 50

def test_fifo_priority():
    engine = MatchingEngine()

    engine.submit_order(
        Order(1, "SELL", 100, 50.0, 1)
    )

    engine.submit_order(
        Order(2, "SELL", 100, 50.0, 2)
    )

    trades = engine.submit_order(
        Order(3, "BUY", 100, 50.0, 3)
    )

    assert trades[0].sell_order_id == 1

def test_price_priority():
    engine = MatchingEngine()

    engine.submit_order(
        Order(1, "SELL", 100, 51.0, 1)
    )

    engine.submit_order(
        Order(2, "SELL", 100, 50.0, 2)
    )

    trades = engine.submit_order(
        Order(3, "BUY", 100, 55.0, 3)
    )

    assert trades[0].sell_order_id == 2
    assert trades[0].price == 50.0