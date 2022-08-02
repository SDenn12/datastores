# Lists

# shopping_list = ["bat", "bread", "milk"]
# print(shopping_list[0])
# print(len(shopping_list))
# print(type(shopping_list))
#
# # how to add to a list
# shopping_list.append("oreos")  # append() adds item to the end of the list
# print(shopping_list)
#
# # how to delete an item from a shopping list
# shopping_list.remove("milk")
# print(shopping_list)
#
# # how to replace item in shopping list
# shopping_list[0] = "milk"

# slice list
# mixed_list = [1, 2, 3, "one", "two", "three"]
# print(mixed_list[1:3])  # outcome would be [2, 3] [start point (inclusive): end point (exclusive): step size]

# Tuples
# Why do we need tuple?
# Lists are mutable and tuples are immutable
# syntax for tuple ()
# Use cases include DOB/place of birth
# essential = ("city", "DOB", "place of birth")
# print(essential)
# print(type(essential))
# print(essential[1])

# Dictionary
# Why do we need dictionary?
# Include key value pairs
# Dictionary can have al types of data collections
# syntax for dictionaries {key:value}

devops_student_1 = {"name": "sam",
                    "age": 21,
                    "stream": "tech",
                    "completed_lessons": 3,
                    "completed_lessons_names": ["strings", "lists", "operations"]
                    }
print(devops_student_1.keys())
print(devops_student_1.values())
print(devops_student_1["completed_lessons_names"][1])
# find out how to delete an item from dictionary and delete operations
# find out how to change completed lessons from 3 to 2
del(devops_student_1["stream"])
devops_student_1["completed_lessons"] = 2
devops_student_1["completed_lessons_names"][1] = "sparta skills"
print(devops_student_1)

