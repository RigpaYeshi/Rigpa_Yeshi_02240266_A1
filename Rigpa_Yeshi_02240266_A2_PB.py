class PokemonBinderManager:
    def __init__(self):
        self.binder = set() 
        self.max_pokedex = 1025
        self.cards_per_page = 64
        self.cards_per_row = 8
    
    def add_card(self, pokedex_num):
        """Add a card to the binder and return its position information"""
        if pokedex_num < 1 or pokedex_num > self.max_pokedex:
            return {"error": f"Pokedex number must be between 1 and {self.max_pokedex}."}
        
        if pokedex_num in self.binder:
            return {
                "page": self._calculate_page(pokedex_num),
                "position": self._calculate_position(pokedex_num),
                "status": "duplicate"
            }
        else:
            self.binder.add(pokedex_num)
            return {
                "page": self._calculate_page(pokedex_num),
                "position": self._calculate_position(pokedex_num),
                "status": "added"
            }
    
    def _calculate_page(self, pokedex_num):
        """Calculate which page a card should be on"""
        sorted_cards = sorted(self.binder)
        if pokedex_num in sorted_cards:
            index = sorted_cards.index(pokedex_num)
        else:
            # Find where it would be inserted
            index = 0
            while index < len(sorted_cards) and sorted_cards[index] <= pokedex_num:
                index += 1
            else:
                index = len(sorted_cards)
        
        return (index // self.cards_per_page) + 1
    
    def _calculate_position(self, pokedex_num):
        """Calculate row and column position on a page"""
        sorted_cards = sorted(self.binder)
        if pokedex_num in sorted_cards:
            index = sorted_cards.index(pokedex_num)
        else:
            # Find where it would be inserted
            index = 0
            while index < len(sorted_cards) and sorted_cards[index] <= pokedex_num:
                index += 1
            else:
                index = len(sorted_cards)
        
        position_in_page = index % self.cards_per_page
        row = (position_in_page // self.cards_per_row) + 1
        column = (position_in_page % self.cards_per_row) + 1
        return f"row {row}, column {column}"
    
    def reset_binder(self):
        """Clear all cards from the binder"""
        self.binder = set()
        return "Binder has been reset."
    
    def view_binder(self):
        """Return current binder contents and statistics"""
        if not self.binder:
            return {
                "contents": "The binder is empty.",
                "total_cards": 0,
                "completion": 0.0
            }
        
        sorted_cards = sorted(self.binder)
        contents = []
        for card in sorted_cards:
            contents.append({
                "pokedex": card,
                "page": self._calculate_page(card),
                "position": self._calculate_position(card)
            })
        
        total_cards = len(self.binder)
        completion = (total_cards / self.max_pokedex) * 100
        
        return {
            "contents": contents,
            "total_cards": total_cards,
            "completion": completion
        }
    
    def score(self):
        """Calculate and return the current score"""
        return len(self.binder)
    
    def exit_program(self):
        """Return exit message with final score"""
        return {
            "message": "Thank you for using the Pokémon Card Binder Manager!",
            "score": self.score()
        }

def display_position_info(info, pokedex_num):
    """Display position information for a newly added card"""
    if "error" in info:
        print(f"Error: {info['error']}")
    else:
        print(f"\nPage: {info['page']}")
        print(f"Position: {info['position']}")
        if info['status'] == "added":
            print(f"Status: Added Pokedex #{pokedex_num}")
        else:
            print(f"Status: Pokedex #{pokedex_num} already exists in binder")

def display_binder_contents(info):
    """Display current binder contents"""
    if isinstance(info['contents'], str):
        print(info['contents'])
    else:
        print("\nCurrent Binder Contents:")
        print("-" * 40)
        for card in info['contents']:
            print(f"Pokedex #{card['pokedex']}:")
            print(f"\tPage: {card['page']}")
            print(f"\tPosition: {card['position']}")
            print("-" * 20)
        
        print(f"\nTotal cards in binder: {info['total_cards']}")
        print(f"% completion: {info['completion']:.1f}%")

def main():
    binder_manager = PokemonBinderManager()
    
    print("\nWelcome to Pokémon Card Binder Manager!")
    
    while True:
        print("\nMain Menu:")
        print("1. Add Pokémon card")
        print("2. Reset binder")
        print("3. View current placements")
        print("4. View score")
        print("5. Exit")
        
        try:
            option = int(input("\nSelect option (1-5): "))
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 5.")
            continue
        
        if option == 1:
            try:
                pokedex_num = int(input("Enter Pokedex number: "))
                result = binder_manager.add_card(pokedex_num)
                display_position_info(result, pokedex_num)
            except ValueError:
                print("Invalid input. Please enter a valid Pokedex number.")
        
        elif option == 2:
            print("\nWARNING: This will erase all cards in your binder!")
            choice = input("Type 'CONFIRM' to reset or 'EXIT' to cancel: ").upper()
            if choice == "CONFIRM":
                print(binder_manager.reset_binder())
            elif choice == "EXIT":
                continue
            else:
                print("Invalid input. No changes made.")
        
        elif option == 3:
            binder_info = binder_manager.view_binder()
            display_binder_contents(binder_info)
        
        elif option == 4:
            print(f"\nCurrent score: {binder_manager.score()} Pokémon cards")
        
        elif option == 5:
            exit_info = binder_manager.exit_program()
            print(f"\n{exit_info['message']}")
            print(f"Final collection score: {exit_info['score']} Pokémon cards")
            break
        
        else:
            print("Invalid option. Please select a number between 1 and 5.")

if __name__ == "__main__":
    main()