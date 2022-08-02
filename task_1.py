# Task 1

# Version 1
def version_one():
    name = "Random String"
    name = "sAM   ".lower().capitalize().replace(" ","")
    last = "DENNIS              ".lower().capitalize().replace(" ","")
    print(len(name))
    full_name = name + " " + last

    print(f"Welcome {full_name}")

# Version 2
def version_two():
    full_name = "Random String"
    full_name = "sam dennis"
    first, last = full_name.split(" ")
    f_n = first.lower().capitalize()
    l_n = last.lower().capitalize()
    print(f"Welcome {f_n} {l_n}! ")


version_two()

