#This file handles logic related to user input, printing recommendations, and loading data

import pandas as pd
from recommendation_engine import Hash
from recommendation_engine import Graph
from recommendation_engine import RecommendationEngine, Perfume
#
def parsePricing(price_selecting):
    #create map of price ranges
    priceMap = {
        "1": (0,50),
        "2": (50, 100),
        "3": (100, 150),
        "4": (150, 200),
        "5": (200, float('inf'))
    }
    price_indexes = price_selecting.split(',')
    #marks the first value of the tuple as the minimum price and the second value of the tuple the max price
    minPrice = min(priceMap[index][0] for index in price_indexes if index in priceMap)
    maxPrice = max(priceMap[index][1] for index in price_indexes if index in priceMap)
    return minPrice, maxPrice


def get_user_preferences():
    user_name = input("Begin by entering your name: ").title()
    print(f"Hello, {user_name}! Let's get started!")

    #scent note selection
    notes_options = ["Woody", "Floral", "Bergamot", "Vanilla", "Tobacco"]
    notes = ''
    while not notes:
        print("\nSelect preferred scent notes:")
        for i, option in enumerate(notes_options, 1):
            print(f"{i}. {option}")
        notes_selections = input("Select numbers (separated by commas): ")
        selected_notes = [notes_options[int(index) - 1] for index in notes_selections.split(',') if index.isdigit() and 0 < int(index) <= len(notes_options)]
        if not selected_notes:
            print("Invalid input. Please select valid numbers corresponding to the scent notes.")
        else:
            notes = ', '.join(selected_notes)

    #price range selection
    price_options = ["Under $50", "$50 - $100", "$100 - $150", "$150 - $200", "Above $200"]
    print("\nSelect your preferred price range:")
    for i, option in enumerate(price_options, 1):
        print(f"{i}. {option}")
    price_selections = input("Select numbers (separated by commas): ")
    minPrice, maxPrice = parsePricing(price_selections)

    #occasion selection
    occasion_options = ["Daytime", "Nightime","Anytime"]
    occasions = ''
    while not occasions:
        print("\nSelect the occasion:")
        for i, option in enumerate(occasion_options, 1):
            print(f"{i}. {option}")
        occasion_selections = input("Select numbers (separated by commas): ")
        selected_occasion = [occasion_options[int(index) - 1] for index in occasion_selections.split(',') if
                             index.isdigit() and 0 < int(index) <= len(occasion_options)]
        if not selected_occasion:
            print("Invalid input. Please select valid numbers corresponding to the occasions.")
        else:
            occasions = ', '.join(selected_occasion)

    #recommendation method selection
    method = input("\nSelect recommendation method: graph/hash: ").strip().lower()
    #invalid selection handling
    while method not in ['graph', 'hash']:
        print("Method must be either 'graph' or 'hash'. Please try again.")
        method = input("Select recommendation method: graph/hash: ").strip().lower()
    return user_name, notes, (minPrice, maxPrice), occasions, method

def user_recommendation(perfumes):
    graph = Graph()
    hashTable = Hash()

    for perfume in perfumes:
        graph.add_perfume(perfume)
        hashTable.add_perfume(perfume)

    #shared notes, implement logic

    return graph, hashTable

# ...

def main():
    print("Welcome to Eau de AI: Perfume Finder")

    # load data
    # installed pip and utilizing pandas to load data from xcsl data set
    file_path = 'perfumeedited3.xlsx'
    perfume_df = pd.read_excel(file_path)
    #test to see if load and read work for first five rows
    #print(perfume_df.head()) #just to see if file is in the directory and loaded propeorly using pandas #comment this out
    #print(perfume_df['Price'].head())

    #perfume objects
    perfumes = [Perfume(row['Name'], row['Notes'], row['Price'], row['Occasion'].split(','))
                for index, row in perfume_df.iterrows()]
    #initialize recommendation engine
    engine = RecommendationEngine(perfumes)

    while True:
        user_name, notes, (minPrice, maxPrice) , occasions, method = get_user_preferences()
        #get recommendations
        recommendations = engine.recommend(notes, minPrice,maxPrice, occasions, method)

        #show the recommendations
        if recommendations:
            print("\nIt's a match! Here are the perfumes we found for you:")
            max_name_length = max(len(perfume.name) for perfume in recommendations)
            name_col_width = max(max_name_length, len("Perfume Name"))
            header = f"{'Perfume Name':<{name_col_width}} {'Price':>5m}"
            print(header)
            print('-' * (name_col_width + 11))
            for perfume in recommendations:
                print(f"{perfume.name:<{name_col_width}} ${perfume.price:>.2f}")
        else:
            print("No recommendations could be made based on the selected criteria, sorry!")

        repeat = input("\nWould you like to use our perfume finder again? (yes/no): ").strip().lower()
        if repeat == 'yes':
            continue
        elif repeat == 'no':
            print("\nThank you for using Eau de AI. Please take a moment to fill out our survey.")
            satisfaction = input("How satisfied are you with the recommendations? (1-5): ")
            print(f"\nYou rated us a {satisfaction}. Thank you for your feedback, bye!")
            break
        else:
            print("Invalid input. Exiting...")
            break

if __name__ == "__main__":
    main()
