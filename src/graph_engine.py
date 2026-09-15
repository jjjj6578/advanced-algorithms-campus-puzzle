import json

def build_conflict_graph(data):
    classes = [c['class_id'] for c in data['classes']]
    graph = {cls: [] for cls in classes}
    
    # Classes share an edge if they are in the same student group conflict
    student_groups = data['student_groups']
    for group, group_classes in student_groups.items():
        for i in range(len(group_classes)):
            for j in range(i + 1, len(group_classes)):
                c1, c2 = group_classes[i], group_classes[j]
                if c2 not in graph[c1]:
                    graph[c1].append(c2)
                if c1 not in graph[c2]:
                    graph[c2].append(c1)
                    
    return graph

def color_graph(graph):
    # Simple Welsh-Powell / Greedy graph coloring for time slots
    coloring = {}
    for node in sorted(graph, key=lambda x: len(graph[x]), reverse=True):
        neighbor_colors = {coloring[neighbor] for neighbor in graph[node] if neighbor in coloring}
        
        # Assign the lowest available time slot color
        color = 1
        while color in neighbor_colors:
            color += 1
        coloring[node] = f"Time_Slot_{color}"
        
    return coloring

if __name__ == "__main__":
    with open("data/constraints.json", "r") as f:
        data = json.load(f)
        
    graph = build_conflict_graph(data)
    time_slots = color_graph(graph)
    
    print("--- STAGE 2: GRAPH COLORING RESULTS ---")
    for class_id, slot in time_slots.items():
        print(f"Class {class_id} assigned to {slot}")
