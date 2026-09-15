import json

def optimize_room_allocation(data):
    classes = sorted(data['classes'], key=lambda x: x['enrolled_students'])
    rooms = sorted(data['rooms'], key=lambda x: x['capacity'])
    
    allocation = []
    for cls in classes:
        best_room = None
        min_waste = float('inf')
        
        for room in rooms:
            waste = room['capacity'] - cls['enrolled_students']
            if 0 <= waste < min_waste:
                min_waste = waste
                best_room = room
                
        if best_room:
            allocation.append({
                "class_id": cls['class_id'],
                "room_id": best_room['room_id'],
                "wasted_seats": min_waste,
                "status": "Perfect Fit" if min_waste == 0 else f"Wasted {min_waste} seats"
            })
            
    return allocation
