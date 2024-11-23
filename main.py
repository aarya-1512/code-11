def parse_blood_pressure(bp_str):
    systolic, diastolic = map(int, bp_str.split('/'))
    return systolic, diastolic


def calculate_patient_statistics(filename):
    # Initialize variables
    ages = []
    male_count = 0
    female_count = 0
    blood_pressures = []
    temperatures = []

    # Read and process the file
    with open(filename, 'r') as file:
        # Skip header line
        next(file)

        for line in file:
            # Split the line and remove whitespace
            name, age, gender, bp, temp = [x.strip() for x in line.split(',')]

            # Process age
            ages.append(int(age))

            # Process gender
            if gender.lower() == 'male':
                male_count += 1
            else:
                female_count += 1

            # Process blood pressure
            blood_pressures.append(bp)

            # Process temperature
            temperatures.append(float(temp))

    # Calculate blood pressure statistics
    bp_systolic_values = [parse_blood_pressure(bp)[0] for bp in blood_pressures]
    bp_diastolic_values = [parse_blood_pressure(bp)[1] for bp in blood_pressures]
    highest_bp_idx = bp_systolic_values.index(max(bp_systolic_values))
    lowest_bp_idx = bp_systolic_values.index(min(bp_systolic_values))

    # Calculate average age and temperature
    avg_age = sum(ages) / len(ages)
    avg_temp = sum(temperatures) / len(temperatures)

    # Format the results
    results = {
        'AverageAge': round(avg_age, 2),
        'MalePatients': male_count,
        'FemalePatients': female_count,
        'HighestBloodPressure': blood_pressures[highest_bp_idx],
        'LowestBloodPressure': blood_pressures[lowest_bp_idx],
        'AverageTemperature': round(avg_temp, 2)
    }

    return results


def print_statistics(stats):
    print("-- Patient Data Statistics --")
    for key, value in stats.items():
        print(f"{key}: {value}")


# Run the analysis
if _name_ == "_main_":
    filename = "Week13Assignment.txt"
    statistics = calculate_patient_statistics(filename)
    print_statistics(statistics)
