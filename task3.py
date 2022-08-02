name = input("What is your name? ").lower().capitalize()
height = input("What is your height? ")
fav_col = input("What is your favourite colour? ")
spir_ani = input("What is your spirit animal? ")

print(f"Welcome {name}. \nYou're {height}m tall. \nYour favourite colour is {fav_col}. "
      f"\nYour secret begins with {spir_ani[0]} and ends with {spir_ani[-1]}. "
      f"\nThe length of the word is {len(spir_ani)}")
guess = input("\nGuess what the spirit animal is! ")
if spir_ani.lower() == guess.lower():
    print("\nWow how did you know? :DD")
else:
    print("\nSorry that is incorrect.")
