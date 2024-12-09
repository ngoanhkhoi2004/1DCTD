# Define the game state
game_state = {
    "morality": 10,
    "team_morale": 10,
    "resources": 5,  # Medkits or supplies
    "survivors_saved": 0
}


# Helper functions
def make_choice(prompt, choices):
    print(prompt)
    for i, choice in enumerate(choices, 1):
        print(f"{i}. {choice['text']}")

    while True:
        try:
            selection = int(input("Choose an option: "))
            if 1 <= selection <= len(choices):
                return choices[selection - 1]
            else:
                print("Invalid choice, try again.")
        except ValueError:
            print("Enter a number corresponding to your choice.")


def update_game_state(choice):
    global game_state
    game_state["morality"] += choice.get("morality", 0)
    game_state["team_morale"] += choice.get("team_morale", 0)
    game_state["resources"] += choice.get("resources", 0)
    game_state["survivors_saved"] += choice.get("survivors_saved", 0)


def show_stats():
    print("\n--- Current Stats ---")
    print(f"Morality: {game_state['morality']}")
    print(f"Team Morale: {game_state['team_morale']}")
    print(f"Resources: {game_state['resources']}")
    print(f"Survivors Saved: {game_state['survivors_saved']}\n")


# Scenarios
def scenario1():
    print("\nScenario 1: Under Fire")
    choice = make_choice(
        "Your unit is pinned down by enemy fire, and several soldiers are injured. What do you do?",
        [
            {
                "text": "Rush to the injured under heavy fire, using your medical supplies to save as many as possible (-2 resources, +2 morality, +1 survivors_saved).",
                "morality": 2, "resources": -2, "survivors_saved": 1},
            {
                "text": "Wait for the firing to die down, then help those you can (-1 morality, +1 team_morale, +1 survivors_saved).",
                "morality": -1, "team_morale": 1, "survivors_saved": 1},
            {"text": "Stay back to avoid risk and preserve supplies for later (-2 morality, +1 resources).",
             "morality": -2, "resources": 1}
        ]
    )
    update_game_state(choice)
    show_stats()


def scenario2():
    print("\nScenario 2: Enemy Captives")
    choice = make_choice(
        "You find a group of wounded enemy soldiers. What do you do?",
        [
            {"text": "Treat their wounds, adhering to your principles (+3 morality, -1 resources).",
             "morality": 3, "resources": -1},
            {"text": "Provide basic aid and move on (+1 morality).",
             "morality": 1},
            {"text": "Leave them, focusing on your unit's needs (-2 morality, +1 resources).",
             "morality": -2, "resources": 1}
        ]
    )
    update_game_state(choice)
    show_stats()


def scenario3():
    print("\nScenario 3: Desperate Plea")
    choice = make_choice(
        "A soldier begs for more pain relief than you have available. What do you do?",
        [
            {"text": "Give them your last dose, knowing others might suffer later (+2 team_morale, -1 resources).",
             "team_morale": 2, "resources": -1},
            {"text": "Explain the situation and ration the dose (+1 morality, -1 team_morale).",
             "morality": 1, "team_morale": -1},
            {"text": "Refuse and save the supplies for critical injuries (-2 team_morale, +1 resources).",
             "team_morale": -2, "resources": 1}
        ]
    )
    update_game_state(choice)
    show_stats()


def determine_ending():
    print("\n--- Mission Complete ---")
    if game_state["morality"] > 12 and game_state["survivors_saved"] >= 3:
        print("You a Hero of Compassion. You upheld your principles and saved many lives!")
    elif game_state["morality"] < 5:
        print("Futile Survival. You strayed from your principles, and the cost was heavy....")
    else:
        print("Balanced Victory! You made tough choices and helped your team survive!")


# Intro
def start_game():
    print(
        "Welcome Soldier, I see you have selected to play as the medic!\nBe warned, the path of the medic is not one for the faint hearted!")
    print("You are roleplaying as James Doakes, You are commited to nonviolence and a strong moral against killing.")
    print("You enlisted in the army as a combat medic determined to save lves rather than take them.")
    print("Remember your own morales and make choices based on what you think is right!")
    print("At the end depending on your choices, you will awarded different statuses!\nLet's Begin!")
    scenario1()
    scenario2()
    scenario3()
    determine_ending()


start_game()
