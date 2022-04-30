#==== weight converter=========
def convert_to_kg (weight):
    return weight / 2.2

def convert_to_lbs (weight):
    return weight * 2.2

weight = int(input ("What is your weight? "))
unit = input("Is this in kg or pounds? ").lower()

if unit == "pounds" or  unit == "lbs" or unit == "lb":
    print(f"You weight is {weight}{unit}, Which converts to {convert_to_kg (weight)} kilograms.")
    
elif unit == "kilograms" or  unit == "kgs" or unit == "kg":
    print(f"You weight is {weight} {unit}, Which converts to {convert_to_lbs (weight)} pounds.")
else :
    print("You must enter weight in pounds or kilograms.")