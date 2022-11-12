suites = {
    "heart": "red",
    "spade": "black",
    "diamond": "red",
    "club": "black"
}
cards = [1,2,3,4,5,6,7,8,9,10,11,12,13]
colors = ["red","black"]

# chance of getting a single color
totalCardCount = len(cards) * len(suites)
print(round(totalCardCount / len(colors), 2))

# chance of getting a single suite
print(round(totalCardCount / len(suites), 2))
