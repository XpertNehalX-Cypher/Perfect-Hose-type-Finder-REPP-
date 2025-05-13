import time

house_types = {
    "low_budget": ["Tiny Houses", "Cabins/Cottages", "Shipping Container/Prefab Homes", "Farmhouses"],
    "mid_high_budget": ["Mansions", "Farmhouses", "Apartments/Condos", "Modern Houses", 
                        "Beach Houses", "Townhouses", "Victorian/Historic Homes"]
}

try:
    price_min = float(input("Enter the minimum price of the house (€): "))
    price_max = float(input("Enter the maximum price of the house (€): "))
    num_people = int(input("Enter the number of people: "))

    if price_min < 0 or price_max < 0 or num_people <= 0:
        print("Please enter only positive values.")
    elif price_max <= 50000 and num_people <= 5:
        print("\nProcessing...")
        for msg in ["Finding Your Perfect Fit", "Checking Connection", "Connecting...", "Searching..."]:
            print(msg)
            time.sleep(0.8)
        print("FOUND!\n")
        print("According to REPP AI, the best home types for you are:")
        print(", ".join(house_types["low_budget"]))
    elif price_max > 50000:
        print("\nProcessing...")
        for msg in ["Finding Your Perfect Fit", "Checking Connection", "Connecting...", "Searching..."]:
            print(msg)
            time.sleep(0.8)
        print("FOUND!\n")
        print("According to REPP AI, the best home types for you are:")
        print(", ".join(house_types["mid_high_budget"]))
    else:
        print("No match found. Please try again with different values.")

except ValueError:
    print("Invalid input. Please enter numbers only.")


