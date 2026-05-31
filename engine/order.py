from dataclasses import dataclass

@dataclass
class Order: 
    order_id: int
    side: str
    quantity: int
    price: float
    timestamp: int