# Flight Data Schema (Updated)

| Column | Description | Unit |
|------|------------|------|
| time_sec | Timestamp | sec |
| altitude_ft | Flight altitude | ft |
| airspeed_mps | Airspeed | m/s |
| battery_voltage | Battery voltage | V |
| battery_current | Battery current | A |
| soc | State of Charge | % |
| wind_speed_kt | Wind speed | kt |
| wind_longitudinal | Longitudinal wind component (head/tail) | kt |
| wind_lateral | Lateral wind component (crosswind) | kt |
| wind_vertical | Vertical wind component | kt |

Notes:
- Wind is represented as a 3D vector.
- Positive longitudinal = tailwind, negative = headwind.
