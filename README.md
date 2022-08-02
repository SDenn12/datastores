# Data Collections
## Lists, Tuples, Dictionaries

### What are lists?
- correct syntax []
- lists are mutable
- indexing applies
```python
shopping_list = ["bat", "bread", "milk"]
print(shopping_list[0])
print(len(shopping_list))
print(type(shopping_list))

# how to add to a list
shopping_list.append("oreos")  # append() adds item to the end of the list
print(shopping_list)

# how to delete an item from a shopping list
shopping_list.remove("milk")
print(shopping_list)

# how to replace item in shopping list
shopping_list[0] = "milk"

# slice list
mixed_list = [1, 2, 3, "one", "two", "three"]
print(mixed_list[1:3])  # outcome would be [2, 3] [start point (inclusive): end point (exclusive): step size]
```