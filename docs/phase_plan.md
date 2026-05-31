# Phase Plan

## Phase 1 — Core Matching Engine

### Goal

Build the foundation of the exchange simulator.

The matching engine should accept incoming orders, match them against resting liquidity, generate trades, and leave unfilled limit order quantity resting on the book.

### Features

- Limit orders
- Market orders
- Buy and sell sides
- Price-time priority
- Partial fills
- Full fills
- Trade generation

### Core Classes

```text
Order
Trade
OrderBook
MatchingEngine
```

### Correctness Requirements

The engine must pass tests for:

- Buy order crossing resting sell order
- Sell order crossing resting buy order
- Partial fill
- Full fill
- Better price priority
- FIFO priority at same price
- Non-crossing orders resting on the book
- Market orders consuming available liquidity

### Commit Point

```bash
git add .
git commit -m "Implement core matching engine"
```

---

## Phase 2 — Full Order Book

### Goal

Expose useful market state.

### Features

- Best bid
- Best ask
- Spread
- Midprice
- Bid depth
- Ask depth
- Total resting liquidity

### Deliverable

A simple script that prints order book state after each order.

### Commit Point

```bash
git add .
git commit -m "Add order book state and market depth"
```

---

## Phase 3 — Historical Replay Engine

### Goal

Replay market events through time.

### Features

- Event objects
- Timestamped order stream
- Replay loop
- Deterministic simulation
- Book snapshots

### Deliverable

A replay script that processes a CSV of market events and reconstructs book state over time.

### Commit Point

```bash
git add .
git commit -m "Add historical market replay engine"
```

---

## Phase 4 — Market Making Agent

### Goal

Build a simple market maker that quotes around the midprice.

### Features

- Bid quote
- Ask quote
- Quote width parameter
- Fill tracking
- Inventory tracking
- Cash tracking
- Mark-to-market PnL

### Deliverable

Run a simulation and output:

- PnL
- Inventory
- Number of fills
- Fill rate
- Spread captured

### Commit Point

```bash
git add .
git commit -m "Add naive market making agent"
```

---

## Phase 5 — Inventory Risk Controls

### Goal

Make the market maker inventory-aware.

### Problem

A naive market maker can accumulate large long or short inventory. This creates directional risk.

### Features

- Inventory limit
- Quote skewing
- Reduced bid aggressiveness when long
- Reduced ask aggressiveness when short
- Naive vs inventory-aware comparison

### Deliverable

Research report comparing:

- PnL
- Inventory volatility
- Max inventory
- Drawdown

### Commit Point

```bash
git add .
git commit -m "Add inventory-aware market making strategy"
```

---

## Phase 6 — Latency Simulation

### Goal

Study how latency affects profitability.

### Features

- Order submission delay
- Market data delay
- Exchange processing delay
- Configurable latency levels

### Research Questions

- How does PnL change as latency increases?
- How does fill quality change?
- When does adverse selection dominate spread capture?

### Commit Point

```bash
git add .
git commit -m "Add latency simulation experiments"
```

---

## Phase 7 — C++ Matching Core

### Goal

Move the performance-critical engine into C++.

### Features

- C++17 order book
- C++17 matching engine
- Python bindings with pybind11
- Benchmark against Python implementation

### Metrics

- Events per second
- Average matching latency
- Memory usage

### Commit Point

```bash
git add .
git commit -m "Add C++ matching engine prototype"
```

---

## Phase 8 — Research Layer

### Goal

Turn the project into a microstructure research platform.

### Studies

- Spread width vs PnL
- Inventory limit vs risk
- Latency vs profitability
- Volatility vs fill rate
- Quote distance vs fill probability

### Final Deliverables

- Plots
- Tables
- Research writeups
- Dashboard
- Benchmarks
- README with clear results

### Commit Point

```bash
git add .
git commit -m "Add microstructure research experiments"
```
