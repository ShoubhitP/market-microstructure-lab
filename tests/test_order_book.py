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

def cancel_order(self, order_id):
        if order_id not in self.order_map:
            return False

        order = self.order_map[order_id]

        if order.side == "BUY":
            queue = self.bids[order.price]
        else:
            queue = self.asks[order.price]

        queue.remove(order)

        if len(queue) == 0:
            if order.side == "BUY":
                del self.bids[order.price]
            else:
                del self.asks[order.price]

        del self.order_map[order_id]
        return True