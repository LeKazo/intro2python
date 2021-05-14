import random

chinese_food = ["House of China", "Imperial Garden", "Golden Hunan", "Main Moon", "Chinatown Inn"]
japanese_food = ["Izumi", "Mizu", "Tokyo House", "Sakura", "Asuka"]
fast_food = ["Wendys", "Taco Bell", "Rasian Canes"]
casual_food = ["Sheetz", "Ihop", "Inner Circle"]
buffets = ["Golden Corral", "Chinese Buffet"]
bbq = ["Mission BBQ", "Outback Steakhouse", "Texas Roadhouse"]
italian_food = ["Salvatores", "Scarsellas", "Nicolinni's"]

cuisine_choice_responses = ["Excellent Choice. ", "Mmmmm... That's a delicious idea. ", "Oh yes. I'm getting fat tonight. ", "One of my favs. ", "My belly is happy. "]

random_response = random.choice(cuisine_choice_responses)

def welcome():
    print("Hello there, looks like you are having trouble deciding what to eat. I'll help.")
    cuisine_choice = input("Please select what type of cuisine you prefer: \n1 = Chinese\n2 = Japanese\n3 = Fast Food\n4 = Casual Food \n5 = Buffets \n6 = BBQ\n7 = Italian\n8 = I Don't Know!\nPlease enter a number: ")
    if cuisine_choice == "1":
        print(random_response+"You should eat at: "+random.choice(chinese_food))
    elif cuisine_choice == "2":
        print(random_response+"You should eat at: "+random.choice(japanese_food))
    elif cuisine_choice == "3":
        print(random_response+"You should eat at: "+random.choice(fast_food))
    elif cuisine_choice == "4":
        print(random_response+"You should eat at: "+random.choice(casual_food))
    elif cuisine_choice == "5":
        print(random_response+"You should eat at: "+random.choice(buffets))
    elif cuisine_choice == "6":
        print(random_response+"You should eat at: "+random.choice(bbq))
    elif cuisine_choice == "7":
        print(random_response+" You should eat at: "+random.choice(italian_food))
    elif cuisine_choice == "8":
        my_random_choice = random.randint(1,8)
        if my_random_choice == 1:
            print(random_response+"You should eat at: "+random.choice(chinese_food))
        elif my_random_choice == 2:
            print(random_response+"You should eat at: "+random.choice(japanese_food))
        elif my_random_choice == 3:
            print(random_response+"You should eat at: "+random.choice(fast_food))
        elif my_random_choice == 4:
            print(random_response+"You should eat at: "+random.choice(casual_food))
        elif my_random_choice == 5:
            print(random_response+"You should eat at: "+random.choice(buffets))
        elif my_random_choice == 6:
            print(random_response+"You should eat at: "+random.choice(bbq))
        else:
            print(random_response+" You should eat at: "+random.choice(italian_food))
    else:
        print("\033[1;32;47m You did not select a number. Please try again. ")
        #https://ozzmaker.com/add-colour-to-text-in-python/
        welcome()

welcome()