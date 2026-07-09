# Game Analytics Validator

## Overview

Game Analytics Validator is a QA Automation project focused on validating analytics events in mobile game systems.

This project demonstrates automation of checks commonly performed during analytics validation for:

- live events
- progression systems
- reward systems
- player actions tracking


The goal is to ensure analytics reliability and prevent incorrect product data.

---

# Testing Scope

The automation validates:

- required analytics events
- event sequence correctness
- duplicate events
- reward-related tracking issues


---

# Test Data

Analytics events are stored in JSON format:

Example event:

```json
{
  "event_name": "reward_claimed",
  "user_id": "user_001",
  "reward_type": "coins",
  "reward_amount": 100
}
```

---

# Automated Tests

## TC-AUTO-001: Required Events Validation

Validates that all required analytics events are present.

Checks:

- event_started
- milestone_completed
- reward_claimed
- event_completed

---

## TC-AUTO-002: Duplicate Events Detection

Validates that analytics events are not duplicated.

Prevents issues such as:

- duplicated reward events
- incorrect analytics metrics
- corrupted event funnels

---

## TC-AUTO-003: Event Sequence Validation

Validates correct event order.

Expected flow:

Player starts event

↓

Completes milestone

↓

Claims reward

↓

Completes event


Incorrect event sequences are detected automatically.

---

# Project Structure

```
Analytics_Validator/

├── data/
│   └── analytics_events.json

├── src/
│   └── validator.py

├── tests/
│   └── test_analytics.py

└── requirements.txt
```

---

# Technologies Used

- Python
- Pytest
- JSON
- Automated validation

---

# How To Run Tests

Install dependencies:

```bash
pip install -r requirements.txt
```

Run tests:

```bash
pytest
```

---

# Connection With Manual QA Experience

This automation project is based on real QA scenarios:

- analytics validation
- live event testing
- progression testing
- reward validation


It demonstrates the transition from manual validation processes to automated quality checks.
