import json

def build_conflict_graph(data):
    # Extract all class IDs
    classes_list = data['classes']
    class_ids = [c['class_id'] for c in classes_list]
    graph = {cls: [] for cls in class_ids}
    
    # 1. Conflict from student groups
    student_groups = data.get('student_groups', {})
    for group, group_classes in student_groups.items():
        for i in range(len(group_classes)):
            for j in range(i + 1, len(group_classes)):
                c1, c2 = group_classes[i], group_classes[j]
                if c1 in graph and c2 in graph:
                    if c2 not in graph[c1]:
                        graph[c1].append(c2)
                    if c1 not in graph[c2]:
                        graph[c2].append(c1)
                        
    # 2. Conflict from shared professor
    for i in range(len(classes_list)):
        for j in range(i + 1, len(classes_list)):
            c1_data = classes_list[i]
            c2_data = classes_list[j]
            
            id1 = c1_data['class_id']
            id2 = c2_data['class_id']
            
            prof1 = c1_data.get('professor_id')
            prof2 = c2_data.get('professor_id')
            
            if prof1 and prof2 and prof1 == prof2:
                if id2 not in graph[id1]:
                    graph[id1].append(id2)
                if id1 not in graph[id2]:
                    graph[id2].append(id1)
                    
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
        coloring[node] = color
        
    return coloring
