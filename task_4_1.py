

import json

def task() -> float:
    with open("input.json", "r", encoding="utf-8") as f:
        data = json.load(f)

    total = sum(item.get("score", 0) * item.get("weight", 0) for item in data)
    return round(total, 3)


print(task())