import sys
import subprocess

def menu():
    print("Choose your game:")
    print("1. Saving Private Ryan")
    print("2. Play the Medic Scenario")
    print("3. Fury")

menu()

choice = input("Enter your choice (1-3): ")
if choice == "1":
    subprocess.run(["python", "ZW.py"])
    subprocess.run([sys.executable, 'GamesMain.py'])

elif choice == "2":
    subprocess.run(["python", "Chester.py"])
    subprocess.run([sys.executable, 'GamesMain.py'])

elif choice == "3":
    subprocess.run([sys.executable, 'Harish.py'])
    subprocess.run([sys.executable, 'GamesMain.py'])

else:
    print("Wrong command!")
    menu()

