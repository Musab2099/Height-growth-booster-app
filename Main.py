# -----------------------------
# Height Growth Booster App (Beginner Version)
# -----------------------------

# 1. Import JSON so we can save and load progress
import json



# 2. Make a function to load old data (sleep, exercise, food logs)
#    If no file exists yet, return an empty list
def load_data():
    try:
        # Try to open the file in read mode
        with open("data.json", "r") as file:
            data = json.load(file)  # Load JSON data
            return data  # Return the loaded data
    except (FileNotFoundError, json.JSONDecodeError):
        # If the file doesn't exist, return an empty list
        # If there's a JSON decode error, also return an empty list
        return []

#    - add the dictionary to the data list
# Function to save new data
def save_data(data, filename="data.json"):
    try:
        # Open the file in write mode
        with open(filename, "w") as file:
            # Use json.dump to save the data
            json.dump(data, file, indent=4)
    except IOError as e:
        # Handle any I/O errors
        print(f"Error saving data: {e}")

def log_habits(filename="data.json"):
    # load existing data
    data = load_data()  # Load existing data from the file

    # use input() to ask user questions
    name = input("What's your name: ")
    age = input("How old are you: ")
    hobbies = input("What are your hobbies: ")
    sleep_duration = input("How many hours do you sleep: ")
    stretch_duration = input("How many minutes do you stretch: ")
    exercise_duration = input("How many minutes do you exercise: ")
    food = input("What kind of food do you eat: ")
    # create a dictionary with all answers
    user_data = {
    "Name": name,
    "Age": age,
    "Hobbies": hobbies,
    "Sleep": sleep_duration,
    "Stretch": stretch_duration,
    "Exercise": exercise_duration,
    "Food": food
}
    # append it to the data list
    data.append(user_data)
    # save the updated data back to the file
    save_data(data, filename)  # Save the updated data to the file

    print("Your habits have been logged successfully!")


# 5. Make a function to show progress
def show_progress(filename="data.json"):
    """Calculates averages, checks goals, and prints a report."""
    data  = load_data(filename)
    if not data:
        print("No data available. Please log your habits first.")
        return
    
    total_sleep = 0
    total_stretch = 0
    total_exercise = 0
    total_entries = 0

   # Loop through all entries and calculate totals
    for log in data:
        try:
            # Convert string inputs to numbers for calculation
            total_sleep += float(log.get("Sleep", 0))
            total_stretch += float(log.get("Stretch", 0))
            total_exercise += float(log.get("Exercise", 0))
            total_entries += 1
        except (ValueError, TypeError):
            # This skips any log where the numbers aren't valid
            print("Warning: Invalid data found in log, skipping entry.")

    if total_entries == 0:
        print("No valid data found to create a report.")
        return
    
    # --- Print Averages ---
    print("\n--- Your Progress Report ---")
    print(f"Average Sleep: {total_sleep / total_entries:.1f} hours")
    print(f"Average Stretch: {total_stretch / total_entries:.1f} minutes")
    print(f"Average Exercise: {total_exercise / total_entries:.1f} minutes")
    print("-----------------------------")

    # --- Check Goals for the Most Recent Day ---
    print("--- Latest Log Analysis ---")
    latest_log = data[-1] # Get the most recent log
    try:
        latest_sleep = float(latest_log.get("Sleep", 0))
        latest_stretch = int(latest_log.get("Stretch", 0))

        #Define your goals here
        Sleep_goal = 8 
        Stretch_goal = 10

        #Check sleep goal 
        if latest_sleep >= Sleep_goal:
            print(f"✅ Great job! You hit your sleep goal of {Sleep_goal} hours.")
        else:
            print(f"❌ Keep trying! You got {latest_sleep} hours of sleep, aiming for {Sleep_goal}.")
            print("💡 Tip: A consistent sleep schedule, even on weekends, can work wonders!")

        #Check stretch goal
        if latest_stretch >= Stretch_goal:
            print(f"✅ Awesome! You met your stretching goal of {Stretch_goal} minutes.")
        else:
            print(f"❌ You missed your stretching goal by a little bit.")
            print("   💡 Tip: Try stretching right after you wake up to start your day fresh.")

    except (ValueError, TypeError):
        print("Could not analyze the latest log due to invalid number format.")
        print("--------------------------------\n")


# 6. Main loop (the app menu)
def main():
    """The main function to run the application menu."""
    while True:
        print("\n--- Height Growth Booster App ---")
        print("1. Log Habits")
        print("2. View Progress report")
        print("3. Quit")

        
        choice = input("Enter your choice (1-3): ")

        if choice == "1":
            log_habits()
        elif choice == "2":
            show_progress()
        elif choice == "3":
            print("\nGreat work today! Keep up the healthy habits. Goodbye! 👋")
            break
        else:
            print("\nInvalid choice. Please select 1, 2, or 3.")

# 7. Run the app
if __name__ == "__main__":
    main()
