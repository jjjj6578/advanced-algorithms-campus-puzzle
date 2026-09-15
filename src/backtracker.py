import json

def backtrack_schedule(data, classes_to_schedule, index=0, current_schedule=None):
    """
    Stage 4: Backtracking / Best-Effort Engine.
    Recursively attempts to find a valid schedule; if constraints are 
    too tight, it flags unscheduled classes gracefully.
    """
    if current_schedule is None:
        current_schedule = {}
        
    if index == len(classes_to_schedule):
        return current_schedule # Success: all scheduled
        
    cls = classes_to_schedule[index]
    
    for room in data['rooms']:
        if room['capacity'] >= cls['enrolled_students']:
            # Try assigning room
            current_schedule[cls['class_id']] = room['room_id']
            
            # Recurse to next class
            result = backtrack_schedule(data, classes_to_schedule, index + 1, current_schedule)
            if result:
                return result
                
            # Backtrack if it fails down the line
            del current_schedule[cls['class_id']]
            
    # If no room fits or conflict blocks it, mark as unscheduled (Best Effort Strategy)
    current_schedule[cls['class_id']] = "Unscheduled / Conflict"
    return backtrack_schedule(data, classes_to_schedule, index + 1, current_schedule)

if __name__ == "__main__":
    with open("data/constraints.json", "r") as f:
        data = json.load(f)
        
    results = backtrack_schedule(data, data['classes'])
    print("--- STAGE 4: BACKTRACKING BEST-EFFORT RESULTS ---")
    for cid, assignment in results.items():
        print(f"Class {cid} -> {assignment}")
