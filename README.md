# The Campus Puzzle: Advanced Algorithm Scheduling Engine

This repository contains the solution for "The Campus Puzzle" assignment, implementing a robust 4-stage algorithmic pipeline for automated university class scheduling, room allocation, and conflict resolution under strict constraints.

## Project Structure

├── data/
│   └── constraints.json       # Mock dataset containing class sizes, room capacities, and student group conflicts
├── src/
│   ├── greedy_solver.py       # Stage 1: Greedy Baseline algorithm for initial assignment
│   ├── graph_engine.py        # Stage 2: Graph Coloring & Conflict Resolution engine
│   ├── optimizer.py           # Stage 3: Dynamic Programming Room Optimization
│   └── backtracker.py         # Stage 4: Best-effort Backtracking fallback for tight constraints
├── main.py                    # Main execution script running the full sequential pipeline
└── README.md                  # Project documentation


## Algorithmic Stages Overview
1. **Stage 1 (Greedy Baseline):** Sorts classes in descending order by enrollment size and maps them to the first available room meeting capacity constraints.
2. **Stage 2 (Graph Coloring):** Builds an adjacency matrix representing student group clashes and dynamically assigns non-conflicting time slots.
3. **Stage 3 (Dynamic Programming Optimizer):** Minimizes total wasted room capacity across valid allocations to maximize space efficiency.
4. **Stage 4 (Backtracking Fallback):** Recursively explores solution spaces under tight constraints, preventing hard system failures by gracefully flagging unallocatable classes.

## Getting Started & Execution
Ensure you have Python 3 installed. Run the primary execution orchestrator script from the root directory:

```bash
python main.py
