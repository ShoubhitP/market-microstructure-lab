from engine.matching_engine import MatchingEngine
from engine.order import Order


engine = MatchingEngine()

engine.submit_order(Order(order_id=1, side="SELL", quantity=100, price=52.0, timestamp=1))
engine.submit_order(Order(order_id=2, side="SELL", quantity=100, price=53.0, timestamp=2))

trades = engine.submit_order(Order(order_id=3, side="BUY", quantity=150, price=53.0, timestamp=3))

for trade in trades:
    print(trade)

print("Best ask:", engine.book.best_ask())
print("Best ask order:", engine.book.best_ask_order())