"""
🔥 PyNexus: Age Chrono-Converter 🔥
Author: YourName
Description: Transforms your age into cosmic units — years, months, and days — with leap year intelligence. 
"""   
      
import time
from calendar import isleap

def is_leap_year(year):
    return isleap(year)

def get_month_days(month, is_leap):
    """Return the number of days in a given month, considering leap years."""
    if month in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    elif month in [4, 6, 9, 11]:
        return 30
    elif month == 2:
        return 29 if is_leap else 28

# 🚀 User Input Zone
print("🌀 Welcome to PyNexus Age Chrono-Converter 🌀")
name = input("Enter your name: ")
age_years = int(input("Enter your age in years: "))

# 🧭 Time Data Acquisition
current_time = time.localtime()
current_year = current_time.tm_year
current_month = current_time.tm_mon
current_day = current_time.tm_mday

# ⏳ Chrono Calculations
total_months = age_years * 12 + current_month
total_days = 0

birth_year = current_year - age_years
for year in range(birth_year, current_year):
    total_days += 366 if is_leap_year(year) else 365

# Add days from current year months before current month
for month in range(1, current_month):
    total_days += get_month_days(month, is_leap_year(current_year))

# Add days from current month
total_days += current_day

# ✨ Results
print(f"\n🎉 Hello, {name}!")
print(f"🔹 You are {age_years} years old.")
print(f"🔸 That's approximately {total_months} months.")
print(f"🔻 Or a galactic {total_days} days on Earth.")
print("🧠 Calculated with leap-year precision by PyNexus.\n")
