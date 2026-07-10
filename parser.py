import json


def load_events(log_file):
    """
    Read Cowrie JSON log (one JSON object per line).
    Returns a list of event dictionaries.
    """
    events = []

    with open(log_file, "r", encoding="utf-8") as file:
        for line in file:
            line = line.strip()

            if not line:
                continue

            try:
                events.append(json.loads(line))
            except json.JSONDecodeError:
                continue

    return events