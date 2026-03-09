from itertools import combinations

print("APRIORI EXAMPLE 1: Movie Watching Patterns")
print("------------------------------------------")

# Transactions (movies watched together)
transactions = [
    ["Avengers", "Spider-Man", "Iron Man"],
    ["Spider-Man", "Iron Man"],
    ["Avengers", "Thor"],
    ["Avengers", "Spider-Man"],
    ["Thor", "Iron Man"]
]

pairs = {}

# Count how often movie pairs appear together
for t in transactions:
    for pair in combinations(t, 2):
        pairs[pair] = pairs.get(pair, 0) + 1

# Display results nicely
print("Movie Pair Frequencies:\n")

for pair, count in pairs.items():
    print(f"{pair[0]} + {pair[1]} : {count} times")