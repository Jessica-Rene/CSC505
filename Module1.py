"""
CSC 505 - Principles of Software Development
Author: Jessica R. Reyes
Due Date: 14 June 
Description: This script reads a CSV file of student grades and calculates basic statistics.
"""

import csv

def read_grades(filename):
    """Reads grades from a CSV file and returns a list of grades."""
    grades = []
    with open(filename, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            grades.append(float(row['score']))
    return grades

def analyze_grades(grades):
    total = sum(grades)
    average = total / len(grades) if grades else 0
    highest = max(grades) if grades else 0
    lowest = min(grades) if grades else 0

    print("Grade Analysis")
    print("-------------")
    print(f"Average: {average:.2f}")
    print(f"Highest: {highest}")
    print(f"Lowest: {lowest}")

def main():
    filename = 'grades.csv'
    grades = read_grades(filename)
    analyze_grades(grades)

if __name__ == "__main__":
    main()
