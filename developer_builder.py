"""
CSC 505 - Principles of Software Development
Author: Jessica R. Reyes
Due Date: 5 July 2026
Description: Personality Traits.
"""

class Developer:
    def __init__(self, curiosity, adaptability, communication):
        self.curiosity = curiosity
        self.adaptability = adaptability
        self.communication = communication
    
    def show_traits(self):
        print("Building your ideal developer...\n")
         
        traits = [
            ("Curiosity", self.curiosity),
            ("Adaptability", self.adaptability),
            ("Communication", self.communication)
        ]
        for name, desc in traits:
            print(f"Trait: {name} - {desc}")
                  
        print(f"\n Total traits included: {len(traits)}")

class DeveloperBuilder:
    def __init__(self):
        self.curiosity = None
        self.adaptability = None
        self.communication = None
    
    def set_curiosity(self, description):
        self.curiosity = description
        return self
    def set_adaptability(self, description):
        self.adaptability = description
        return self

    def set_communication(self, description):
        self.communication = description
        return self

    def build(self):
        return Developer(
            self.curiosity, 
            self.adaptability, 
            self.communication)

if __name__ == "__main__":
    developer = (
        DeveloperBuilder()
        .set_curiosity("Drives exploration of new tools and techniques.")
        .set_adaptability("Enables flexibility in changing environments.")
        .set_communication("Enhances team collaboration and clarity.")
        .build()
    )
    
    developer.show_traits()
    