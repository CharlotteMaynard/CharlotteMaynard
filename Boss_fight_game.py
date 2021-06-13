
from time import sleep
import random

#upload 2

# Charelor boss health
charelor_health = 1000
new_health = charelor_health
if new_health <= 0:
    print("Charelor is dead! congratulations!")

# player health
player_health = 1000
new_player_health = player_health
if new_player_health <= 0:
    print("You have died!")
###########################################################

#player energy
player_energy = 5
new_player_energy = player_energy
####

HEALTH_POTION_COUNT = 0
new_hp_count = HEALTH_POTION_COUNT

SUPER_POTION_COUNT = 0
new_sp_count = SUPER_POTION_COUNT


# player dmg values
posion_dmg = 200

# boss dmg values
boss_melee_attack = 100
boss_deadly_blow_attack = 200
boss_heal_amount = 100

# empty list containing a list of all the attacks/potions used.

player_attacks_used = [""]





#######################################

def start_game():
    print("Welcome adventurer to Boss Fight!")
    sleep(1)
    print("Before you go into battle please open this chests which will give you a random assortment of potions!...")
    sleep(1)
    random_chest()
    sleep(1)
    see_attack_values()
    sleep(1)
    see_potion_values()
    sleep(1)
    print("Good luck!")
    sleep(1)



def random_chest():

    global HEALTH_POTION_COUNT
    global SUPER_POTION_COUNT
    global new_sp_count
    global new_hp_count
    random_health_potion = random.randint(1, 6)
    random_sp_potion = random.randint(1,3)
    open_chest = input("Please press 1 to open the chest!..")
    if open_chest == "1":
        new_hp_count = new_hp_count + random_health_potion
        new_sp_count = new_sp_count + random_sp_potion
        sleep(1)
        print ("You now have: \n", new_hp_count, " Health potions!\n", new_sp_count, " Super potions!")


def see_attack_values():
    yes_or_no = input("Would you like to see your attack stats? if so please press 1")

    if yes_or_no == "1":
        sleep(1)
        print("Melee attack:  50 damage")
        sleep(1)
        print("Poison attack:  200 damage")
    else:
        return


def see_potion_values():
    yes_or_no = input("Would you like to see your potion stats? if so please press 1: ")

    if yes_or_no == "1":
        print("Health potion:  Heals for 100 health points")
        sleep(1)
        print("Super potion:   Your next hit will be doubled! (If it does not miss!..)")

    else:
        return


def Charelor():
    global charelor_health
    charelor_health = 1000


################################################################################
def which_boss():
    global boss_name

    boss_input = input("""Please choose a boss to battle (enter a number):
                      Charelor (1)
                      Sunshar  (2)
                      Ugnor(3)
                         """)

    if boss_input == "1":
        boss_name = Charelor
        sleep(2)
        print("you have chosen to fight Charelor!")

    if (boss_input == "2"):
        boss_name = Sunshar
        print("you have chosen to fight Sunshar!")

    if (boss_input == "3"):
        boss_name = Ugnor
        print("you have chosen to fight Ugnor!")


####################################
#boss fight function. loops until either the player or the boss has died.

def boss_fight():
    global boss_name
    global new_player_health
    global new_health
    global new_player_energy

    if boss_name == Charelor:
        while new_player_health > 0 or new_health > 0:
            if new_player_health > 0:
                sleep(1)
                choose_attack()
                sleep(2)
            if new_player_health <= 0:
                player_dead()
                print("Thank you for playing!")
                break
            if new_health > 0:
                sleep(1)
                boss_attack()
                sleep(2)
            if new_health <= 0:
                boss_dead()
                print("Thank you for playing!")
                break


#############################################################################
#functions when the player of the boss dies

def player_dead():
    global new_player_health

    if new_player_health <= 0:
        print("You have died!")


def boss_dead():
    global new_health

    if new_health <= 0:
        print("Charelor is dead! congratulations!")


#########################################################################


# attacks for player

def melee_attack():
    chance = random.randint(0, 100)
    global fingal_health
    global new_health
    global new_player_energy
    global player_attacks_used


    if chance <= 20:  # there is a 20% chance to miss this hit.
        print("melee attack missed! you miss a turn..")
        player_attacks_used.append("melee_attack")
        return

    if player_attacks_used[-1] != "sp":       # if the last used attack was not a super potion then carry out normal melee attack
        new_health = new_health - 50
        sleep(2)
        print("""melee attack inflicted
                 Charelor health - 50
                 health is now""", new_health)
        player_attacks_used.append("melee_attack")

    if player_attacks_used[-1] == "sp":
            new_health = new_health - 100          # if the last used attack was a super potion then melee attack damage is doubled
            sleep(2)
            print("""melee attack inflicted with a super potion in affect!
                     Charelor health - 100
                     health is now""", new_health)
            player_attacks_used.append("melee_attack")      # add used attack/potion to end of the list
            return




def poision_hit():
    chance = random.randint(0, 100)
    global new_health
    global posion_dmg
    global player_attacks_used

    if chance <=40:                # 40% chance to miss
        print("poison hit missed!.. you miss a turn...")
        return

    if boss_name == Charelor:
        if player_attacks_used[-1] != "sp":
            new_health = new_health - posion_dmg
            sleep(2)
            if new_health < 0:
                new_health = 0
        print("posion hit inflicted!\n Charelor's health is now", str(new_health + (posion_dmg / 2)))
        sleep(1)
        print ("Charelor's health is now", new_health)
        player_attacks_used.append("poision_hit")
        return new_health

    if player_attacks_used[-1] == "sp":
        new_health = new_health - (poison_dmg*2)
        sleep(2)
        if new_health < 0:
            new_health = 0
    print("""Poison attack inflicted with a Super Potion in affect!
             Charelor health - 400
             Charelor's health is now: """, new_health)



###########################################################################

#item for players to use

def use_item():
    chance = random.randint(0, 100)
    global new_player_health
    global new_hp_count
    global HEALTH_POTION_COUNT
    global SUPER_POTION_COUNT
    global new_sp_count
    global player_attacks_used

    item_requested = input("""Please choose which item you would like to use!:
                              health potion (1)
                              energy potion (2)
                              super hit potion (3)
                              go back (4)     
                              """)
    if item_requested == "1":
        if new_hp_count <=0:      # if the player chooses item 1 and they have run out then let them know
            print("sorry you can't use this item")
            return use_item()
        else:
            if chance <=20:
                new_hp_count = new_hp_count - 1
                print("SMASH!...you dropped your health potion... it has no effect\n You now have: " , new_hp_count, "health potions left")
                return
        new_hp_count = new_hp_count - 1      # takes 1 item from their inventory amount
        new_player_health = new_player_health + 100
        print ("""you have used a health potion!
                   your new health is now: """, new_player_health , " you now have: ", new_hp_count
                ," health potions left")

    if item_requested == "3":
        if new_sp_count <=0:
            print("sorry you can't you this item")
            return use_item()
        else:
            new_sp_count = new_sp_count - 1
            print("""you have used a super potion!
                     your next attack, if it does not miss, will be doubled!""")
            player_attacks_used.append("sp")

    if item_requested == "4":    # go back option
        choose_attack()


#############################################################


# attack for boss


def boss_melee():
    chance = random.randint(0, 100)
    global player_health
    global new_player_health


    if chance <=25:
        print("Charelor missed their melee attack!..")
        return

    if boss_name == Charelor:
        sleep(2)
        new_player_health = new_player_health - boss_melee_attack
        if new_player_health < 0:
            new_player_health = 0
        print("""Charelor has inflicted a melee attack!
                  your health is now: """, new_player_health)


def boss_deadly_blow():
    chance = random.randint(0, 100)
    global player_health
    global new_player_health

    if chance <=35:
        print("Charelor missed deadly blow!...")
        return


    if boss_name == Charelor:
        sleep(2)
        new_player_health = new_player_health - boss_deadly_blow_attack
        if new_player_health < 0:
            new_player_health = 0
        print("""Charelor has inflicted a deadly blow!
                  your health is now:""", new_player_health)


def boss_heal():
    chance = random.randint(0, 100)
    global new_health
    global boss_heal_amount


    if chance <=40:
        print("Charelor tried to heal himself but missed!")
        return

    if boss_name == Charelor:
        new_health = new_health + boss_heal_amount
        print("""Charelor has healed itself by 100 health points!
                  Charelor's health is now: """, new_health)


#####################################################################

# boss attack chooses from lists


def boss_attack():
    if boss_name == Charelor:
        print("Charelor is preparing an attack!")

    chance = random.randint(0, 100)

    if chance <= 30:  # this means that these attacks have a 30% chance to be casted. they can still miss.
        low_chance_boss_list = [boss_heal]  # choose from this list
        random.choice(low_chance_boss_list)()
    else:
        boss_list = [boss_melee, boss_deadly_blow]
        random.choice(boss_list)()

####################################################################################

# player choose attack function

def choose_attack():
    item_or_attack = input("""Please choose whether you want to use an item or cast an attack (enter a number 1/2):
                              item (1)
                              attack (2)
                              """)

    if item_or_attack == "1":
        use_item()

    else:
        attack_input = input("""Please choose an attack (enter a number 1-3):
                                melee attack (1)
                                posion hit (2)
                                """)

        if attack_input == "1":
            print("Inflicting melee attack on Charelor!")
            melee_attack()

        if attack_input == "2":
            print("Inflicting poison attack on Charelor!")
            poision_hit()


###########################################################################


# game playing out
print("Welcome to boss fight!")

start_game()
which_boss()
sleep(2)

boss_fight()

