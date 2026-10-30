print("======= Daily Dose of Drink! =======")
menu = "Our menu offers: mint, strawberry, coffee and mango tastes."
print(' ')
print(menu)
print(' ')

choose1 = input("Please choose the first taste: ").lower()
choose2 = input("Please choose the second taste: ").lower()

print(' ')
print("Your drink is being prepared ...")
print(' ')

if choose1 == choose2:
    print("Double-trouble!")
elif (choose1 == "mint" and choose2 == "coffee") or (choose2 == "mint" and choose1 == "coffee"):
    print(choose1.capitalize(), "and", choose2, "-", "this cool espresso might be a little rough!", end=':)')
elif (choose1 == "mint" and choose2 == "mango") or (choose2 == "mint" and choose1 == "mango"):
    print(choose1.capitalize(), 'and', choose2, '-', 'tropical Mohito might be the thing!')
elif (choose1 == "mint" and choose2 == "strawberry") or (choose2 == "mint" and choose1 == "strawberry"):
    print(choose1.capitalize(), "and", choose2, "-", "fruity!")
elif (choose1 == "strawberry" and choose2 == "coffee") or (choose2 == "strawberry" and choose1 == "coffee"):
    print(choose1.capitalize(), 'and', choose2, '-', 'almost Matcha Latte!')
elif (choose1 == "mango" and choose2 == "coffee") or (choose2 == "mango" and choose1 == "coffee"):
    print(choose1.capitalize(), "and", choose2, "-", "jungle energy drink, are you a fan of Red Bull?")
elif (choose1 == "strawberry" and choose2 == "mango") or (choose2 == "strawberry" and choose1 == "mango"):
   print(choose1.capitalize(), "and", choose2, "-", "like a natural jungle drink")
else:
    print("We don't offer this drink yet, check out our menu once again!", menu, sep=' :^ ')

print(' ')

sugar = input("Should I add some sugar? Yes/No: ").lower()
ice = input("Would you like some ice? Yes/No: ").lower()
allergy = input("Do you have any allergies? Yes/No: ").lower()

if (sugar == "No" or sugar == "no") and (ice == "No" or ice == "no"):
    print("You chose a really healthy option")
elif (choose1 == "coffee" and choose2 == "mint") or (choose1 == "mint" and choose2 == "coffee") and (ice == "Yes" or ice == "yes"):
    print("Careful! Coffee might taste bad and too cold!")
elif allergy == "Yes" or allergy == "yes":
   print("Careful! THE DRINK CONTAINS STRAWBERRY ! ! !")
   
print(' ')
review = int(input("Please leave a review about your drink from 1 to 5: "))
if review == 5 or review == 4:
    print("Thank you for your review! We are glad you liked it!")
elif review == 3:
    print("Thank you for your review! We hope to improve!")
else:
    print("Thank you for your review! We will use your feedback to improve!")
print("======= Bye! =======")