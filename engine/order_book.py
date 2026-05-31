from collections import defaultdict, deque

from engine.order import Order


class OrderBook:
    def __init__(self):
        self.bids = defaultdict(deque)
        self.asks = defaultdict(deque)
        self.order_map = {}

    def add_order(self, order: Order):
        if order.side == "BUY":
            self.bids[order.price].append(order)
            self.order_map[order.order_id] = order
        elif order.side == "SELL":
            self.asks[order.price].append(order)
            self.order_map[order.order_id] = order
        else:
            raise ValueError(f"Invalid order side: {order.side}")

    def best_bid(self):
        if not self.bids:
            return None
        return max(self.bids.keys())

    def best_ask(self):
        if not self.asks:
            return None
        return min(self.asks.keys())
    
    def best_bid_order(self):
        price = self.best_bid()
        if price is None:
            return None
        return self.bids[price][0]
    
    def best_ask_order(self):

        price = self.best_ask()
        if price is None: 
            return None
        return self.asks[price][0] 
    
    def pop_best_bid_order(self):
        price = self.best_bid()
        if price is None: 
            return None 
        order = self.bids[price].popleft()
        if len(self.bids[price]) == 0:
            del self.bids[price]
        return order 
    
    def pop_best_ask_order(self):
        price = self.best_ask()
        if price is None:
            return None 
        order = self.asks[price].popleft()
        if len(self.asks[price]) == 0:
            del self.asks[price]
        return order
    
    def spread(self):
        bid = self.best_bid()
        ask = self.best_ask()

        if bid is None or ask is None:
            return None

        return ask - bid

    def midprice(self):
        bid = self.best_bid()
        ask = self.best_ask()

        if bid is None or ask is None:
            return None

        return (bid + ask) / 2
    
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