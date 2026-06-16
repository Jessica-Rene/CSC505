"""
CSC 505 - Principles of Software Development
Author: Jessica R. Reyes
Due Date: 21 June 2026
Description: This script allows users to build an adaptive model by defining phases and their descriptions. 
The model emphasizes iterative feedback and continuous improvement between phases.
"""

def main():
    print("Adaptive Model Builder\n")

    phrases = []
    num_phrases = int(input("How many phases are in your model? "))

    for i in range(num_phrases):
        print(f"\nPhase {i + 1}:")
        name = input("Enter phase name: ")
        description = input("Enter phase description: ")
        phrases.append((name, description))

    print("\nYour adaptive model:")
    for i, (name, description) in enumerate(phrases, start=1):
        print(f"Phase {i}: {name} - {description}")
    print("\nModel structure includes iterative feedback and continuous improvement between phases.")

if __name__ == "__main__":
    main()