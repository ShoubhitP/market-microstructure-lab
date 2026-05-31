from engine.order import Order
from engine.order_book import OrderBook


book = OrderBook()

book.add_order(Order(order_id=1, side="BUY", quantity=100, price=50.0, timestamp=1))
book.add_order(Order(order_id=2, side="BUY", quantity=100, price=50.0, timestamp=2))

print(book.bids[50.0][0])
print(book.bids[50.0][1])