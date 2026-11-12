
# Charlotte Week 9 Assignment
# Class 2: Python Collections and Drilling Telemetry

# Store eight sensor observations in a list of dictionaries
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
    },
    {
        "well_id": "WELL-07",
        "pressure": 2600,
        "temperature": 86
    },
    {
        "well_id": "WELL-09",
        "pressure": 2400,
        "temperature": 82
    },
    {
        "well_id": "WELL-08",
        "pressure": 2800,
        "temperature": 91
    },
    {
        "well_id": "WELL-07",
        "pressure": 2550,
        "temperature": 84
    },
    {
        "well_id": "WELL-09",
        "pressure": 2450,
        "temperature": 83
    },
    {
        "well_id": "WELL-08",
        "pressure": 2750,
        "temperature": 89
    }
]

# 1. Display the first two and last observations
print("First two observations:")
print(observations[:2])

print("Last observation:")
print(observations[-1])

# 2. Create and display sorted distinct well IDs
unique_wells = set()

for observation in observations:
    unique_wells.add(observation["well_id"])

print("Sorted unique well IDs:")
print(sorted(unique_wells))

# 3. Calculate the total and average pressure
total_pressure = sum(observation["pressure"] for observation in observations)

print("Total pressure:", total_pressure, "psi")

average_pressure = total_pressure / len(observations)

print("Average pressure:", average_pressure, "psi")

# 4. Count the number of observations per well
well_counts = {}

for observation in observations:
    well_id = observation["well_id"]

    if well_id not in well_counts:
        well_counts[well_id] = 0

    well_counts[well_id] += 1

print("Number of observations per well:")
print(well_counts)

# Display the distinct field names
fields = set(observations[0].keys())

print("Distinct fields:")
print(sorted(fields))