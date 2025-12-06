
def describe_pet(animal_type, pet_name):
    print(f"I have a {animal_type} and its name is {pet_name}.")


describe_pet("cat", "ginger")
describe_pet("spider", "twoyie")
describe_pet("turtle", "gonggong")



describe_pet("dog", "ryu")


describe_pet(pet_name="dindo", animal_type="chicken")


def describe_pet(pet_name, animal_type="tiger"):
    print(f"I have a {animal_type} and its name is {pet_name}.")

describe_pet("bantul")
describe_pet("abdul", "jidulo")



def order_drink(drink, size="medium", iced=False):
    if iced:
        ice_text = "iced"
    else:
        ice_text = "hot"

    return f"Your order: {size} {ice_text} {drink}"


print(order_drink("coke"))
print(order_drink("san mig", size="large", iced=False))
print(order_drink("red horse", size="small", iced=True))


def compute(operation, num1, num2=1):
    if operation == "add":
        return num1 + num2
    elif operation == "multiply":
        return num1 * num2
    elif operation == "subtract":
        return num1 - num2
    else:
        return "Invalid operation"


print(compute("add", 6, 7))
print(compute("multiply", num1=6, num2=7))
print(compute("subtract", 67))  
print(compute("divide", 6, 7)) 