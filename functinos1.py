'''
def greet_user():
    """ask the user for their name and greet them"""
    name = input("Enter you name")
    print(f"hello, {name}! Welcome to the course")

greet_user()

def calculate_total(price,quantity):
    total = price*quantity
    return total
item_price = 19.99
item_quantity = 3
bill_total = calculate_total(item_price,item_quantity)
print(" total bill:", bill_total)

def checkout(amount,shipping=5.0):
    final_amount = amount + shipping
    return final_amount
print("order 1 total:", checkout(50))
print("order 2 total:", checkout(50,shipping=10))



def register_student(name,program,year):
    print("-------Student Registration-------")
    print(f"name:{name}")
    print(f"program:{program}")
    print(f"year:{year}")
    print("----------------------------------")

register_student("anu","computer science", 1)
'''

def average_score(*scores):
    if not scores:
        print("no scores provided")
        return None
    total = sum(scores)
    avg = total/len(scores)
    print(f"scores:{scores}")
    print(f"average:{avg}")
    return avg

average_score(80,90,75)
average_score(100,95)
average_score()






