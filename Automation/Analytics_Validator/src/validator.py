import json


def load_events(file_path):
    with open(file_path, "r") as file:
        return json.load(file)


def get_event_names(events):
    return [event["event_name"] for event in events]


def has_required_events(events, required_events):
    event_names = get_event_names(events)

    for event in required_events:
        if event not in event_names:
            return False

    return True


def has_duplicate_events(events):
    event_ids = []

    for event in events:
        event_ids.append(event["event_id"])

    return len(event_ids) != len(set(event_ids))


def is_correct_sequence(events, expected_sequence):
    actual_sequence = get_event_names(events)

    return actual_sequence == expected_sequence
