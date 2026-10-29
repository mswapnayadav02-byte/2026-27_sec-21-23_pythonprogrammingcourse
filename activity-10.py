# Smart Campus Maintenance Prioritisation

reports = []

n = int(input("Enter number of incidents: "))

for i in range(n):
    name = input("Incident name: ")
    severity = input("Severity (High/Medium/Low): ").lower()
    location = input("Location: ").lower()
    frequency = int(input("Frequency: "))

    # Assign priority
    if severity == "high":
        priority = "Critical"
        score = 4

    elif severity == "medium" and (
        location == "laboratory" or
        location == "library" or frequency >= 3
    ):
        priority = "High"
        score = 3

    elif severity == "low" and frequency >= 5:
        priority = "Medium"
        score = 2

    else:
        priority = "Low"
        score = 1

    reports.append([name, location, frequency, priority, score])

# Sort by priority
reports.sort(key=lambda x: x[4], reverse=True)

# Display report
print("\n--- MAINTENANCE PRIORITY REPORT ---")

for i, report in enumerate(reports, 1):
    print(i, report[0], report[1], report[2], report[3])

# Display urgent requirements
print("\n--- OUTSTANDING REQUIREMENTS ---")

for report in reports:
    if report[4] >= 3:
        print(report[0], "-", report[3],
              "- Immediate maintenance required")

print("\nReport completed.")