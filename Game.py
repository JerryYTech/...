import random

class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.inventory = []

    def take_damage(self, damage):
        self.health -= damage

    def heal(self, amount):
        self.health += amount

    def add_to_inventory(self, item):
        self.inventory.append(item)

    def remove_from_inventory(self, item):
        if item in self.inventory:
            self.inventory.remove(item)

class Room:
    def __init__(self, name, description, items=None, monster=None):
        self.name = name
        self.description = description
        self.items = items if items else []
        self.monster = monster

    def add_item(self, item):
        self.items.append(item)

    def remove_item(self, item):
        if item in self.items:
            self.items.remove(item)

class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description

class Monster:
    def __init__(self, name, health, damage):
        self.name = name
        self.health = health
        self.damage = damage

    def take_damage(self, damage):
        self.health -= damage

def combat(player, monster):
    print(f"A wild {monster.name} appears!")
    while player.health > 0 and monster.health > 0:
        player_attack = random.randint(1, 20)  # Simulating a dice roll
        monster_attack = random.randint(1, 20)  # Simulating a dice roll
        if player_attack >= monster_attack:
            damage = random.randint(10, 20)
            monster.take_damage(damage)
            print(f"You hit the {monster.name} for {damage} damage!")
        else:
            damage = random.randint(5, 15)
            player.take_damage(damage)
            print(f"The {monster.name} hits you for {damage} damage!")
    if player.health <= 0:
        print("You were defeated.")
    else:
        print(f"You defeated the {monster.name}!")

def main():
    player_name = input("Enter your name: ")
    player = Player(player_name)
    print(f"Welcome, {player.name}!")

    # Define rooms
    room1 = Room("Room 1", "You are in a dark room.")
    room2 = Room("Room 2", "You are in a dimly lit corridor.")
    room3 = Room("Room 3", "You are in a spacious hall.", [Item("Sword", "A shiny sword")])
    room4 = Room("Room 4", "You are in a dusty attic.", [Item("Potion", "A healing potion")], Monster("Goblin", 50, 10))

    # Connect rooms
    room1.add_item(Item("Key", "A rusty key"))
    room1.add_item(Item("Coin", "A golden coin"))
    room1.add_item(Item("Candle", "A half-burnt candle"))

    room2.add_item(Item("Book", "An old book"))

    room3.add_item(Item("Shield", "A sturdy shield"))

    # Start game loop
    current_room = room1
    while True:
        print("\n" + "=" * 50)
        print(current_room.description)
        print("Items in the room:")
        for item in current_room.items:
            print(f"- {item.name}: {item.description}")
        if current_room.monster:
            combat(player, current_room.monster)
            if player.health <= 0:
                print("Game over.")
                break
            else:
                print("You continue exploring...")
        command = input("Enter a command (e.g., 'look', 'take key', 'go north'): ").lower()
        if command == "look":
            pass  # Implement look functionality
        elif command.startswith("take"):
            item_name = command.split(" ", 1)[1]
            for item in current_room.items:
                if item.name.lower() == item_name:
                    player.add_to_inventory(item)
                    current_room.remove_item(item)
                    print(f"You take the {item.name}.")
                    break
            else:
                print("Item not found.")
        elif command.startswith("go"):
            direction = command.split(" ", 1)[1]
            print(f"You go {direction}.")
            # Implement room navigation
        elif command == "quit":
            print("Quitting game.")
            break
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()
