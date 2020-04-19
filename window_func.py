import csv
from datetime import datetime
"""
{
    name: "v",
    current_window: datestamp,
    current_window_count:
    max_count:
}
"""
windowed = []
time = []
max_in_one_window = []
def find_in(array, value):
    for ob in array:
        if value == ob["name"]:
            return ob
    return None

def format_time(s):
    return datetime.strptime(s, "%H:%M:%S.%f")

def create_obj(row):
    return {
        "name": row[3],
        "current_window": format_time(row[0]),
        "current_window_count": 1,
        "max_count": 1
    }

def reset_obj(old_obj, row):
    old_obj["current_window"] = format_time(row[0])
    old_obj["current_window_count"] = 1
    return old_obj

def incremet_current_window(obj):
    obj["current_window_count"] += 1
    if obj["current_window_count"] > obj["max_count"]:
        obj["max_count"] = obj["current_window_count"]
    return obj

with open("trades.csv", "r") as f:
    reader = csv.reader(f)
    for row in reader:
        obj = find_in(windowed, row[3])
        if obj:
            delta = format_time(row[0]) - obj["current_window"]
            if (delta.seconds*1000000+delta.microseconds) >= 6000000:
                reset_obj(obj, row)
            else:
                incremet_current_window(obj)
        else:
            windowed.append(create_obj(row))



windowed = sorted(windowed, key=lambda o: o["name"])
for w in windowed:
    print(w["max_count"])

