# Initialize the availability of the rooms using a list
import os

rooms = [
    "Room 001", "Room 002", "Room 003", "Room 004",
    "Room 005", "Room 006", "Room 007", "Room 008",
    "Room 009", "Room 010"
]

booked_status = [False] * len(rooms)  # Corresponding booking status for each room

while True:
    # Display the menu
    print("\n--- Simple Hotel Room Booking System ---")
    print("1. View Available Rooms")
    print("2. Book a Room")
    print("3. Checkout (Free a Room)")
    print("4. Exit")
    print("-----------------------------------------")

    # Get user choice
    choice = input("Enter your choice (1-4): ").strip()

    # Handle each choice
    if choice == '1':
        # View available rooms
        print("\nAvailable Rooms:")
        available = False  # To check if at least one room is available

        for i in range(len(rooms)):
            if not booked_status[i]:
                print(f"- {rooms[i]}")
                available = True

        if not available:
            print("No rooms available — all are currently booked.")

    elif choice == '2':
        # Book a room
        room_name = input("Enter the room name you want to book: ").strip().title()

        if room_name in rooms:
            index = rooms.index(room_name)
            if not booked_status[index]:
                booked_status[index] = True
                print(f"You have successfully booked '{room_name}'.")
            else:
                print(f"'{room_name}' is already booked.")
        else:
            print("Room not found. Please enter a valid room name.")

    elif choice == '3':
        # Checkout (free a room)
        room_name = input("Enter the room name you want to checkout (free): ").strip().title()

        if room_name in rooms:
            index = rooms.index(room_name)
            if booked_status[index]:
                booked_status[index] = False
                print(f"You have successfully checked out of '{room_name}'. It is now available.")
            else:
                print(f"'{room_name}' was not booked.")
        else:
            print("Room not found. Please enter a valid room name.")

    elif choice == '4':
        # Exit the system
        print("Exiting the system. Thank you for using Bright Minds Hotel Booking!")
        break

    else:
        # Handle invalid choice
        print("Invalid choice. Please select a valid option (1-4).")
