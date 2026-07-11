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

# Test Coverage

| Test ID | Test Name | Validation Area |
|---|---|---|
| AUTO-001 | Required Events Validation | Checks that all required analytics events are received |
| AUTO-002 | Duplicate Events Detection | Detects duplicated analytics events |
| AUTO-003 | Event Sequence Validation | Validates correct analytics event order |
| AUTO-004 | Duplicate Reward Bug Detection | Detects duplicated reward claim events |
| AUTO-005 | Missing Progression Event Detection | Detects missing progression tracking events |

---

# Bugs Covered By Automation

## Duplicate Reward Events

Manual testing risk:

Reward events could be sent multiple times during specific completion scenarios.

Automated validation:

- detects duplicated reward events
- prevents incorrect reward analytics
- protects analytics funnels


---

## Incomplete Progression Tracking

Manual testing risk:

Progression analytics could miss intermediate progression states.

Automated validation:

- verifies required progression events
- detects missing analytics data
- improves reliability of progression tracking

```

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


# Test Execution Result

Example of successful automated test execution:

![Pytest Result](https://github.com/yungblyuty/QA-Portfolio/blob/main/Automation/Analytics_Validator/screenshots/pytest_result.jpg)

---

# Connection With Manual QA Experience

This automation project is based on real QA scenarios:

- analytics validation
- live event testing
- progression testing
- reward validation


It demonstrates the transition from manual validation processes to automated quality checks.
