# Virtual Pet Simulator
# Python Assignment A2
# This program allows a user to take care of a virtual pet by feeding,
# playing, and checking its status.

def feed_pet(pet):
    # Feeding reduces hunger but slightly reduces happiness
    pet["hunger"] -= 15
    pet["happiness"] -= 5
    print("\nYou fed the pet 🥕")

def play_with_pet(pet):
    # Playing increases happiness but increases hunger
    pet["happiness"] += 15
    pet["hunger"] += 10
    print("\nYou played with the pet 🎾")

def check_status(pet):
    # Display current pet status
    print("\n🐾 Pet Status 🐾")
    print("Hunger Level   :", pet["hunger"])
    print("Happiness Level:", pet["happiness"])

def apply_time_effects(pet):
    # Automatic changes as time passes
    pet["hunger"] += 5
    pet["happiness"] -= 5

def keep_values_in_range(pet):
    # Ensure hunger and happiness stay between 0 and 100
    pet["hunger"] = max(0, min(100, pet["hunger"]))
    pet["happiness"] = max(0, min(100, pet["happiness"]))

def game_over_check(pet):
    # Check game over conditions
    if pet["hunger"] >= 100:
        print("\n❌ Your pet became too hungry. Game Over!")
        return True
    if pet["happiness"] <= 0:
        print("\n❌ Your pet became too sad. Game Over!")
        return True
    return False

# -------- Main Program --------

print("🐶 Welcome to the Virtual Pet Simulator 🐶")
pet_name = input("Name your pet: ")

# Initialize pet attributes
pet = {
    "name": pet_name,
    "hunger": 50,
    "happiness": 50
}

print(f"\nYou are now taking care of {pet['name']} ❤️")

while True:
    print("\n----- Menu -----")
    print("1. Feed the pet")
    print("2. Play with the pet")
    print("3. Check pet status")
    print("4. Quit")

    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        feed_pet(pet)
    elif choice == "2":
        play_with_pet(pet)
    elif choice == "3":
        check_status(pet)
    elif choice == "4":
        print("\n👋 Thanks for playing! Goodbye!")
        break
    else:
        print("\n⚠ Invalid choice. Please select a valid option.")

    # Apply automatic changes after each action
    apply_time_effects(pet)
    keep_values_in_range(pet)

    # Check if game should end
    if game_over_check(pet):
        break
