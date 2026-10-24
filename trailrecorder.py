import json
import os
from datetime import datetime


#hey its me its recordity ask me anything  I know one thing your hikity, give me your datity,


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
    name = ask_text("Hike name: ")
    date = ask_date("Date (YYYY-MM-DD): ")
    distance = ask_number("Distance (miles): ", 0.1, 999999)
    duration = ask_number("Duration  (minutes): ", 1, 9999999, whole=True) #these are the stuff the user inputs in, potentially replaced through GPS?

    rating = ask_number("Rating (1-5) : ", 1, 5, whole=True)
    notes = input("Notes: (How did it feel?) ")

    print("Weather during the hike: ")
    temp_f = ask_number("Temp (F): ", -40, 130, whole=True)
    wind_mph = ask_number("Wind MPH (mph): ", 0, 100, whole=True)
    rain = ask_for_yes_or_no("Did it rain (y/n): ")
    hike = {
        "name": name,
        "date": date,
        "distance_mi": distance,
        "duration_3min": duration,
        "rating": rating,
        "notes": notes,
        "weather": {"temp_f": temp_f, "wind_mph": wind_mph, "rain": rain},

    }
    hikes.append(hike)
    save_hikes(hikes)
    print(f"Saved '{name}' {make_stars(rating)}\n") #appending data to json file.

def list_hikes(hikes):
        """Print every hike, then the total miles recorded"""
        if not hikes:
            print("\nNo hikes logged in yet")
            return

        print("\n--- Your Hikes! ---") #hikes
        for number, hike in enumerate(hikes, start=1):
            rating = hike.get("rating")
            stars = make_stars(rating) if rating else "unrated"

            weather = hike.get("weather")  # only Day 4+ json files have the data
            if weather:
                rain_text = "rain" if weather["rain"] else "dry"
                weather_text = f"{weather['temp_f']:.0f}F, {weather['wind_mph']:.0f} mph, {rain_text}"
            else:
                weather_text = "no weather"
            print(
                f"{number}. {hike['date']} {hike['name']}"
                f" {hike['distance_mi']} mi {hike['duration_min']} min"
                f" {stars} | {weather_text}"
            )


        total_miles = sum(hike['distance_mi'] for hike in hikes)
        print(f"\nTotal: {len(hikes)} hikes, {total_miles:.1f} miles \n")

# lists the stats of the hike (hikes in V1 do not have this data).
def show_stats(hikes):
    if not hikes:
        print("\nNo hikes logged in yet")
        return

    total_miles = sum(hike['distance_mi'] for hike in hikes)
    total_minutes = sum(hike['duration_min'] for hike in hikes)
    average_distance = total_miles / len(hikes)
    average_pace = total_minutes / total_miles

    longest = max(hikes, key=lambda hike: hike['distance_mi'])

    #gui interface for stats
    print("\n--- Your Stats! ---")
    print(f"Hikes Logged:         {len(hikes)}")
    print(f"Total Distance:       {total_miles:.1f} mi")
    print(f"Average Distance:     {average_distance:.1f} mi")
    print(f"Average pace:         {average_pace:.1f} min/mi ({60 / average_pace:.1f} mph)")
    print(f"Longest Hike:         {longest['name']} ({longest['distance_mi']} mi)")

    rated = [hike for hike in hikes if hike.get("rating")]
    if rated:
        average_rating = sum(hike["rating"] for hike in rated) / len(rated)
        best = max(rated, key=lambda hike: hike["rating"])
        print(f"Average Rating:     {make_stars(average_rating)}")
        print(f"Top-Rated Hike:     {best['name']} ({best['rating']}/5)")
    else:
        print("No ratings recorded - Please rate a hike to see rating stats.")
    print()

#star system for ratings
def make_stars(rating):
    filled = round(rating)
    return "★" * filled + "☆" * (5 - filled)

#make sure that the inputs are correct format text for text, number for number, etc

def ask_text(prompt):
    while True:
        text = input(prompt).strip()
        if text:
            return text
        print("Cannot be empty.")

def ask_number(prompt, min_value, max_value, whole=False): #make sure user enters no. in range
    while True:
        text = input(prompt)
        try:
            value = int(text) if whole else float(text)

        except ValueError:
            print("Please enter a number.")
            continue
        if min_value <= value <= max_value:
            return value
        print(f"Please enter a number between {min_value} and {max_value}.")

def ask_for_yes_or_no(prompt):
    while True:
        answer = input(prompt).strip().lower()
        if answer in ("y", "yes"):
            return True
        if answer in ("n", "no"):
            return False
        print("Please enter yes or no.")

def ask_date(prompt):
    while True:
        text = input(prompt).strip()
        try:
            datetime.strptime(text, "%Y-%m-%d")
            return text
        except ValueError:
            print("Please enter a date, use format YYYY-MM-DD.")


#main menu
def main():
    hikes = load_hikes()

    while True:
        print("Trail Recorder")
        print("1. Add a hike")
        print("2. List all hikes")
        print("3. Stats")
        print("4. Quit")
        choice = input("Enter your choice: ")

        if choice == "1":
            add_hike(hikes)
        elif choice == "2":
            list_hikes(hikes)
        elif choice == "3":
            show_stats(hikes)
        elif choice == "4":
            print("Enjoy Your Hike!")
            break
        else:
            print("Invalid choice. Please enter your choice again.")


# Only run main when file is run directly (no importation)
if __name__ == "__main__":
    main()



