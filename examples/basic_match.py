from engine.order import Order
from engine.trade import Trade


buy_order = Order(
    order_id=1,
    side="BUY",
    quantity=100,
    price=50.0,
    timestamp=1,
)

sell_order = Order(
    order_id=2,
    side="SELL",
    quantity=100,
    price=49.0,
    timestamp=2,
)

trade = Trade(
    buy_order_id=buy_order.order_id,
    sell_order_id=sell_order.order_id,
    price=50.0,
    quantity=100,
    timestamp=2,
)

print(buy_order)
print(sell_order)
print(trade)