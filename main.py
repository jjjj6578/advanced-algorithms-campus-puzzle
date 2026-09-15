import json
from src.greedy_solver import greedy_schedule
from src.graph_engine import build_conflict_graph, color_graph
from src.optimizer import optimize_room_allocation
from src.backtracker import backtrack_schedule

def main():
    print("==========================================")
    print("   M603 ADVANCED ALGORITHMS: CAMPUS PUZZLE  ")
    print("==========================================")
    
    with open("data/constraints.json", "r") as f:
        data = json.load(f)
        
    print("\n[Stage 1] Running Greedy Baseline...")
    greedy_results = greedy_schedule(data)
    for res in greedy_results:
        print(f"  -> {res['class_id']} scheduled at {res['time']} in {res['room']} ({res['status']})")
        
    print("\n[Stage 2] Running Graph Coloring Engine...")
    graph = build_conflict_graph(data)
    slots = color_graph(graph)
    for cid, slot in slots.items():
        print(f"  -> {cid} assigned to {slot}")
        
    print("\n[Stage 3] Running Room Optimization (DP)...")
    optimized = optimize_room_allocation(data)
    for opt in optimized:
        print(f"  -> {opt['class_id']} optimized to {opt['room_id']} ({opt['status']})")
        
    print("\n[Stage 4] Running Backtracking Best-Effort Strategy...")
    backtracked = backtrack_schedule(data, data['classes'])
    for cid, assignment in backtracked.items():
        print(f"  -> {cid} final status: {assignment}")
        
    print("\n==========================================")
    print("       ALL ALGORITHMS EXECUTED SAFELY     ")
    print("==========================================")

if __name__ == "__main__":
    main()
