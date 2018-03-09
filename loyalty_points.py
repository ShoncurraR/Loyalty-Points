import pickle
import matplotlib.pyplot as plt 

def load():
    try:
        me = pickle.load(open("loyalty.txt", "rb"))
    except EOFError:
        me = []
    return me

def askSave(save):
    ask = input("Do you want to save?\n-->").upper()
    if ask == "Y" or ask == "YES":
        pickle.dump(save, open("loyalty.txt", "wb"))
    elif ask == "N" or ask == "NO":
        print("Okay, maybe next time")
        return
customers = load()
#del customers [0]
#askSave(customers)

print(customers)

print("Welcome to Southern Boots!!")
print("What's your name?")
name = input()
print("Hey " + name + " have you shopped with us before?")
answer = input()

points = 0

if answer == "yes":
    points += 50
    print("Thanks for returning, how many pair of boots have you bought from us?")
    answer = int(input())
    if answer >= 5:
        print("You've have gained 10 loyalty points")
        points += 10
    elif answer <= 5:
        print("You've gained 5 loyalty points and 10% off your next purchase of boots")
        points += 5
    print("Please enter in your information for clerical reasons")
if answer == "no":
    print("Would you like to sign up to catch our big sales and gain points?")
answer = input()
print("Please enter your first and last name")
name = input()
print(" Please enter a vaild email address")
email = input()
print("Thanks for signing up, your next visit you will gain 10 loyalty points for being a new customer.")

customers.append({ 'name': name, 'email': email, 'points': points })

askSave(customers)