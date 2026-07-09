import sys
import os

sys.path.append(os.path.abspath("src"))

from validator import (
    load_events,
    has_required_events,
    has_duplicate_events,
    is_correct_sequence
)


EVENTS_FILE = "data/analytics_events.json"


def test_required_events_exist():
    events = load_events(EVENTS_FILE)

    required_events = [
        "event_started",
        "milestone_completed",
        "reward_claimed",
        "event_completed"
    ]

    assert has_required_events(events, required_events)


def test_no_duplicate_events():
    events = load_events(EVENTS_FILE)

    assert has_duplicate_events(events) is False


def test_event_sequence():
    events = load_events(EVENTS_FILE)

    expected_sequence = [
        "event_started",
        "milestone_completed",
        "reward_claimed",
        "event_completed"
    ]

    assert is_correct_sequence(events, expected_sequence)


def test_detect_duplicate_reward_bug():
    events = load_events(
        "data/duplicate_reward_events.json"
    )

    assert has_duplicate_events(events) is True


def test_detect_missing_progression_event():
    events = load_events(
        "data/missing_progression_event.json"
    )

    required_events = [
        "event_started",
        "milestone_completed",
        "reward_claimed",
        "event_completed"
    ]

    assert has_required_events(
        events,
        required_events
    ) is False
