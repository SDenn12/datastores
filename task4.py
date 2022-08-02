story = {
    "start": "James woke up one morning and went to the shop.",
    "middle": "James got mugged at the shop.",
    "end": "Shop owner called the police. The end."
}

print(type(story))
print(story.keys())
print(story.values())
print("\nStory Begins\n ")

for key in story.keys():
    print(story[key])

story["hero"] = "Super Pravin turns up saves the day"

for key in story.keys():
    print(story[key])
