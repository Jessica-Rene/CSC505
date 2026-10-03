"""
CSC 505 - Principles of Software Development
Author: Jessica R. Reyes
Due Date: 28 June 
Description: Shopping List Prototype.
"""

# Define screens
screens = [
    "Home",
    "Add Item",
    "View List",
    "Edit Item",
    "Settings"
]

# Define navigation flow
navigation_flow = {
    "Home": ["Add Item", "View List", "Settings"],
    "Add Item": ["View List"],
    "View List": ["Edit Item"],
    "Edit Item": ["View List"],
    "Settings": ["Home"]
}

# Print summary
print("Screens:", ", ".join(screens))
print("Total Screens:", len(screens))

print("\nNavigation Flow:")
for screen, destinations in navigation_flow.items():
    for dest in destinations:
        print(f" - {screen} → {dest}")

# Optional descriptions
screen_descriptions = {
    "Home": "Main dashboard for navigation.",
    "Add Item": "Add a new shopping list item.",
    "View List": "Displays all items in the shopping list.",
    "Edit Item": "Modify or delete an item.",
    "Settings": "Configure app preferences."
}

print("\nScreen Descriptions:")
for screen, description in screen_descriptions.items():
    print(f" - {screen}: {description}")
    