"""
Unique Visitor Tracker using Sets
"""

# Visitors (IPs)
day1 = {"192.168.1.1", "192.168.1.2", "192.168.1.3"}
day2 = {"192.168.1.2", "192.168.1.3", "192.168.1.4"}

# 🔹 Common visitors (retention)
common = day1.intersection(day2)

# 🔹 Unique visitors per day
unique_day1 = day1.difference(day2)
unique_day2 = day2.difference(day1)

# 🔹 Total unique visitors
total_unique = day1.union(day2)

# 🔹 Metrics
growth_rate = (len(day2) - len(day1)) / len(day1) * 100
retention_rate = len(common) / len(day1) * 100

print("\n--- Visitor Analysis ---")
print("Common Visitors:", common)
print("Unique Day 1:", unique_day1)
print("Unique Day 2:", unique_day2)
print("Total Unique Visitors:", total_unique)

print(f"Growth Rate: {growth_rate:.2f}%")
print(f"Retention Rate: {retention_rate:.2f}%")