def introduction():
    print("Good day, Sir.")
    print("You are the Lieutenant in charge of the offense mission XYZ.")
    print(
        "Your mission is to lead your team to victory against the group of Wakandans who have taken hostage of the President.")
    print(
        "The Wakandans are known for their stealth and strong close combat ability,\nso take that into account when selecting your team and your approach to the mission.\n")


def select_team():
    print("First, you must select your team members.\n")
    print("You have the following soldiers available to choose from:")
    print("1. Sergeant Harish - Stealth expert, great at infiltration and sabotage.")
    print("2. Sergeant Chester  - Close combat specialist, fast and strong.")
    print("3. Corporal Lee - Long-range sniper, skilled at precision shots from a distance.")
    print("4. Sergeant Ng - Tactics and strategy expert, can analyze enemy movement.")
    print("5. Sergeant Khoi - Heavy weapons specialist, great for taking out large groups of enemies.")

    team = []
    while len(team) < 3:
        choice = input("Choose a team member by entering the corresponding number (1-5): ")
        if choice == "1" and "Sergeant Harish" not in team:
            team.append("Sergeant Harish")
        elif choice == "2" and "Sergeant Chester" not in team:
            team.append("Sergeant Chester")
        elif choice == "3" and "Corporal Lee" not in team:
            team.append("Corporal Lee")
        elif choice == "4" and "Sergeant Ng" not in team:
            team.append("Sergeant Ng")
        elif choice == "5" and "Sergeant Khoi" not in team:
            team.append("Sergeant Khoi")
        else:
            print("Invalid choice or already selected. Try again.")
    print(f"\nYour team has been selected: {', '.join(team)}\n")
    return team


def mission_approach(team):
    print("Now that you've selected your team, it's time to plan your approach.")
    print(
        "The Wakandans are known for their stealth and close combat skills, so you must decide how to approach the mission.")
    print("Choose your strategy carefully!\n")
    print("1. Stealth Approach: Infiltrate the Wakandan base quietly to avoid detection.")
    print("2. Direct Assault: Take the fight head-on, using overwhelming force.")
    print("3. Distraction Tactic: Send a small group to distract the enemy while the rest of the team flanks them.")

    approach_choice = input("Enter your strategy choice (1-3): ")

    if approach_choice == "1":
        stealth_approach(team)
    elif approach_choice == "2":
        direct_assault(team)
    elif approach_choice == "3":
        distraction_tactic(team)
    else:
        print("Invalid choice. Mission failed.")
        game_over()


def stealth_approach(team):
    print("\nYou have chosen the Stealth Approach.")
    print("Your team will attempt to infiltrate the Wakandan base quietly.")

    if "Sergeant Harish" in team:
        print(
            "Sergeant Harish uses his stealth skills to disable the security systems, allowing your team to sneak past undetected.")
        print("You successfully infiltrate the base!")
        final_encounter(team)
    else:
        print("Without a stealth expert like Sergeant Harish, your team is detected early!")
        print("The Wakandans ambush you. Mission failed.")
        game_over()


def direct_assault(team):
    print("\nYou have chosen the Direct Assault.")
    print("Your team moves towards the Wakandan base for a full frontal attack.")

    if "Sergeant Khoi" in team and "Sergeant Chester" in team:
        print(
            "Sergeant Khoi's heavy weapons and Sergeant Chester's close combat skills help overpower the Wakandan forces.")
        print("The enemy is forced to retreat. Victory achieved!")
        final_encounter(team)
    else:
        print(
            "Without heavy firepower and close combat specialists, your team struggles against the Wakandans' strength.")
        print("You are overwhelmed and the mission fails.")
        game_over()


def distraction_tactic(team):
    print("\nYou have chosen the Distraction Tactic.")
    print("You send a small group to create a diversion while the rest of the team flanks the enemy.")

    if "Corporal Lee" in team and "Sergeant Ng" in team:
        print("Corporal Lee uses his sniper skills to pick off key targets while Sergeant Ng coordinates the flank.")
        print("The distraction works, and your team successfully defeats the Wakandans!")
        final_encounter(team)
    else:
        print("Without a sniper and strategist, the distraction fails and the enemy counters your plan.")
        print("You are surrounded, and the mission fails.")
        game_over()


def final_encounter(team):
    print("\nYou've successfully infiltrated the Wakandan base and reached the final confrontation.")
    print("Choose your final action to secure victory!")
    print("1. Engage in direct combat with the Wakandan leader.")
    print("2. Use a tactical EMP to disable their weapons and electronics.")
    print("3. Launch explosives to destroy their base.")

    final_choice = input("Enter your choice (1-3): ")

    if final_choice == "1":
        if "Sergeant Chester" in team:
            print("Sergeant Chester engages the Wakandan leader in close combat and defeats him. Victory!")
            game_won()
        else:
            print("Without a close combat specialist, the Wakandan leader overpowers your team. Mission failed.")
            game_over()
    elif final_choice == "2":
        if "Sergeant Ng" in team:
            print("Sergeant Ng uses his strategy to deploy the EMP and disable the enemy's systems.")
            print("The team engages the Wakandan base undetected. Victory!")
            game_won()
        else:
            print("Without a strategist, your EMP plan fails. The Wakandans counterattack. Mission failed.")
            game_over()
    elif final_choice == "3":
        if "Sergeant Khoi" in team:
            print("You launch explosives to destroy their base")
            print("OH NO, YOU KILLED THE PRESIDENT!!!")
            game_over()
        else:
            print("Invalid choice. The mission ends in failure.")
            game_over()


def game_over():
    print("\nThe mission has failed. Better luck next time!")
    exit()


def game_won():
    print(
        "\nMission XYZ was a success! You have led your team to victory against the Wakandans and saved the President!")
    exit()

def main():
    introduction()
    team = select_team()
    mission_approach(team)

main()

