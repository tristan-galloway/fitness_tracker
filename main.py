from os import system, name
from time import sleep
from workout import Biking, Swimming, Running
from firestore import push_event, delete_event, get_all_events, print_all_events

# define our clear function
def clear():
	# for windows
	if name == 'nt':
		_ = system('cls')
	# for mac and linux(here, os.name is 'posix')
	else:
		_ = system('clear')

def main_menu():
    choice = 0

    while choice != 4:
        # Display the menu for the user to make a selection
        print("""Main Menu:
        [1] Record workout
        [2] Remove workout
        [3] View workout history
        [4] Exit""")
        print("Enter a selection.")
        choice = int(input("> "))

        if choice == 1:
            record_workout()
        elif choice == 2:
            remove_workout()
        elif choice == 3:
            workout_history()
        elif choice == 4:
            print("Thank you for using the fitness app.")

def record_workout():
    clear()
    print("""What workout would like to record:
    [1] Running
    [2] Biking 
    [3] Swimming""")
    print("Enter a selection.")
    choice = int(input("> "))

    if choice == 1:
        # Build Running Event.
        clear()
        duration = input("How long in minutes did it take you to run? ")
        clear()
        distance = input("How far in miles did you go? ")
        push_event("Running", distance, duration)
    elif choice == 2:
        # Build Biking Event.
        clear()
        duration = input("How long in minutes did it take you to bike? ")
        clear()
        distance = input("How far in miles did you go? ")
        push_event("Biking", distance, duration)
    elif choice == 3:
        # Build Swimming Event.
        clear()
        duration = input("How long in minutes did it take you to swim? ")
        clear()
        distance = input("How many laps did you swim? ")
        push_event("Swimming", distance, duration)

def remove_workout():
    events = get_all_events('workoutsCollection')
    print_all_events()
    # Get the number they want to remove and convert to a index value
    choice = int(input('Enter the event you\'d like to remove: ')) - 1
    event_to_remove_id = events[choice]['id']
    delete_event('workoutsCollection', event_to_remove_id)

def workout_history():
    clear()
    print_all_events()

def run():
    clear()
    print("Welcome to the fitness tracker app.")
    sleep(2)
    main_menu()

# Run the program.
run()