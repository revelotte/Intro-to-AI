from itertools import combinations

print("\nAPRIORI EXAMPLE 2: Song Playlist Patterns")
print("-----------------------------------------")

# Playlists (songs that appear together)
playlists = [
    ["Blinding Lights", "Stay", "Levitating"],
    ["Stay", "Levitating"],
    ["Blinding Lights", "Stay"],
    ["Levitating", "Stay"],
]

pairs = {}

# Count song pairs
for playlist in playlists:
    for pair in combinations(playlist, 2):
        pairs[pair] = pairs.get(pair, 0) + 1

# Display results nicely
print("Song Pair Frequencies:\n")

for pair, count in pairs.items():
    print(f"{pair[0]} + {pair[1]} : {count} times")