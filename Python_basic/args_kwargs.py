# *args is tuple
# **kawargs is dict

def add(*args):
    total = 0
    for num in args:
        total += num
    return total

print(add(1,2,3,4))


def display(*args):
    for arg in args:
        print(arg, end= " ")

display("sopup", "dir" , "roy")

def change_value(*args):
    for list in args:
        print(list, end=" ")

change_value("this", "add", "mutiple", "changing", "value")


# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>..?

# if you have mutltiple arguments(parameters) so you use **kwargs becuase you don't type this args in fuction parameters 
# kwargs store data in key value pair beacuse of its use dict

def print_address(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")


print_address(street="st. friont", city="LA", state="calfronia",zip="54554")


#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

def ship(*args, **kwargs):
    for arg in args:
        print(arg, end=" ")
    print()
    for value in kwargs.values():
        print(value, end=" ")

ship("dr", "ryan", "bourd" , "IIV",
     street="23. fake St.",
     city="san francesico",
     state="MI",
     zip="44544")