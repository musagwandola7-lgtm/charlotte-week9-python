# Charlotte Week 9 Assignment
# Class 2: Python Collections and Drilling Telemetry

observations = [
    {
        "well_id": "WELL-07",
        "pressure": 2500,
        "temperature": 85
    },
    {
        "well_id": "WELL-08",
        "pressure": 2700,
        "temperature": 90
    }
]

# Display the first two observations
print(observations[:2])

# Display the last observation
print(observations[-1])

# Get unique well IDs
unique_wells = set()

for observation in observations:
    unique_wells.add(observation["well_id"])

print(sorted(unique_wells))

# Calculate total pressure
total_pressure = sum(observation["pressure"] for observation in observations)

print("Total pressure:", total_pressure, "psi")

# Calculate average pressure
average_pressure = total_pressure / len(observations)

print("Average pressure:", average_pressure, "psi")