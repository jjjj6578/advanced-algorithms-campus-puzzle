import json

def greedy_schedule(data):
    # Sort classes by number of students descending (Greedy approach)
    sorted_classes = sorted(data['classes'], key=lambda x: x['enrolled_students'], reverse=True)
    available_rooms = sorted(data['rooms'], key=lambda x: x['capacity'])
    
    schedule = []
    for cls in sorted_classes:
        assigned_room = None
        for room in available_rooms:
            if room['capacity'] >= cls['enrolled_students']:
                assigned_room = room
                break
                
        if assigned_room:
            wasted_seats = assigned_room['capacity'] - cls['enrolled_students']
            status = f"Wasted {wasted_seats} seats" if wasted_seats > 0 else "Perfect Fit"
            schedule.append({
                "class_id": cls['class_id'],
                "time": "09:00",
                "room": assigned_room['room_id'],
                "status": status
            })
        else:
            schedule.append({
                "class_id": cls['class_id'],
                "time": "N/A",
                "room": "N/A",
                "status": "Unscheduled"
            })
            
    return schedule
