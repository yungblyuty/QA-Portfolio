# Case Study: Testing a Limited-Time Resource Collection Event in a Mobile Casual Game

---

# Feature Overview

## Context

The feature under testing was a limited-time in-game event focused on resource collection and progression rewards.

Players participated in the event by:
- collecting special event resources through gameplay
- progressing through reward milestones
- exchanging collected resources for rewards

The event included:
- event rewards
- consumable rewards
- progression-based reward stages

The feature was designed to:
- increase player engagement
- improve retention during the event period
- encourage recurring gameplay sessions
- support monetization through event-related offers

Due to the feature’s impact on progression systems and player motivation, the event required deep validation of:
- gameplay balance
- progression pacing
- analytics accuracy
- live-event synchronization

---

# Testing Objectives

The primary testing goals included:
- validating event progression logic
- ensuring reward delivery accuracy
- verifying synchronization between client and server event states
- preventing progression-related issues
- validating analytics tracking
- ensuring event lifecycle stability

Special attention was given to:
- progression pacing
- reward economy
- event restart scenarios
- edge-case progression states

The testing process focused not only on identifying defects, but also on minimizing risks affecting:
- retention
- monetization
- overall player experience

---

# Risk Analysis

## Progression & Economy Risks

### Identified Risks
- incorrect progression scaling
- progression acceleration
- duplicated rewards
- broken reward sequences
- economy imbalance

### Potential Impact
- progression exploitation
- reduced long-term engagement
- monetization devaluation
- reward economy instability

One identified issue allowed players to complete progression significantly faster than intended, creating major balance risks.

---

## Live Event Risks

### Identified Risks
- incorrect event start timing
- desynchronization between client and server
- unexpected event restart behavior
- inconsistent event stage transitions

### Potential Impact
- inconsistent player experience
- confusion during event participation
- reduced trust in live-event systems

---

## Analytics Risks

### Identified Risks
- duplicated analytics events
- incomplete progression tracking
- incorrect milestone reporting
- missing stage completion data

### Potential Impact
- inaccurate analytics
- unreliable progression metrics
- incorrect product decisions

---

## UX Risks

### Identified Risks
- visually incorrect progression bar states
- misleading progression feedback
- unclear reward state transitions

### Potential Impact
- player confusion
- reduced usability
- decreased engagement

---

# Testing Strategy

Testing priorities were based on:
- progression impact
- monetization impact
- retention risks
- live-event stability
- analytics reliability

The testing strategy combined:
- functional testing
- exploratory testing
- regression testing
- analytics validation
- edge-case validation

---

# Testing Types

## Functional Testing

Validation included:
- resource collection
- milestone progression
- reward delivery
- progression calculations
- event restart conditions
- timer synchronization

---

## Exploratory Testing

Exploratory testing focused on:
- unusual progression behavior
- rapid milestone completion
- interrupted event flows
- simultaneous reward claims
- edge-case progression states
- reconnect scenarios

This approach helped uncover several high-impact issues outside predefined test coverage.

---

## Regression Testing

Regression testing validated:
- stability of existing event systems
- compatibility with other live features
- absence of side effects after remote configuration updates

---

## Analytics Validation

Validation included:
- progression events
- reward claim tracking
- milestone completion events
- event restart tracking

The goal was to ensure accuracy and completeness of analytics data used for product analysis.

---

# Critical Issues Identified

## Incorrect Event Start Timing

### Description
The actual event start time differed from the values defined in remote configuration settings.

### Risks
- inconsistent player experience
- event synchronization issues
- reduced trust in live-event systems

### Result
The issue was identified before release and corrected prior to deployment.

---

## Progress Bar Visual State Issue

### Description
At boundary progression values between event stages, the progress bar appeared visually completed before the actual milestone was reached.

### Risks
- misleading player feedback
- progression confusion
- negative user experience

### Result
The issue was reproduced and fixed before release.

---

## Unexpected Event Restart Behavior

### Description
After fully completing the event and collecting all rewards, the event restarted from the beginning instead of ending correctly.

### Risks
- unlimited reward farming
- economy destabilization
- monetization devaluation

### Result
The issue was identified during exploratory testing and resolved before release.

---

## Duplicate Reward Analytics Events

### Description
Reward claim analytics events were duplicated under specific event completion scenarios.

### Risks
- incorrect analytics data
- inflated reward metrics
- unreliable product analysis

### Result
The issue was documented and fixed before release.

---

## Incomplete Progression Analytics Tracking

### Description
If multiple progression stages were completed simultaneously, analytics events were triggered only for the current and final stage, while intermediate stages were skipped.

### Risks
- incomplete progression analytics
- inaccurate event funnel data
- unreliable progression metrics

### Result
The issue was escalated and corrected before release.

---

# Cross-Functional Collaboration

The testing process involved active collaboration with:
- developers
- product managers
- game designers

Responsibilities included:
- validating event logic
- discussing balance risks
- clarifying progression behavior
- reviewing event readiness before release
- evaluating monetization and retention risks

Several release-related decisions were adjusted based on identified progression and economy risks.

---

# Process Improvement

During simultaneous work on multiple live-event systems, a real-time QA collaboration workflow was introduced to improve communication and testing efficiency.

### Results
- faster validation cycles
- reduced feedback loop
- improved regression efficiency
- faster issue investigation
- improved release stability

The workflow was actively used by:
- QA
- product managers
- game designers
- development teams

---

# Result & Impact

Testing activities helped prevent critical issues affecting:
- player retention
- progression balance
- reward economy
- monetization
- analytics reliability
- live-event stability

The combination of exploratory and risk-based testing significantly improved release quality and reduced production risks before the event launch.

---

# Test Plan
[TP-004](https://docs.google.com/spreadsheets/d/10MAkEVS5qUhmlEqaCDZF8TK_DDyotVlVMqlT7zZ4H1M/edit?gid=945417199#gid=945417199&range=A6:K6)

---

# Test Cases
[TC-TP004](https://docs.google.com/spreadsheets/d/10MAkEVS5qUhmlEqaCDZF8TK_DDyotVlVMqlT7zZ4H1M/edit?gid=1694348965#gid=1694348965&range=A28:M37)

---

# Bug Reports

[BUG_004](https://docs.google.com/spreadsheets/d/10MAkEVS5qUhmlEqaCDZF8TK_DDyotVlVMqlT7zZ4H1M/edit?gid=0#gid=0&range=A19:T26)

