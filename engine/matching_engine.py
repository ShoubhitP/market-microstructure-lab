from engine.order import Order
from engine.order_book import OrderBook
from engine.trade import Trade


class MatchingEngine:
    def __init__(self):
        self.book = OrderBook()
        self.trades = []

    def submit_order(self, incoming: Order):
        if incoming.side == "BUY":
            return self._match_buy(incoming)
        elif incoming.side == "SELL":
            return self._match_sell(incoming)
        else:
            raise ValueError(f"Invalid order side: {incoming.side}")

    def _match_buy(self, incoming: Order):
        trades = []

        while (
            incoming.quantity > 0
            and self.book.best_ask() is not None
            and self.book.best_ask() <= incoming.price
        ):
            resting_sell = self.book.pop_best_ask_order()

            trade_quantity = min(incoming.quantity, resting_sell.quantity)

            trade = Trade(
                buy_order_id=incoming.order_id,
                sell_order_id=resting_sell.order_id,
                price=resting_sell.price,
                quantity=trade_quantity,
                timestamp=incoming.timestamp,
            )

            trades.append(trade)

            incoming.quantity -= trade_quantity
            resting_sell.quantity -= trade_quantity

            if resting_sell.quantity > 0:
                self.book.add_order(resting_sell)

        if incoming.quantity > 0:
            self.book.add_order(incoming)

        self.trades.extend(trades)
        return trades

    def _match_sell(self, incoming: Order):
        trades = []

        while (
            incoming.quantity > 0
            and self.book.best_bid() is not None
            and self.book.best_bid() >= incoming.price
        ):
            resting_buy = self.book.pop_best_bid_order()

            trade_quantity = min(incoming.quantity, resting_buy.quantity)

            trade = Trade(
                buy_order_id=resting_buy.order_id,
                sell_order_id=incoming.order_id,
                price=resting_buy.price,
                quantity=trade_quantity,
                timestamp=incoming.timestamp,
            )

            trades.append(trade)

            incoming.quantity -= trade_quantity
            resting_buy.quantity -= trade_quantity

            if resting_buy.quantity > 0:
                self.book.add_order(resting_buy)

        if incoming.quantity > 0:
            self.book.add_order(incoming)

        self.trades.extend(trades)
        return trades