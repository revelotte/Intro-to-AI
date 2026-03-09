import random

print("\nGENETIC ALGORITHM EXAMPLE 2: Song Popularity Optimization")
print("----------------------------------------------------------")

target_popularity = 90

# Initial population
songs = [random.randint(50, 100) for _ in range(10)]

print("Initial Popularity Scores:", songs)

def fitness(x):
    return abs(target_popularity - x)  # closer to 90 is better

for generation in range(20):

    songs = sorted(songs, key=fitness)

    best = songs[:5]

    while len(best) < 10:
        p1, p2 = random.sample(best, 2)

        child = (p1 + p2) // 2

        # Mutation
        if random.random() < 0.2:
            child += random.randint(-5, 5)

        best.append(child)

    songs = best

print("\nTarget Popularity:", target_popularity)
print("Best Song Popularity Found:", songs[0])