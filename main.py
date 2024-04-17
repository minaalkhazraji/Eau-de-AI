from perfume import Perfume
from graph import Graph
from hash import Hash
def get_user_preferences():
    print("Welcome to Eau de AI: Perfume Finder")
    user_name = input("Begin by entering your name: ")
    print(f"Hello, {user_name}! Let's get started!")

    #scent note selection
    notes_options = ["Woody", "Floral", "Citrus", "Spicy", "Sweet"]
    print("\nSelect preferred scent notes:")
    for i, option in enumerate(notes_options, 1):
        print(f"{i}. {option}")
    notes_selections = input("Select numbers (separated by commas): ")
    selected_notes = [notes_options[int(index) - 1] for index in notes_selections.split(',') if index.isdigit() and 0 < int(index) <= len(notes_options)]
    notes = ', '.join(selected_notes)

    #price range selection
    price_options = ["Under $50", "$50 - $100", "$100 - $150", "$150 - $200", "Above $200"]
    print("\nSelect your preferred price range:")
    for i, option in enumerate(price_options, 1):
        print(f"{i}. {option}")
    price_selections = input("Select numbers (separated by commas): ")
    selected_prices = [price_options[int(index) - 1] for index in price_selections.split(',') if index.isdigit() and 0 < int(index) <= len(price_options)]
    price_range = ', '.join(selected_prices)

    #occasion selection
    occasion_options = ["Casual", "Formal", "Evening", "Sport"]
    print("\nSelect the occasion:")
    for i, option in enumerate(occasion_options, 1):
        print(f"{i}. {option}")
    occasion_selections = input("Select numbers (separated by commas): ")
    selected_occasion  = [occasion_options[int(index) - 1] for index in occasion_selections.split(',') if index.isdigit() and 0 < int(index) <= len(occasion_options)]
    occasions = ', '.join(selected_occasion)

    #recommendation method selection
    method = input("\nSelect recommendation method: 'graph' or 'hash': ")
    #invalid selection handling
    while method not in ['graph', 'hash']:
        print("Method must be either 'graph' or 'hash'. Please try again.")
        method = input("Select recommendation method: 'graph' or 'hash': ")
    return user_name, notes, price_range, occasions, method
def user_recommendation(perfumes):
    graph = Graph()
    hashTable = Hash()

    for perfume in perfumes:
        graph.add_perfume(perfume)
        hashTable.add_perfume(perfume)

    #shared notes, implement logic

    return graph, hashTable



def main():
    get_user_preferences()

if __name__ == "__main__":
    main()