import turtle

# Questions and answers (geared toward 5-year-olds)
questions = [
    {
        "question": "What is war?",
        "choices": ["A. A way to solve problems nicely",
                    "B. A peaceful talk",
                    "C. A fight between countries",
                    "D. A fun game"],
        "answer": "C"
    },
    {
        "question": "Why is peace better than war?",
        "choices": ["A. Because everyone is happy",
                    "B. Because people don’t get hurt",
                    "C. Because friends can play together",
                    "D. All of the above"],
        "answer": "D"
    },
    {
        "question": "Which country helped stop the war in World War II?",
        "choices": ["A. The Moon",
                    "B. The United States",
                    "C. Atlantis",
                    "D. Candyland"],
        "answer": "B"
    },
    {
        "question": "Why do we try to avoid wars?",
        "choices": ["A. Because they are loud",
                    "B. Because they are messy",
                    "C. Because people can get hurt",
                    "D. Because they are too short"],
        "answer": "C"
    },
    {
        "question": "What can we do instead of fighting?",
        "choices": ["A. Talk and listen",
                    "B. Shout loudly",
                    "C. Hide and seek",
                    "D. Build a fort"],
        "answer": "A"
    },
    {
        "question": "What does peace mean?",
        "choices": ["A. Everyone getting along",
                    "B. A quiet place",
                    "C. Eating pizza",
                    "D. Winning a race"],
        "answer": "A"
    },
    {
        "question": "How can we show kindness to others?",
        "choices": ["A. Sharing toys",
                    "B. Saying nice words",
                    "C. Helping someone in need",
                    "D. All of the above"],
        "answer": "D"
    },
    {
        "question": "Why is it important to say sorry?",
        "choices": ["A. It makes us happy",
                    "B. It shows we care",
                    "C. It fixes mistakes",
                    "D. All of the above"],
        "answer": "D"
    },
    {
        "question": "What should you do if someone is upset?",
        "choices": ["A. Ignore them",
                    "B. Make fun of them",
                    "C. Be kind and help",
                    "D. Run away"],
        "answer": "C"
    },
    {
        "question": "What can we do to make the world a better place?",
        "choices": ["A. Be mean to others",
                    "B. Clean up trash",
                    "C. Help people in need",
                    "D. B and C"],
        "answer": "D"
    },
]

# Setup turtle visuals
def setup_screen():
    screen = turtle.Screen()
    screen.title("Are You Smarter Than a 5th Grader?")
    screen.bgcolor("lightblue")
    return screen

def display_question(t, question, choices):
    t.clear()
    t.penup()
    t.goto(-200, 200)
    t.write(question, align="left", font=("Arial", 16, "bold"))
    y_offset = 150
    for choice in choices:
        t.goto(-200, y_offset)
        t.write(choice, align="left", font=("Arial", 14, "normal"))
        y_offset -= 30

def display_score(t, score, total):
    t.clear()
    t.penup()
    t.goto(-200, -200)
    t.write(f"Score: {score}/{total}", align="left", font=("Arial", 16, "bold"))

# Initialize turtle for questions and score
screen = setup_screen()
question_turtle = turtle.Turtle()
question_turtle.hideturtle()
question_turtle.speed(0)

score_turtle = turtle.Turtle()
score_turtle.hideturtle()
score_turtle.speed(0)

# Game variables
score = 0

# Game loop
for index, q in enumerate(questions, 1):
    # Display the question and choices
    display_question(question_turtle, f"Question {index}: {q['question']}", q['choices'])

    # Get the user's answer
    answer = screen.textinput(f"Question {index}", "Your answer (A, B, C, or D):").strip().upper()

    # Check the answer
    if answer == q["answer"]:
        score += 1
        feedback = "Correct! War is never a good solution."
    else:
        feedback = f"Wrong! The correct answer was: {q['answer']}. Let's always choose peace!"

    # Display feedback on screen
    question_turtle.goto(-200, -50)
    question_turtle.write(feedback, align="left", font=("Arial", 14, "italic"))
    screen.update()

    # Display the score
    display_score(score_turtle, score, len(questions))

    # Wait for a moment before showing the next question
    turtle.time.sleep(3)

# End of game
question_turtle.clear()
question_turtle.goto(-200, 0)
question_turtle.write(f"Game Over! Final Score: {score}/{len(questions)}", align="left", font=("Arial", 24, "bold"))

turtle.done()