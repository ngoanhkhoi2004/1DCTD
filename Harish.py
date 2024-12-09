import time #ensures dialogues do not appear too fast

#Print welcome message
print("Welcome to Tank Simulator!")

def get_callsign():
    while True:
        Callsign = input("Enter your desired callsign! [Maximum of 10 characters and no spaces]:").strip() #eliminates space before and after callsign
        time.sleep(1)
        if len(Callsign)>10:
            print("Can't you follow rules soldier? You've exceeded the maximum characters! Try again.")
        elif " " in Callsign: #spaces in  callsign
            print("That's 10 push ups soldier! I said no spaces! Try again.")
        elif not Callsign: #empty callsign
            print("Give me a name soldier! Try again!")
        else: #correct name
            return f'Private Anderson "{Callsign}" Mactavish'

#Welcome message with name
player_name = get_callsign()
print(f"Get moving, {player_name}! There's no time to waste!")
time.sleep(1)

def show_tank_info(tank_name): #dictionary of tank info
    tank_info = {
        "1" : {
            "Name" : "M4 Sherman Firefly",
            "Description" : "AKA the Mayfly, it was one of the tanks present at Normandy that was able to penetrate the notoriously thick German Tiger I tank's armor."
        },
        "2" : {
            "Name" : "A22 Infantry Tank Mk. IV",
            "Description" : "AKA the Churchill, it was built to travel on unexpected terrain conditions allowing it to provide on the ground support to troops where other tanks could not reach."
        },
        "3" : {
            "Name" : "Panzer V Panther",
            "Description" : "With a long-barreled, high-powered gun that could fire six rounds per minute and a storage capacity of 79 rounds of 75mm ammunition, this was one opponent you didn't want to make an appearance on the battlefield."
        }
    }

    tank = tank_info.get(tank_name)
    if tank:
        print(f"\nTank: {tank["Name"]}")
        print(f"Description : {tank["Description"]}\n")
    else:
        print("Stop wasting my time! Pick a valid option!\n")

#main function to make the user choose and display info about the tanks
def choose_tank():
    while True:
        print("\nChoose a tank to learn more about it.\n")
        time.sleep(1)
        print("1. M4 Sherman Firefly")
        time.sleep(0.5)
        print("2. A22 Infantry Tank Mk. IV")
        time.sleep(0.5)
        print("3. Panzer V Panther")
        time.sleep(0.5)

        #get user input
        choice = input(f"1.[TANK INFO]Make your selection (1,2 or 3), {player_name}! \n2.[TANK SELECTION]Type '4' to confirm your tank for battle \033[1mAFTER\033[0m you have read about each tank:").strip().lower()


        if choice == "1" or choice == "2" or choice == "3":
            #show tank info and wait for exit command
            while True:
                time.sleep(2)
                show_tank_info(choice)
                back_to_menu = input("Type '11' to return to the tank options page: ").strip().lower()
                if back_to_menu == "11":
                    print("\nReturning to Tank INFO page...\n")
                    time.sleep(2)
                    break
                else:
                    time.sleep(1)
                    print("Invalid command! Type '11' to return to Tank INFO page...")

        elif choice == "11":
            time.sleep(1)
            print("\nReturning to tank options...\n")
        elif choice == "4":
            time.sleep(1)
            selected_tank = input("Enter your option (1,2 or 3):").strip()
            if selected_tank in ["1","2","3"]:
                time.sleep(1)
                print(f"\nYou have selected {["M4 Sherman Firefly", "A22 Infantry Tank Mk. IV", "Panzer V Panther"][int(selected_tank)-1]}")
                time.sleep(1.3)
                print(f"There is no turning back now... Good luck with your mission {player_name}. If we don't end war, war will end us...")
                break
            else:
                time.sleep(1)
                print("\nThat's 20 push ups soldier!")
                time.sleep(2)
                print("\nReturning to the menu.")
        else:
            time.sleep(1)
            print("\nStop wasting my time! Pick a valid option!\n")
            time.sleep(1)
            print("\nReturning to tank options...\n")
            time.sleep(3)

#Main selection page
choose_tank()

time.sleep(1.5)
print(f"You are on your way to the frontlines, {player_name}!")
time.sleep(1)
print("Good luck soldier...")

#setting up scenario
time.sleep(3)
print("\nMaking your way into the battlegrounds, you can't contain your excitement as this what you have been training for all your life...\n")
time.sleep(3)
print("\nAll of a sudden, you hear a loud \033[1mBANG\033[0m to your left!\n")


#prompt user for input
def player_action():
    while True:
        print("\nWhat do you want to do? You can turn left (1) or keep moving (2).\n")
        nextAction = input(">").strip()

        # First path: Turning left
        if nextAction == '1':
            time.sleep(1)
            print("\nYou chose to turn left...\n")
            time.sleep(1)
            print("You spot a burning tank and several destroyed vehicles ahead.")
            time.sleep(2)
            print("As you approach, your commander warns of potential mines in the area.")
            time.sleep(2)

            while True:
                print("\nDo you want to proceed cautiously through the suspected minefield (1) or find another route (2)?")
                second_action = input(">").strip()
                if second_action == "1":
                    time.sleep(1)
                    print("\nYou proceed cautiously, scanning for mines.")
                    time.sleep(2)
                    print("Your crew detects and disarms a mine just in time, clearing the path for allied tanks.")
                    time.sleep(2)
                    print("Your bravery earns you the respect of your team, and you push forward to the next objective.")
                elif second_action == "2":
                    time.sleep(1)
                    print("\nYou take a detour to avoid the minefield.")
                    time.sleep(2)
                    print(
                        "Unfortunately, the detour takes longer, and the enemy uses the time to reinforce their position.")
                    time.sleep(2)
                    print("\033[1mThis makes your next battle significantly harder...\033[0m")
                    break
                else:
                    print("Invalid option. Please type '1' or '2'.")



        # Second path: Moving forward
        elif nextAction == '2':
            time.sleep(1)
            print("\nYou decide to press forward, sticking to your main objective.\n")
            time.sleep(2)
            print("Suddenly, you encounter an enemy tank column blocking your path.")
            time.sleep(2)


            while True:
                print("\nDo you want to ambush them from cover (1) or call in artillery support (2)?")
                ambush_action = input(">").strip()
                if ambush_action == "1":
                    time.sleep(1)
                    print("\nYou position your tank in cover and fire the first shot.")
                    time.sleep(2)
                    print("Your ambush catches the enemy by surprise, and you destroy two tanks before they can respond.")
                    time.sleep(2)
                    print("However, a surviving tank escapes to warn the main enemy force.")
                    time.sleep(2)
                    print("\033[1mThe enemy will be on high alert for the remainder of your mission...\033[0m")
                elif ambush_action == "2":
                    time.sleep(1)
                    print("\nYou call in artillery support, raining destruction on the enemy column.")
                    time.sleep(2)
                    print("The artillery obliterates the tanks, clearing the way.")
                    time.sleep(2)
                    print("However, the loud barrage alerts nearby enemy forces to your presence.")
                    break
                else:
                    print("Invalid option. Please type '1' or '2'.")
        #if they choose something else for first path
        else:
            print("Invalid option. Please type '1' or '2'.")
            continue #Re-prompt for valid input



        # Moral Choice: Abandoned Enemy Tank
        time.sleep(2)
        print("\nYou push forward and discover an abandoned enemy tank.")
        time.sleep(2)

        while True:
            print("Do you want to salvage it for supplies (1) or destroy it to prevent enemy use (2)?")
            salvage_action = input(">").strip()
            if salvage_action == "1":
                time.sleep(1)
                print("\nYour crew salvages ammunition and repair tools from the tank, boosting your combat readiness.")
                time.sleep(2)
                print("Your team feels confident as you prepare for the next battle.")
            elif salvage_action == "2":
                time.sleep(1)
                print("\nYou destroy the tank to ensure the enemy can't use it against you.")
                time.sleep(2)
                print("However, this decision leaves your crew feeling uneasy about missed opportunities.")
                break
            else:
                print("Invalid option. Please type '1' or '2'.")

        # Final Objective
        time.sleep(2)
        print("\nYou reach the final objective: an enemy stronghold fortified with tanks and infantry.")
        time.sleep(2)


        while True:
            print("Do you want to lead a direct assault with your tank (1) or coordinate with allied forces for a pincer attack (2)?")
            final_action = input(">").strip()
            if final_action == "1":
                time.sleep(1)
                print("\nYou lead the charge, driving straight into the heart of enemy defenses.")
                time.sleep(2)
                print("Your tank destroys several enemy vehicles, but you're overwhelmed by concentrated fire.")
                time.sleep(2)
                print("\033[1mYour bravery inspires others, but you die in the process. Mission failed.\033[0m")
                exit()
            elif final_action == "2":
                time.sleep(1)
                print("\nYou coordinate with allied tanks, executing a flawless pincer maneuver.")
                time.sleep(2)
                print("The enemy stronghold falls, and your mission is a resounding success.")
                time.sleep(2)
                print(f"\033[1mCongratulations, {player_name}! You are promoted to Captain for your heroic efforts.\033[0m")
                #greatest ending
                break
            else:
                print("Invalid option. Please type '1' or '2'.")

player_action()
