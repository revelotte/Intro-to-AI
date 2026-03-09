import random

print("GENETIC ALGORITHM EXAMPLE 1: Movie Rating Optimization")
print("------------------------------------------------------")

movies = ["Action", "Comedy", "Drama"]

# Initial population (random ratings)
population = [random.randint(1, 10) for _ in range(6)]

print("Initial Ratings:", population)

def fitness(x):
    return x   # higher rating is better

for generation in range(5):

    population = sorted(population, reverse=True)

    parent1 = population[0]
    parent2 = population[1]

    child = (parent1 + parent2) // 2

    # Mutation
    if random.random() < 0.3:
        child += random.randint(-1, 1)

    population[-1] = child

    print(f"Generation {generation+1}:", population)

print("\nMovie Categories:", movies)
print("Best Rating Found:", population[0])