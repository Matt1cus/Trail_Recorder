import json
import os

data_file = "hikes.json" #how we will store hikes in json

def load_hikes():
    """Read hikes from file. Return empty list if file not found or no file yet."""
    if not os.path.exists(data_file):
        return [] #this returns the empty list
    with open(data_file, "r") as f:
        return json.load(f) #loads the file

def save_hikes(hikes):
    """Write the full list of hikes to file."""
    with open(data_file, "w") as f:
        json.dump(hikes, f, indent=2) #dumps json

#commands

def add_hike(hikes):
    """Ask the user about a hike and add it to list"""
    print("\n--- Log New Hike ---")
    name = input("Hike name: ")
    date = input("Date (YYYY-MM-DD): ")
    distance = float(input("Distance (miles): "))
    duration = int(input("Duration  (minutes): ")) #these are the stuff the user inputs in, potentially replaced through GPS?

    hike = {
        "name": name,
        "date": date,
        "distance_mi": distance,
        "duration_min": duration
    }
    hikes.append(hike)
    save_hikes(hikes)
    print(f"Saved '{name}'! \n") #appending data to json file.

def list_hikes(hikes):
        """Print every hike, then the total miles recorded"""
        if not hikes:
            print("\nNo hikes logged in yet")
            return

        print("\n--- Your Hikes! ---") #hikes
        for number, hike in enumerate(hikes, start=1):
            print(
                f"{number}. {hike['date']} {hike['name']}"
                f"{hike['distance_mi']} mi {hike['duration_min']} min"
            )
        total_miles = sum(hike['distance_mi'] for hike in hikes)
        print(f"\nTotal: {len(hikes)} hikes, {total_miles:.1f} miles \n")

#main menu

def main():
    hikes = load_hikes()

    while True:
        print("Trail Recorder")
        print("1. Add a hike")
        print("2. List all hikes")
        print("3, Quit")
        choice = input("Enter your choice: ")

        if choice == "1":
            add_hike(hikes)
        elif choice == "2":
            list_hikes(hikes)
        elif choice == "3":
            print("Happy Hikes!")
            break
        else:
            print("Invalid choice. Please enter your choice again.")


# Only run main when file is run directly (no importation)
if __name__ == "__main__":
    main()



