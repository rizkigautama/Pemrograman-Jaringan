x = "riziq"

def print_x():
    global x
    x = "123"
    print(f"my id is {x} ")

print(f"value is() : {x}")
print_x()
print(f"value is() : {x}")