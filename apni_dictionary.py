print("Welcome to Apni Dictionary!!")
print("1)Hello\n2)WoW\n3)Benefit\n4)Dally")
my_dict={"Hello": "Greetings", "WoW ": "Exclamation", "Benefit":"Advantage","Dally":"Delay"}
print("Enter the word whose meaning you want")
choice=input()
print("Meaning of the word" + " " + choice + " " + "is" +" "+ my_dict.get(choice))