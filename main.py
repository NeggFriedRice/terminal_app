import random, time, sys

class BeyBlade:
    def __init__(self, name):
        self.name = name
        self.owner = ""
        self.strength = self.statRand()
        self.strength_modifier = self.modifierRand()
        self.speed = self.statRand()
        self.speed_modifier = self.modifierRand()
        self.stamina = self.statRand()
        self.stamina_modifier = self.modifierRand()
        self.total_stats = self.get_total_stats()
        self.money = 200
        self.playing = True
        self.win_counter = 0
        self.rounds_to_play = 3
        self.upgrades_count = 1
        self.opponents_count = 1
        self.shop_visit = 1
        
    def modifierRand(self):
        return (random.randint(10, 20)) / 10
    
    def statRand(self):
        return random.randint(85, 100)
    
    def get_total_stats(self):
        return round(self.strength * self.strength_modifier + self.speed * self.speed_modifier + self.stamina * self.stamina_modifier)

class Battle:
    def battle_lobby(self, opponent):
        delay_print("Do you want to battle? (Yes or No)\n")            
        battle_yes_no = input()
        if battle_yes_no.lower() == "yes":
            Battle.battle(player, opponent)
        elif battle_yes_no.lower() == "no":
            print("")
        else:
            print("That is not a valid selection")

    def battle(self, opponent):
        self.rounds_to_play -= 1
        self.opponents_count += 1
        player.upgrades_count += 1
        if self.get_total_stats() > opponent.get_total_stats():
            print(f"{self.name} has won the battle!")
            player.shop_visit += 1
            player.win_counter += 1
            win_money = random.randint(25, 65)
            player.money += win_money
            print(f"You won ${win_money} for winning this round!")
        elif self.get_total_stats() == opponent.get_total_stats():
            player.shop_visit += 1
            self.rounds_to_play += 1
            print("It's a draw! No money awarded! You'll need to play an extra round!")
        else:
            lose_money = random.randint(5, 25)
            player.shop_visit += 1
            player.money -= lose_money
            print(f"{self.name} has lost the battle!")
            print(f"You give ${lose_money} for losing this round! :(")

class Opponent(BeyBlade):
    name_list = [
        "Ash Ketchum", 
        "Spock", 
        "Taylor Swift", 
        "Hagrid", 
        "Ron Weasley", 
        "John Howard",
        "Captain America",
        "Dwight Schrute",
        "Michael Scott",
        "Michael Cera",
        "Danny DeVito",
        "Edward Scissorhands",
        "Britney Spears"
        ]
    def __init__(self, name):
        stats_list = [
            player.strength,
            player.speed,
            player.stamina,
        ]
        super().__init__(name)
        player.opponents_count -= 1
        if player.rounds_to_play == 2:
            self.strength = max(stats_list) * (1 + (random.randint(15, 30) / 100))
        elif player.rounds_to_play == 1:
            self.strength = max(stats_list) * (1 + (random.randint(22, 30) / 100))

class Upgrades:
    # Show upgrades and cost
    strength_random_price = random.randint(12, 30)
    speed_random_price = random.randint(12, 30)
    stamina_random_price = random.randint(12, 30)

    def show_upgrades():
        print(f''' ** Welcome to the UPGRADES shop! **
[A] Buy STRENGTH stat upgrade: {Upgrades.strength_random_price} dollars
[B] Buy SPEED stat upgrade: {Upgrades.speed_random_price} dollars
[C] Buy STAMINA stat upgrade: {Upgrades.stamina_random_price} dollars

You can only upgrade once before each battle!''')
        player.shop_visit -= 1

    def buy_upgrade(input):
        if player.upgrades_count >= 1:
            if input.upper() == "A":
                player.strength += random.randint(45, 65)
                print("You bought a STRENGTH upgrade!")
                player.upgrades_count -= 1
                player.shop_visit = 0
                player.money -= Upgrades.strength_random_price
            elif input.upper() == "B":
                player.speed += random.randint(45, 65)
                print("You bought a SPEED upgrade!")
                player.upgrades_count -= 1
                player.shop_visit = 0
                player.money -= Upgrades.speed_random_price
            else:
                player.stamina += random.randint(45, 65)
                print("You bought a STAMINA upgrade!")
                player.upgrades_count -= 1
                player.shop_visit = 0
                player.money -= Upgrades.stamina_random_price
        else:
            print("You don't have any upgrade slots available!")

class Dialogue:
  
    def intro():
        welcome_message = "Welcome to the 2023 Battle BeyBlade Bonanza!\n"
        delay_print(welcome_message)
        delay_print("Before we get started, could we please have your name for registration?\n")
        player.owner = input()
        delay_print(f"Thank you for registering {player.owner.capitalize()}! We are so glad to have you here!\nAs per the tournament rules, you will be renting one of our Tournament BeyBlades!\n")

    def name_beyblade():
        delay_print("What would you like to name your BeyBlade?\n")

    def present_beyblade(self):
        delay_print(f"Here is your Tournament BeyBlade ~ {self.name.capitalize()} ~ with a total power of {self.total_stats}!\n")
        if self.strength_modifier > self.speed_modifier and self.strength_modifier > self.stamina_modifier:
            delay_print(f"It appears that your BeyBlade favours STRENGTH upgrades!\n")
        elif self.speed_modifier > self.stamina_modifier:
            delay_print(f"It appears that your BeyBlade favours SPEED upgrades!\n")
        else:
            delay_print(f"It appears that your BeyBlade favours STAMINA upgrades!\n")
    
    def beyblade_stats():
        print(f"Your BeyBlade stats:\nStrength: {player.strength}\nSpeed: {player.speed}\nStamina: {player.stamina}\n\n(Stat modifiers are hidden)\nYou have {player.upgrades_count} upgrade slot available!\n")

    def end_game():

        pass
class Menu:
    def menu():
        while player.playing == True:
            Menu.hud()
            choice = input("")
            if choice == "1":
                Dialogue.beyblade_stats()
            elif choice == "2":
                if player.shop_visit > 0:
                    Upgrades.show_upgrades()
                else:
                    print("Sorry, the shop has closed for the day!")
            elif choice == "3":
                if player.opponents_count > 0:
                    opponent = Opponent(random.choice(Opponent.name_list))
                    delay_print(f"Your opponent is {opponent.name}. Their BeyBlade has a total power of {opponent.get_total_stats()}.\n")
                    Battle.battle_lobby(player, opponent)
                else:
                    print(f"You have to beat {opponent.name} (Total power: {opponent.get_total_stats()}) first before battling someone else!")
                    Battle.battle_lobby(player, opponent)
            elif choice.upper() == "A" or choice.upper() == "B" or choice.upper() == "C":
                Upgrades.buy_upgrade(choice)
            else:
                print("That's not a valid selection")

    def hud():
        print(f'''===================================================================
Rounds left: {player.rounds_to_play}   |   Total BeyBlade power: {player.get_total_stats()}   |   Money: {player.money}''')
        print(f'''[1] Check BeyBlade Stats | [2] Go to Upgrade Store | [3] Battle
===================================================================''') 
    
def delay_print(s):
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.01)

# Main
player = BeyBlade("")
Dialogue.intro()
Dialogue.name_beyblade()
player.name = input()
Dialogue.present_beyblade(player)
Menu.menu()


