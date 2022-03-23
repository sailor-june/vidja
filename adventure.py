import random
name = input('what is thy name, traveler? ' )
hero_hp = 100
bad_id = random.randint(1,9)
initiative = 0
 
if bad_id == 1:
  bad_name = "rat"
elif bad_id == 2:
  bad_name = "pig"
elif bad_id == 3:
  bad_name = "goblin"
elif bad_id == 4:
  bad_name = "mean cat"
elif bad_id == 5:
  bad_name = "hobogoblin"
elif bad_id == 6:
  bad_name = "Derek"
elif bad_id == 7:
  bad_name = "centaur"
elif bad_id == 8:
  bad_name = "stump"
elif bad_id == 9:
  bad_name = "lich king"
else:
   bad_name = "missingno."




bad_hp = bad_id * 6



print("A wild", bad_name, " appears!")

def combat():
  global hero_hp
  global bad_hp

  print("your hp: ", hero_hp)
  print("enemy hp: ", bad_hp)
  print('what will you do, ', name,  '?')
  print("1 = attack, 2 = surrender")
  initiative = int(input())
 

  if initiative == 1:
    print(name, " swings wildly!")
    print(bad_name, " lunges toward you!")
    get_badhit = (bad_id * random.randint(1,6))
    get_herohit = (5* random.randint(1,6))
    bad_hp = bad_hp - get_herohit
    hero_hp = hero_hp - get_badhit
    print (name, " did ", get_herohit, " damage!")
    if get_herohit >= 25:
      print(" a critical hit!")
    print (bad_name, " did", get_badhit," damage!")
    initiative = 0


  if initiative == 2:
      print('A shameful display!')
      print(bad_name, " swings with all their might!")
      print (badname, " hits for critical damage")
      print("your hp: ", hero_hp)
      print("enemy hp: ", bad_hp)
      hero_hp = 0

while initiative == 0 and hero_hp > 0 and bad_hp > 0:
  combat()


if hero_hp <= 0:
  print("You have been defeated, slain by a ", bad_name, ". F in the chat.")

if hero_hp <= 0 and bad_hp<=0:
  print("As you fall to the ground bleeding, your only comfort is the sight of the dreaded ", bad_name, "Lying slain before you. Rest in peace, oh noble one.")

if hero_hp > 0 and bad_hp <= 0:
  print("Victory is yours! The ", bad_name, "has been defeated! Rest well, brave adventurer.")
