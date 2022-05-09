from clear import clear 
from colors import color
import colors, os, sys, json, cakes, math

clear()
color("Welcome to Cake Baker", colors.blue)
color("Here you will bake, eat and sell cakes\n", colors.cyan)

def home():
  color("Home screen\n", colors.white)
  color("(1) Bake Cake", colors.blue)
  color("(2) Sell Cake", colors.brown)
  color("(3) Eat Cake", colors.tan)
  color("(4) Quit", colors.dark_red)
  color("\nWhat do you want to do? ", colors.bold)
  pick = input("> ")
  if (pick == "1") or (pick.lower().startswith("b")):
    bakeCakes()
  elif (pick == "2") or (pick.lower().startswith("s")):
    sellCakes()
  elif (pick == "3") or (pick.lower().startswith("e")):
    eatCake()
  elif (pick == "4") or (pick.lower().startswith("q")) or ("quit" in pick.lower()):
    clear()
    quit(color("You left the Cake Shop.\nSee you soon!", colors.green))

def eatCake():
  pass

def sellCakes():
  pass

def bakeCakes():
  clear()
  allCakes()

cakes = json.loads(cakes.cakesList)

def allCakes():
  for i in range(len(cakes["cakes"])):
    price = cakes["cakes"][i]["layers"] * 6.3 + 29 / 3 // 1
    #price = round(price, 1)
    print(f'{cakes["cakes"][i]["name"]} - {cakes["cakes"][i]["description"]} - Layers: {cakes["cakes"][i]["layers"]} ${price}')

for i in range(len(cakes["cakes"])):
  #print(cakes["cakes"][i])
  pass

allCakes()

home()