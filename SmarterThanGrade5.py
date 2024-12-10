#ARE YOU SMARTER THAN A 5TH GRADER

import turtle
import time
import sys
import subprocess


#List of 10 questions and respective answers
questions = [
    {
    "Question": "What is War?",
    "Options": ["1. A way to solve problems nicely",
                "2. A peaceful talk",
                "3. A fight between countries",
                "4. A fun game"],
    "Answer": "3"
},
{
    "Question": "Why is peace better than war?",
    "Options": ["1. Because everyone is happy",
                "2. Because people dont get hurt",
                "3. Because friends can play together",
                "4. All of the above"],
    "Answer": "4"
},
    {
    "Question": "Which country stopped the war in World War II?",
    "Options": ["1. The Moon",
                "2. The United States",
                "3. Atlantis",
                "4. Disneyland"],
    "Answer": "2"
    },
    {
    "Question": "Why do we try to avoid wars?",
    "Options": ["1. Because they are loud",
                "2. Because they are messy",
                "3. Because people can get hurt",
                "4. Because they are too short"],
    "Answer": "3"
    },
    {
    "Question": "What can we do instead of fighting?",
    "Options": ["1. Talk and listen",
                "2. Shout loudly",
                "3. Hide and seek",
                "4. Build a fort"],
    "Answer": "1"
    },
    {
    "Question": "What does peace mean?",
    "Options": ["1. Everyone getting along",
                "2. A quiet place",
                "3. Eating pizza",
                "4. Winning a race"],
    "Answer": "1"
    },
    {
    "Question": "How can we show kindness to others?",
    "Options": ["1. Sharing toys",
                "2. Saying nice words",
                "3. Helping someone in need",
                "4. All of the above"],
    "Answer": "4"
    },
    {
    "Question": "Why is it important to say sorry?",
    "Options": ["1. It makes us happy",
                "2. It shows we care",
                "3. It fixes mistakes",
                "4. All of the above"],
    "Answer": "4"
    },
    {
    "Question": "What should you do if someone is upset?",
    "Options": ["1. Ignore them",
                "2. Make fun of them",
                "3. Be kind and help",
                "4. Run away"],
    "Answer": "3"
    },
    {
    "Question": "What can we do to make the world a better place?",
    "Options": ["1. Be mean to others",
                "2. Clean up trash",
                "3. Help people in need",
                "4. Options 2 and 3 only"],
    "Answer": "4"
    },
]

# Setup the turtle screen for the game visuals

# Function to display the question and its options on the screen
def display_question(t, question, options):
    t.clear()  # Clear page
    t.penup()  # Lift the mouse to move without drawing
    t.goto(-350, 200)  # Move to the starting position for the question text
    t.write(question, align="left", font=("Arial", 18, "bold"))  # Write the question in bold

    # Set the vertical position for the first choice
    y_offset = 150

    # Loop through each option and display it below the question
    for option in options:
        t.goto(-350, y_offset)  # Move to the next line for the option
        t.write(option, align="left", font=("Arial", 16, "normal"))  # Write the options
        y_offset -= 30  # Move down for the next option


# Function to display the player's score on the screen
def display_score(t, score, total):
    t.clear()  # Clear the previous score from screen
    t.penup()  # Lift the mouse to move without drawing
    t.goto(-350, -200)  # Move to the position for displaying the score
    t.write(f"Score: {score}/{total}", align="left", font=("Arial", 16, "bold"))  # Display the score in the format "Score: X/Total"

# Initialize the screen and turtles for questions and score

screen = turtle.Screen()  # Creating a screen on turtle for game to run on
screen.setup(750,750)
screen.title("Are You Smarter Than a 5th Grader?")  # Adding the title of the game
screen.bgcolor("lightgreen")  # Set the background color of the screen, green for war theme, light for ease of reading  # Return the screen so we can use it later  # Call the function to set up the screen

# Create a turtle for displaying questions
question_turtle = turtle.Turtle()  # Create a turtle object for question text
question_turtle.hideturtle()  # Hide the turtle shape so it doesn't appear on the screen
question_turtle.speed(0)  # Set the turtle speed to immediate

# Create a turtle for displaying the score
score_turtle = turtle.Turtle()  # Create another turtle object for score text
score_turtle.hideturtle()  # Hide the turtle shape for this turtle as well
score_turtle.speed(0)  # Set the turtle speed to immediate

#Start the score at 0
score = 0

# Game loop
for index, q in enumerate(questions): #Start the question numbering from qn 1 instead of python auto qn 0
    display_question(question_turtle, f"Question {index+1}: {q['Question']}", q['Options']) # Display the question and choices

    answer = screen.textinput(f"Question {index+1}", "Your answer (1, 2, 3, or 4):").strip().upper() # Get the chosen answer

    # Check the answer

    if answer == q["Answer"]:
        score += 1


# Show the final score
display_score(score_turtle, score, len(questions))

# Wait for 2 secs before showing the next question
time.sleep(2)

# End of game
question_turtle.clear()
question_turtle.goto(-200, 0)
question_turtle.write(f"Game Over! Final Score: {score}/{len(questions)}", align="left", font=("Arial", 26, "bold"))

#End the code in turtle
turtle.bye()

subprocess.run([sys.executable, 'GamesMain.py'])