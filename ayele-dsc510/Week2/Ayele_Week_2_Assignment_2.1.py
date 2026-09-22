# ---------------------------------------------------------
# DSC 510
# Week 2
# Programming Assignment: Week 2 - Fiber Optic Installation Cost
# Author: Yohannes Ayele
# 9/20/2026
#
# Purpose: Calculate the cost of installing fiber optic
#          cable based on user input of feet.
#
# ---------------------------------------------------------

# This will show a welcome message
print("Welcome to the Calculator for Fiber Optic Installation Costs.")
print("-*" * 30)

# User input company name
company_name = input("Please enter the company name: ")

# Find out how many feet of fiber optic cable need to be installed.
feet_of_cable = float(input("Input the fiber optic cable's length in feet: "))

# Cost per foot of fiber optic cable
cost_per_foot = 0.95

# Calculate the total installation cost
total_cost = feet_of_cable * cost_per_foot

# Display the final output report
print("\n" + "=" * 35)
print("Fiber Optic Installation Report")
print("=" * 35)
print(f"Company Name: {company_name}")
print(f"Feet of Cable: {feet_of_cable:,.2f}")
print(f"Cost Per Foot: ${cost_per_foot:.2f}")
print(f"Total Cost:    ${total_cost:,.2f}")
print("=" * 35)
print("Thank you for your business!")