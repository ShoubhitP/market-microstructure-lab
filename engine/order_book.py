from collections import defaultdict, deque

from engine.order import Order


class OrderBook:
    def __init__(self):
        self.bids = defaultdict(deque)
        self.asks = defaultdict(deque)

    def add_order(self, order: Order):
        if order.side == "BUY":
            self.bids[order.price].append(order)
        elif order.side == "SELL":
            self.asks[order.price].append(order)
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