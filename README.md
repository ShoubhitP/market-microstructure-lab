# Market Microstructure Lab

A high-performance exchange simulator and market making research platform for studying market microstructure, order book dynamics, and automated market making strategies.

## Overview

Market Microstructure Lab is designed to answer a core question:

> How do markets actually function at the order book level?

The project will simulate an exchange with price-time priority matching, order book state, historical replay, market making agents, inventory risk controls, latency modeling, and research dashboards.

This project complements derivatives/volatility work by covering the other major side of quantitative trading:

- Derivatives pricing
- Market microstructure
- Execution systems
- Market making
- Latency and systems performance

## Core Goals

The goal is not to build a toy order book. The goal is to build a research-grade platform with clear engineering and quantitative depth.

The system should support:

- Limit orders
- Market orders
- Cancel orders
- Price-time priority matching
- Full order book depth
- Historical market replay
- Market making agents
- Inventory-aware quoting
- Latency simulation
- PnL and risk analytics
- Performance benchmarking
- Eventually, a C++ matching core exposed to Python

## Architecture

Planned major components:

```text
engine/
  order.py
  trade.py
  order_book.py
  matching_engine.py

research/
  market_maker.py
  inventory_model.py
  pnl.py
  experiments.py

replay/
  event.py
  replay_engine.py

api/
  main.py

frontend/
  React dashboard later

tests/
  unit and integration tests

docs/
  design notes and phase roadmap
```

## Project Roadmap

### Phase 1 — Core Matching Engine

Build a correct exchange core.

Features:

- Order representation
- Trade representation
- Limit order matching
- Market order matching
- Partial fills
- Full fills
- Price-time priority
- Unit tests

### Phase 2 — Full Order Book

Add order book visibility.

Features:

- Best bid
- Best ask
- Spread
- Midprice
- Market depth
- Bid/ask levels

### Phase 3 — Historical Replay Engine

Replay timestamped market events.

Features:

- Event model
- Deterministic replay
- Time-based simulation
- Order book snapshots

### Phase 4 — Market Making Agent

Build a naive market maker.

Features:

- Quote bid/ask around midprice
- Track fills
- Track cash
- Track inventory
- Track PnL

### Phase 5 — Inventory Risk Controls

Build an inventory-aware market maker.

Features:

- Quote skewing
- Inventory limits
- Risk-adjusted quoting
- Naive vs inventory-aware comparison

### Phase 6 — Latency Simulation

Model delay and adverse selection.

Features:

- Order delay
- Processing delay
- Market data delay
- PnL vs latency study

### Phase 7 — C++ Core

Move performance-critical components to C++17.

Features:

- C++ matching engine
- C++ order book
- pybind11 bindings
- Python vs C++ benchmark

### Phase 8 — Research Layer

Turn the simulator into a research platform.

Studies:

- Spread width vs PnL
- Inventory limits vs risk
- Latency vs profitability
- Volatility vs fill rate
- Fill probability vs quote distance

## Final Goal

The final system should demonstrate both systems engineering and quantitative research ability:

> A high-performance exchange simulator supporting price-time priority matching, market making agents, inventory risk controls, latency modeling, and microstructure research.
