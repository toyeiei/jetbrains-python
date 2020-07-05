# initial stocks
water = 400
milk = 540
beans = 120
disp_cup = 9
money = 550

# ask user's action
while True:
    action = input("Write action (buy, fill, take, remaining, exit):")
    if action == "exit":
        break    
    elif action == "buy":
        coffee = input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:")
        if coffee == "1" and water >= 250 and beans >= 16 and disp_cup >= 1:
            print("I have enough resources, making you a coffee!")
            water -= 250
            beans -= 16
            money += 4
            disp_cup -= 1
        elif coffee == "2" and water >= 350 and milk >= 75 and beans >= 20 and disp_cup >= 1:
            print("I have enough resources, making you a coffee!")
            water -= 350
            milk -= 75
            beans -= 20
            money += 7
            disp_cup -= 1
        elif coffee == "3" and water >= 200 and milk >= 100 and beans >= 12 and disp_cup >= 1:
            print("I have enough resources, making you a coffee!")
            water -= 200
            milk -= 100
            beans -= 12
            money += 6   
            disp_cup -= 1 
        elif coffee == "back":
            continue
        else:
            print("Sorry, not enough water!")
    elif action == "fill":
        water += int(input("Write how many ml of water do you want to add: "))
        milk += int(input("Write how many ml of milk do you want to add: "))
        beans += int(input("Write how many grams of coffee beans do you want to add: "))
        disp_cup += int(input("Write how many disposable cups of coffee do you want to add: "))  
    elif action == "take":
        print(f"I gave you ${money}")
        money = 0
    elif action == "remaining":
        # print remaining stocks
        print(f"""
        The coffee machine has:
        {water} of water
        {milk} of milk
        {beans} of coffee beans
        {disp_cup} of disposable cups
        {money} of money
        """)
