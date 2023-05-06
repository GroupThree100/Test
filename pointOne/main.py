from Coctel import Coctel
from CoctelFruit import CoctelFruit

print('"If your type product is "COCTEL CON JUGO DE FRUTAS" type: (1)"')

print('"If your type product is "SHOT DE ALCOHOL" type: (2)"')
typeProduct = int(input('...'))
if typeProduct == 1:
    print("enter 1")
    classCoctel = Coctel()
    classCoctel.name = "COCTEL CON JUGO DE FRUTAS"
    classCoctel.amount = int(input("Type amout of product: "))
    classCoctel.amountAlcohol = int(input("Type amount of alcohol of the shot: "))
    classCoctel.temperature = int(input("Type the temperature when served Shot in grades: "))
    classCoctel.price = int(input("Type price of product: "))
    classCoctel.cost = classCoctel.amount * classCoctel.price 
    
    print("The name of your product is ",classCoctel.name)
    print("The amount of alcohol is ", classCoctel.amountAlcohol,"%")
    print("The temperature of product when was served is ", classCoctel.temperature,"°")
    print("The cost of product is $", classCoctel.cost,".00")
elif typeProduct == 2:
    print("enter 2")
    classCoctelFruit = CoctelFruit()
    classCoctelFruit.name = "COCTEL CON JUGO DE FRUTAS"
    classCoctelFruit.amount = int(input("Type amout of product: "))
    classCoctelFruit.amountAlcohol = int(input("Type amount of alcohol of the shot: "))
    classCoctelFruit.price = int(input("Type price of product: "))
    classCoctelFruit.levelFresH = int(input("Type in days the level of fresh: "))
    if classCoctelFruit.levelFresH == 1:
        classCoctelFruit.cost = classCoctelFruit.amount * classCoctelFruit.price    
        print("classCoctelFruit.cost ",classCoctelFruit.cost)
    elif classCoctelFruit.levelFresH == 2:
        classCoctelFruit.cost = (classCoctelFruit.amount * classCoctelFruit.price)* 0.20
        print("classCoctelFruit.cost ",classCoctelFruit.cost)
    elif classCoctelFruit.levelFresH == 3:
        classCoctelFruit.cost =  (classCoctelFruit.amount * classCoctelFruit.price)* 0.50
        print("classCoctelFruit.cost ",classCoctelFruit.cost)
    elif classCoctelFruit.levelFresH > 3:
        classCoctelFruit.cost =  "No se vende el producto"
        print("classCoctelFruit.cost ",classCoctelFruit.cost)    
    else:
        print("----------------------TYPE DATAS CORRECTS------------------")
    
    print("The name of your product is ",classCoctelFruit.name)
    print("The amount of alcohol is ", classCoctelFruit.amountAlcohol,"%")
    print("The cost of product is $", classCoctelFruit.cost)
else:
    print("----------------------TYPE DATAS CORRECTS------------------")
    