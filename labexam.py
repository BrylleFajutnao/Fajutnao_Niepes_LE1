class Game:
    def __init__(self, title, copies=10, cost=10):
        self.title = title
        self.copies = copies
        self.cost = cost

    def __str__(self):
        return self.title

class GameRentalSystem:
    ADMIN_USERNAME = "admin"
    ADMIN_PASSWORD = "adminpass"
    
    def __init__(self):
        self.games = {
            "Tekken 8": {"copies": 10, "cost": 10},
            "Mortal Kombat 1": {"copies": 10, "cost": 10},
            "Street Fighter 6": {"copies": 10, "cost": 10}
        }
        self.users = {}
        self.current_user = None

    def add_game(self, title, copies=0, cost=0):
        if title not in self.games:
            self.games[title] = {"copies": copies, "cost": cost}
            print(f"{title} added to the system with {copies} copies and cost ${cost}.")
        else:
            print(f"{title} already exists in the system.")

    def remove_game(self, title):
        if title in self.games:
            del self.games[title]
            print(f"{title} removed from the system.")
        else:
            print(f"{title} does not exist in the system.")

    def rent_game(self, title):
        if title in self.games:
            game = self.games[title]
            if game["copies"] > 0:
                game["copies"] -= 1
                print(f"{title} rented successfully.")
            else:
                print(f"{title} is out of stock.")
        else:
            print(f"{title} does not exist in the system.")

    def return_game(self, title):
        if title in self.games:
            self.games[title]["copies"] += 1
            print(f"{title} returned successfully.")
        else:
            print(f"{title} does not exist in the system.")

    def display_available_games(self):
        print("Available Games:")
        for title, game in self.games.items():
            if game["copies"] > 0:
                print(f"- {title} (Copies: {game['copies']}, Cost: ${game['cost']})")


    def login(self, username, password):
        if username == self.ADMIN_USERNAME and password == self.ADMIN_PASSWORD:
            self.current_user = username
            print(f"Logged in as '{username}'.")
            self.admin_menu()
        elif username in self.users:
            if self.users[username]["password"] == password:
                self.current_user = username
                print(f"Logged in as '{username}'.")
                self.user_menu()
            else:
                print("Incorrect password.")
        else:
            print("User not found.")
    
    def add_user(self, username, password, is_admin=False):
        if username not in self.users:
            self.users[username] = {"password": password, "is_admin": is_admin}
            print(f"User '{username}' added successfully.")
        else:
            print(f"User '{username}' already exists.")

    def signup(self, username, password):
        if username not in self.users:
            self.add_user(username, password)
            print("Signup successful! Please log in.")
        else:
            print("Username already exists. Please choose another one.")

    def admin_menu(self):
        while True:
            print("\nAdmin Menu:")
            print("1. Add Game")
            print("2. Remove Game")
            print("3. Display Available Games")
            print("4. Logout")
            choice = input("Enter your choice: ")
            if choice == "1":
                title = input("Enter the title of the game: ")
                copies = input("Enter the amount of copies: ")
                cost = input("Enter the cost: ")
                self.add_game(title,copies,cost)
            elif choice == "2":
                title = input("Enter the title of the game: ")
                self.remove_game(title)
            elif choice == "3":
                self.display_available_games()
            elif choice == "4":
                self.current_user = None
                print("Logged out.")
                break
            else:
                print("Invalid choice.")

    def user_menu(self):
        while True:
            print("\nUser Menu:")
            print("1. Rent Game")
            print("2. Return Game")
            print("3. Display Available Games")
            print("4. Logout")
            choice = input("Enter your choice: ")
            if choice == "1":
                title = input("Enter the title of the game you want to rent: ")
                self.rent_game(title)
            elif choice == "2":
                title = input("Enter the title of the game you want to return: ")
                self.return_game(title)
            elif choice == "3":
                self.display_available_games()
            elif choice == "4":
                self.current_user = None
                print("Logged out.")
                break
            else:
                print("Invalid choice.")

if __name__ == "__main__":
    rental_system = GameRentalSystem()

    while True:
        print("\nWelcome to the Game Rental System!")
        print("1. Sign Up")
        print("2. Log In")
        print("3. Exit")
        option = input("Enter your choice: ")

        if option == "1":
            username = input("Enter username: ")
            password = input("Enter password: ")
            rental_system.signup(username, password)
        elif option == "2":
            username = input("Enter username: ")
            password = input("Enter password: ")
            rental_system.login(username, password)
        elif option == "3":
            print("Exiting...")
            break
        else:
            print("Invalid choice.")


  
      
  


    



      




    
