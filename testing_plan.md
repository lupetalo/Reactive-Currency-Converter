# Testing Plan

**Target URL**: ask user

This document outlines the test cases to verify the full functionality of the Reactive Currency Converter. It will be updated as development progresses.

## Test Environment
- **Browser**: Modern Chrome/Firefox/Safari
- **URL**: ask user

## Test Cases

### 1. Initialization & Configuration
- [ ] **TC1.1: Load Config Data**
  - **Action**: Open the application.
  - **Expected**: 
    - Page Title should be "Reactive Currency Converter".
    - Card Title should be "Converter".
    - Labels "Amount", "Currency" should be visible.
    - Footer text "Live rates updated instantly." should be visible.
- [ ] **TC1.2: Load Rates Data**
  - **Action**: Check the "Currency" dropdown and the conversion table.
  - **Expected**: 
    - Dropdown should contain currency codes (e.g., USD, EUR, GBP).
    - Table should list exchange rates.

### 2. Default State
- [ ] **TC2.1: Default Values**
  - **Action**: Observe initial inputs.
  - **Expected**: 
    - Amount should be `1` (or value from `config.json`).
    - Currency should be `USD` (or default from `rates.json`).
    - Theme should be `forest` (or first in `config.themes`).

### 3. Core Functionality (Reactivity)
- [ ] **TC3.1: Convert Amount**
  - **Action**: Change "Amount" input to `100`.
  - **Expected**: Table values should update instantly to reflect `100 * Rate`.
- [ ] **TC3.2: Change Base Currency**
  - **Action**: Select a different currency (e.g., `EUR`) from the dropdown.
  - **Expected**: 
    - Symbol input icon should update (e.g., `$` -> `€`).
    - Table should filter out `EUR` and show `USD`.
    - Conversion rates should recalculate based on `EUR`.
- [ ] **TC3.3: Exhaustive Currency Check**
  - **Action**: For *each* currency in the list (EUR, USD, RSD, GBP):
    1. Select currency.
    2. Change amount to `50`.
    3. Verify conversion table updates.
  - **Expected**: Every currency selection should trigger a correct UI update and calculation.

### 4. UI & Theming
- [ ] **TC4.1: Switch Theme**
  - **Action**: Select a different theme (e.g., `Forest`).
  - **Expected**: 
    - Background colors and fonts should change immediately.
    - Selection should persist in `localStorage` (if reload is tested).
- [ ] **TC4.2: Responsiveness**
  - **Action**: Resize browser to mobile width (< 500px).
  - **Expected**: Layout should remain usable (stacked or fitted).

### 5. Technical Verification
- [ ] **TC5.1: No Console Errors**
  - **Action**: Open Developer Tools -> Console.
  - **Expected**: No red error messages (404s, JS errors).
- [ ] **TC5.2: Local Assets**
  - **Action**: Open Developer Tools -> Network.
  - **Expected**: Key assets (`alpine.js`, `daisyui.css`, etc.) should be loaded from `/assets/` (or relative path), not external CDNs.

## Test History
| Date | Version | Result | Notes |
|------|---------|--------|-------|
| 2026-01-05 | 1.0.0 | ✅ PASS | All core functional tests passed on production. |
| 2026-01-05 | 1.0.0 | ✅ PASS | Exhaustive currency check (EUR, USD, RSD, GBP) passed. |
