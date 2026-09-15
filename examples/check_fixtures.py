import json
from pathlib import Path

def validate(path):
    cases = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(cases, list) or not cases:
        raise ValueError("Expected nonempty case list")
    ids = set()
    for case in cases:
        if not all(isinstance(case.get(key), str) and case[key].strip() for key in ("id", "prompt", "expected")):
            raise ValueError("Missing evaluation fields")
        if case["id"] in ids:
            raise ValueError("Duplicate evaluation ID")
        ids.add(case["id"])
    return len(cases)

if __name__ == "__main__":
    print(f"Validated {validate(Path(__file__).with_name('evaluations.json'))} fixtures; run agent evaluations manually")
