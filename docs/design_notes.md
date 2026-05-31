# Design Notes

## Purpose

This document explains the design decisions behind the Market Microstructure Lab.

The goal is to build a realistic and extensible exchange simulator, not just a simple coding exercise.

## What Is an Order?

An order is an instruction to buy or sell a financial instrument.

An order should contain:

```text
order_id
side
order_type
price
quantity
timestamp
```

### Side

The side indicates whether the order is a buy or sell.

```text
BUY
SELL
```

### Order Type

The initial system should support:

```text
LIMIT
MARKET
```

A limit order specifies a maximum buy price or minimum sell price.

A market order executes immediately against available liquidity.

## What Is a Trade?

A trade is created when a buy order and sell order match.

A trade should contain:

```text
trade_id
buy_order_id
sell_order_id
price
quantity
timestamp
```

The trade price is usually determined by the resting order, because the incoming order removes liquidity from the book.

## What Is a Price Level?

A price level groups all resting orders at the same price.

Example:

```text
BUY 100 @ 50
BUY 200 @ 50
BUY 150 @ 50
```

These are three different orders at the same price level.

Within a price level, orders should execute in FIFO order.

## Price-Time Priority

Price-time priority means:

1. Better prices execute first.
2. If prices are equal, older orders execute first.

For bids:

```text
Higher price has priority.
```

For asks:

```text
Lower price has priority.
```

At the same price:

```text
Earlier timestamp has priority.
```

## Matching Logic

### Incoming Buy Limit Order

An incoming buy order matches if:

```text
best_ask <= buy_price
```

It should continue matching until:

```text
incoming quantity is zero
```

or

```text
best ask is greater than buy price
```

If quantity remains, the rest becomes a resting bid.

### Incoming Sell Limit Order

An incoming sell order matches if:

```text
best_bid >= sell_price
```

It should continue matching until:

```text
incoming quantity is zero
```

or

```text
best bid is less than sell price
```

If quantity remains, the rest becomes a resting ask.

## Order Book Representation

A simple Python implementation can use:

```text
dict[price] -> queue of orders
```

For bids:

```text
highest price first
```

For asks:

```text
lowest price first
```

Within each price level:

```text
FIFO queue
```

This is not the fastest possible implementation, but it is clean for Phase 1.

Later, the C++ version can use more efficient structures.

## Important Operations

The system should eventually support:

```text
add_order
cancel_order
match_order
best_bid
best_ask
market_depth
```

### Performance Goals

Eventually:

```text
best_bid: O(1) or O(log n)
best_ask: O(1) or O(log n)
add_order: O(log n)
cancel_order: O(1) with order_id map
match_order: depends on number of fills
```

## Why Cancel Orders Are Harder

Cancel orders require fast lookup by order ID.

A realistic design needs:

```text
order_id -> order location
```

This lets the engine remove an order without scanning the entire book.

This should be added after basic matching works.

## Planned Evolution

### Phase 1

Correct Python implementation.

### Phase 2

Better order book visibility.

### Phase 3

Replay historical events.

### Phase 4

Market making agent.

### Phase 5

Inventory-aware strategy.

### Phase 6

Latency modeling.

### Phase 7

C++ implementation.

### Phase 8

Research experiments.

## Design Principle

Correctness first.

Performance second.

Research layer third.

The project should not become a dashboard before the engine is correct.
