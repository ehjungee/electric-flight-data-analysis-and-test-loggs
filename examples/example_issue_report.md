# Issue Report – Recurrent SOC Fluctuation During Test Runs

## Issue ID
ISSUE-2026-01-003

## Date Identified
2026-01-20

## Test Context
- Test Type: Electric aircraft climb performance test
- Flight Phase: Initial climb (below 500 m)
- Climb Profile: Continuous Climb
- Environment:
  - OAT: 5°C
  - Wind: Light to moderate headwind

## Issue Description
During multiple test runs, short-term fluctuations in SOC (State of Charge) readings
were observed during the initial climb phase. The fluctuation appeared as sudden
drops and recoveries within a short time window.

## Frequency
- Observed in 3 out of 5 test flights
- Occurred consistently during early climb phase

## Affected Signals
- SOC (%)
- Battery current (A)

## Initial Analysis / Suspected Cause
- Possible sensor noise under high current draw
- SOC estimation instability during rapid power changes
- Low-temperature effects on battery management system (BMS)

## Temporary Workaround
- Ignore SOC readings within the first 30 seconds of climb for performance comparison
- Cross-check SOC change using integrated current instead of instantaneous SOC

## Suggested Follow-up Actions
- Verify SOC estimation algorithm behavior during high load
- Compare SOC trend with raw voltage/current integration
- Flag early-climb SOC data during automated analysis

## Status
Open – requires further validation with additional flight data
