#This file handles logic related to user input, printing recommendations, and loading data

import pandas as pd
from recommendation_engine import Hash
from recommendation_engine import Graph
from recommendation_engine import RecommendationEngine, Perfume
def parsePricing(price_selecting):
    priceMap = {
        "1": (0,50),
        "2": (50, 100),
        "3": (100, 150),
        "4": (150, 200),
        "5": (200, float('inf'))
    }
    price_indexes = price_selecting.split(',')
    minPrice = min(priceMap[index][0] for index in price_indexes if index in priceMap)
    maxPrice = max(priceMap[index][1] for index in price_indexes if index in priceMap)
    return minPrice, maxPrice


def get_user_preferences():
    print("Welcome to Eau de AI: Perfume Finder")
    user_name = input("Begin by entering your name: ")
    print(f"Hello, {user_name}! Let's get started!")

    #scent note selection
    notes_options = ["Woody", "Floral", "Bergamot", "Vanilla", "Tobacco"]
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
    minPrice, maxPrice = parsePricing(price_selections)

    #occasion selection
    occasion_options = ["Daytime", "Nightime","Anytime"]
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
    # load data
    # installed pip and utilizing pandas to load data from xcsl data set
    file_path = 'perfumeedited3.xlsx'
    perfume_df = pd.read_excel(file_path)
    #test to see if load and read work for first five rows
    #print(perfume_df.head()) #just to see if file is in the directory and loaded propeorly using pandas #comment this out
    #print(perfume_df['Price'].head())

    #Perfume objects
    perfumes = [Perfume(row['Name'], row['Notes'], row['Price'], row['Occasion'].split(','))
                for index, row in perfume_df.iterrows()]

    # Initialize recommendation engine
    engine = RecommendationEngine(perfumes)

    user_name, notes, (minPrice, maxPrice) , occasions, method = get_user_preferences()

    # Get recommendations
    recommendations = engine.recommend(notes, minPrice,maxPrice, occasions, method)

    # show the recommendation
    if recommendations:
        for perfume in recommendations:
            print(f"Recommended Perfume: {perfume.name}")
    else:
        print("No recommendations could be made based on the selected criteria.")


if __name__ == "__main__":
    main()
