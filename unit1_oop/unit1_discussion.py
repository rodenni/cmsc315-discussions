from copy import copy, deepcopy


# Parent Class
class Animal:
    living = True

    def __init__(self, name: str, species: str):
        self.name = name
        self.species = species

    def display_info(self):
        print(f"Name: {self.name}\nSpecies: {self.species}")


# Child Class
class Dog(Animal):
    sound = "Bark"

    def __init__(self, name: str, species: str, breed: str, achievements=None):
        super().__init__(name, species)

        if achievements is None:
            achievements = {"tricks": 0, "competitions": 0}

        self.breed = breed
        self.achievements = achievements

    def change_breed(self, breed):
        if breed != self.breed:
            self.breed = breed
        else:
            print(f"{self.name} is already a {self.breed}.")

    def update_achievements(self, tricks=0, competitions=0):
        self.achievements["tricks"] = tricks
        self.achievements["competitions"] = competitions

    def display_info(self):
        print(
            f"Name: {self.name}\n"
            f"Species: {self.species}\n"
            f"Breed: {self.breed}\n"
            f"Achievements:"
        )

        for key, value in self.achievements.items():
            print(f"\t{key}: {value}")


# Namespace Demonstration
def demonstrate_namespaces():
    print("\n=== Namespace Demonstration ===")

    dog_one = Dog("Buddy", "Canine", "Golden Retriever")
    dog_two = Dog("Max", "Canine", "German Shepherd")

    # Access class variable through class
    print(f"Class access: {Dog.sound}")

    # Access class variable through object
    print(f"Object access: {dog_one.sound}")

    # Add an attribute to one object only
    dog_one.favorite_toy = "Tennis Ball"

    print("\nDog One Namespace:")
    print(dog_one.__dict__)

    print("\nDog Two Namespace:")
    print(dog_two.__dict__)

    print("\nDog Class Namespace:")
    print(Dog.__dict__)


# Copy Demonstration
def demonstrate_copying():
    print("\n=== Copy Demonstration ===")

    dog_one = Dog("Buddy", "Canine", "Golden Retriever")
    dog_one.update_achievements(5, 2)

    # Shallow copy
    shallow_copy = copy(dog_one)

    # Deep copy
    deep_copy = deepcopy(dog_one)

    # Modify original nested data
    dog_one.update_achievements(10, 4)

    print("\nOriginal Object:")
    dog_one.display_info()

    print("\nShallow Copy:")
    shallow_copy.display_info()

    print("\nDeep Copy:")
    deep_copy.display_info()

    # Explanation:
    # The shallow copy shares the same achievements dictionary
    # as the original object. Therefore, changes made to the
    # original dictionary appear in the shallow copy.
    #
    # The deep copy creates a completely separate achievements
    # dictionary, so changes to the original do not affect it.


# Main Function
def main():
    print("=== Unit 1 OOP Assignment ===\n")

    # Parent object
    animal = Animal("Leo", "Lion")

    # Child object
    dog = Dog("Buddy", "Canine", "Golden Retriever")

    print("Parent Class Demonstration:")
    animal.display_info()

    print("\nChild Class Demonstration:")
    dog.display_info()

    demonstrate_namespaces()
    demonstrate_copying()


if __name__ == "__main__":
    main()