# Case Study: Testing an In-Game Store in a Mobile Farming Simulator

## Feature Overview

### Context
The feature under testing was an in-game store system used for:
- premium currency purchases
- limited-time offers
- progression-related offers
- monetization of in-game events

The store was one of the core monetization systems of the project and directly impacted:
- project revenue
- player retention
- progression balance
- overall user experience

Due to its high business criticality, the feature required not only functional validation, but also deep analysis of risks related to:
- game economy
- player behavior
- progression systems
- edge-case scenarios

---

# Testing Objectives

Main testing goals included:
- ensuring store stability across different user scenarios
- validating purchase flow reliability
- preventing monetization blockers before release
- validating analytics correctness
- identifying UX issues affecting conversion
- detecting risks affecting progression balance and player retention

The testing process focused not only on defect detection, but also on minimizing business and production risks.

---

# Risk Analysis

## Monetization Risks

### Identified Risks
- purchase failures
- blocked purchase flow
- incorrect offer configuration
- duplicated purchases
- reward delivery issues

### Potential Impact
- direct revenue loss
- increased refund requests
- reduced player trust
- lower conversion rates

---

## Economy & Progression Risks

### Identified Risks
- incorrectly configured progression-related offers
- excessive rewards
- accelerated progression
- economy imbalance

### Potential Impact
- reduced retention
- shortened player lifecycle
- monetization devaluation

One identified issue allowed players to progress significantly faster than intended progression pacing.

---

## UX & User Flow Risks

### Identified Risks
- overlapping UI windows
- hidden purchase buttons
- inconsistent navigation
- conflicts between onboarding and store flow

### Potential Impact
- reduced usability
- player frustration
- decreased monetization efficiency

Special attention was given to player behavior during early-session gameplay.

---

## Analytics Risks

### Identified Risks
- missing analytics events
- incorrect event tracking
- incomplete data collection
- inconsistencies between expected and actual analytics behavior

### Potential Impact
- inaccurate product data
- incorrect business decisions
- unreliable monetization metrics

---

# Testing Strategy

Testing priorities were based on:
- business criticality
- monetization impact
- user experience risks
- release stability risks

The testing strategy combined:
- structured testing
- exploratory testing
- risk-based testing

---

## Functional Testing

Validation included:
- purchase flow
- offer logic
- reward delivery
- pricing accuracy
- limitations and timers

---

## Exploratory Testing

Exploratory testing was heavily used due to:
- complex interactions between systems
- event-related dependencies
- complex monetization scenarios

### Focus Areas
- interrupted user flows
- unusual player behavior
- rapid interactions
- conflicts between ads and store systems
- edge-case session states

This approach helped identify several critical issues outside predefined test cases.

---

## Regression Testing

Regression testing validated:
- stability of existing functionality
- compatibility with live events
- absence of side effects after updates

---

## Analytics Validation

Validation included:
- purchase events
- reward claim events
- progression tracking
- offer interaction tracking

The goal was to ensure reliability and accuracy of analytics data used for product decisions.

---

# Critical Issues Identified

## Critical Purchase Blocker

### Description
A critical issue caused purchase flow failures with a high reproduction rate under specific conditions.

### Risks
- blocked monetization
- direct revenue loss
- negative user experience

### Result
The issue was identified and fixed before release.

---

## Progression Balance Issue

### Description
A configuration issue in progression rewards allowed players to progress significantly faster than intended progression pacing.

### Risks
- economy destabilization
- reduced player engagement
- monetization devaluation

### Result
The issue was identified during exploratory testing and resolved before release.

---

## UI Conflict Affecting Monetization

### Description
A rewarded advertisement window overlapped the premium currency store during a forced store popup scenario.

### Risks
- reduced conversion
- blocked monetization flow
- degraded user experience

### Result
The issue was reproduced, documented, and fixed before release.

---

# Cross-Functional Collaboration

The testing process required active collaboration with:
- developers
- product managers (PM)
- game designers (GD)

### Responsibilities Included
- clarification of feature logic
- alignment on expected behavior
- discussion of retention and monetization risks
- participation in release readiness evaluation

Several release decisions were reconsidered based on identified risks.

---

# Result & Impact

The testing process helped prevent critical production issues affecting:
- monetization
- player retention
- progression balance
- analytics reliability
- overall user experience

The combination of exploratory and risk-based testing significantly improved release stability and reduced production risks before deployment.

---

# Test Plan
[TP-003](https://docs.google.com/spreadsheets/d/10MAkEVS5qUhmlEqaCDZF8TK_DDyotVlVMqlT7zZ4H1M/edit?gid=945417199#gid=945417199&range=A5:K5)

---

# Test Cases
[TC-TP003](https://docs.google.com/spreadsheets/d/10MAkEVS5qUhmlEqaCDZF8TK_DDyotVlVMqlT7zZ4H1M/edit?gid=1694348965#gid=1694348965&range=A19:M26)

---

# Bug Reports

[BUG_003](https://docs.google.com/spreadsheets/d/10MAkEVS5qUhmlEqaCDZF8TK_DDyotVlVMqlT7zZ4H1M/edit?gid=0#gid=0&range=A12:T20)
