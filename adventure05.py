import random
import time

hero_hp = 100
encounter = False

badguy = ["rat",
          "j.k. rowling",
          "goblin",
          "mean cat",
          "hobogoblin",
          "Derek",
          "centaur",
          "stump",
          "",
          ]


def get_baddie():
    bad_id = random.randint(0, len(badguy) - 1)
    return bad_id


def slowdown():

    for i in range(2):
        time.sleep(.5)
        print("*", end='')
    time.sleep(.5)
    print('*')
    time.sleep(.5)
    print('')


def get_init():
    global name
    print('what will you do, ', name, """?
        (a)ttack, or (s)urrender """)
    init = input()
    if init == 'a':
        return 1

    elif init == 's':

        return 0
    else:
        print('Invalid!')



## Combat starts here ########              ##########          ###########
def combat():
    global hero_hp
    global name
    encounter = True
    get_baddie()
    bad_id = get_baddie()


    turn = 0
    initiative = 0
    bad_id = get_baddie()
    bad_name = badguy[bad_id]
    bad_hp = bad_id * 6 + 1

    def take_turn(bad_hp, hero_hp, turn, encounter):


        if turn == 0:
            print("A wild ", bad_name, " appears!")
            print("")
            print("your hp: ", hero_hp)
            print("enemy hp: ", bad_hp)
        else:
            print("")
            print("your hp: ", hero_hp)
            print("enemy hp: ", bad_hp)

        initiative = get_init()
        if initiative == 0 :
                initiative = get_init()
        if initiative == 1:
            print(name, " swings wildly!")
            print(bad_name, " lunges toward you!")
            get_badhit = (bad_id * random.randint(1, 6))
            get_herohit = (5 * random.randint(1, 6))
            bad_hp = bad_hp - get_herohit
            if get_herohit >= 25:
                print(" a critical hit!")
            hero_hp = hero_hp - get_badhit
            print(name, " did ", get_herohit, " damage!")
            print(bad_name, " hit for ", get_badhit, " damage!")
            turn += 1
            while bad_hp > 0:
                take_turn(bad_hp,hero_hp,turn, encounter)
            else:
                encounter = False




### i dont think this works yet
        elif initiative == 2:

                print('A shameful display!')
                print(bad_name, " swings with all their might!")
                print(bad_name, " hits for critical damage")
                hero_hp = 0
                print("your hp: 0")
                print("enemy hp: ", bad_hp)
        print("")
        print("your hp: ", hero_hp)
        print(bad_name, "'s hp: ", bad_hp)
        turn += 1
        get_init()



    slowdown()

    while encounter == True:
        take_turn(bad_hp, hero_hp, turn, encounter)
        return encounter

    if encounter == False and hero_hp <= 0:
        print("You have been defeated, slain by a ", bad_name, ". F in the chat.")

        return encounter

    elif encounter == False and hero_hp <= 0 and bad_hp <= 0:
        print("As you fall to the ground bleeding, your only comfort is the sight of the dreaded ", bad_name,
              "Lying slain before you. Rest in peace, oh noble one.")

        return encounter
    if encounter == False and hero_hp > 0 and bad_hp <= 0:
        print("Victory is yours! The ", bad_name, "has been defeated!")

        return encounter









name = input("What is thy name, o wand'rer? ")
if name == "":
    name = input("Speak up! What is thy name? ")

badguy[8] = input (str("And who is thy greatest foe? "))
if badguy[8] == "":
    badguy[8] = input("Speak up! who is thy greatest foe? ")

slowdown()
print("An enemy approaches...")



encounter = True
while encounter == True:
    combat()
else:
    print("is it working????")