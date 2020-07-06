# refactor code making it more modular
# create CoffeeMachine Class
class CoffeeMachine:

    # initial states
    water = 400
    milk = 540
    beans = 120
    disp_cup = 9
    money = 550
    current_state = None  # keep track of last action
    coffee_type = None  # keep track of last order 

    def turn_on_machine(self):
        while True:
            # update current state i.e. get input from user
            self.get_action()
            # five states of our coffee machine
            if self.current_state == "buy":
                self.make_order()
            elif self.current_state == "fill":
                self.fill_resource()
            elif self.current_state == "take":
                self.take_money()
            elif self.current_state == "remaining":
                self.display_remaining()                   
            elif self.current_state == "exit":
                break

    def get_action(self):
        self.current_state = input("Write action (buy, fill, take, remaining, exit): ")

    def make_order(self):
        self.coffee_type = input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, " +
                                         "back - to main menu: ")
        if self.coffee_type == "1" and self.water >= 250:
            self.making_coffee()
            self.water -= 250
            self.beans -= 16
            self.money += 4
            self.disp_cup -= 1
        elif self.coffee_type == "2" and self.water >= 350:
            self.making_coffee()
            self.water -= 350
            self.milk -= 75
            self.beans -= 20
            self.money += 7
            self.disp_cup -= 1
        elif self.coffee_type == "3" and self.water >= 200:
            self.making_coffee()
            self.water -= 200
            self.milk -= 100
            self.beans -= 12
            self.money += 6   
            self.disp_cup -= 1 
        elif self.coffee_type == "back":
            self.get_action()
        else:
            self.not_enough_water()

    def making_coffee(self):
        print("I have enough resources, making you a coffee!")

    def not_enough_water(self):
        print("Sorry, not enough water!")

    def fill_resource(self):
        self.water += int(input("Write how many ml of water do you want to add: "))
        self.milk += int(input("Write how many ml of milk do you want to add: "))
        self.beans += int(input("Write how many grams of coffee beans do you want to add: "))
        self.disp_cup += int(input("Write how many disposable cups of coffee do you want to add: "))

    def display_remaining(self):
        print(f"""
        The coffee machine has: 
        {self.water} of water
        {self.milk} of milk
        {self.beans} of beans
        {self.disp_cup} of disposable cups
        ${self.money} of money
        """)

    def take_money(self):
        print(f"I gave you ${self.money}")
        self.money = 0  # all money are taken

# create new instance              
agape = CoffeeMachine()
agape.turn_on_machine()
