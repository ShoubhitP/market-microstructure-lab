from engine.order import Order
from engine.order_book import OrderBook


book = OrderBook()

book.add_order(Order(order_id=1, side="BUY", quantity=100, price=50.0, timestamp=1))
book.add_order(Order(order_id=2, side="BUY", quantity=100, price=50.0, timestamp=2))
book.add_order(Order(order_id=3, side="BUY", quantity=100, price=49.0, timestamp=3))

print("Best bid order:", book.best_bid_order())

removed = book.pop_best_bid_order()
print("Removed:", removed)

print("New best bid order:", book.best_bid_order())