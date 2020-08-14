
class CoffeeMachine:

    def __init__(self, water=400, milk=540, coffee=120, money=550, cups=9):
        self.water = water
        self.milk = milk
        self.coffee = coffee
        self.money = money
        self.cups = cups
        self.main()

    def current_state(self):
        print("The coffee machine has:")
        print("%s of water" % self.water)
        print("%s of milk" % self.milk)
        print("%s of coffee beans" % self.coffee)
        print("%s of disposable cups" % self.cups)
        print("$%s of money" % self.money)

    def any_coffee(self, n_water, n_milk, n_coffee, n_cups, n_money):
        if self.water < n_water:
            print("Sorry, not enough water!")
        elif self.milk < n_milk:
            print("Sorry, not enough milk!")
        elif self.coffee < n_coffee:
            print("Sorry, not enough coffee!")
        elif self.cups < n_cups:
            print("Sorry, not enough cups!")
        else:
            self.water -= n_water
            self.milk -= n_milk
            self.coffee -= n_coffee
            self.cups -= n_cups
            self.money += n_money
            print("I have enough resources, making you a coffee!")

    def buy(self):
        coffee_type = input("What do you want to buy? 1 - espresso,"
                            "2 - latte, 3 - cappuccino, back - to main menu:")
        if coffee_type == "back":
            return False
        elif coffee_type == "1":
            self.any_coffee(250, 0, 16, 1, 4)
        elif coffee_type == "2":
            self.any_coffee(350, 75, 20, 1, 7)
        elif coffee_type == "3":
            self.any_coffee(200, 100, 12, 1, 6)

    def fill(self):
        self.water += int(input("Write how many ml of water do you want to add:"))
        self.milk += int(input("Write how many ml of milk do you want to add:"))
        self.coffee += int(input("Write how many grams of coffee beans do you want to add:"))
        self.cups += int(input("Write how many disposable cups of coffee do you want to add:"))

    def take(self):
        print("I gave you $%s" % self.money)
        self.money = 0

    def main(self):
        while True:
            action = input("Write action (buy, fill, take, remaining, exit):")
            if action == "buy":
                if not self.buy():
                    continue
                else:
                    self.buy()
            elif action == "fill":
                self.fill()
            elif action == "take":
                self.take()
            elif action == "remaining":
                self.current_state()
            elif action == "exit":
                break

