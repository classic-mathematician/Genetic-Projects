import string
import random



genes = " abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!."
target = "Hello World!"


def generate_parent(lenght):
	dna = []

	while len(dna) < lenght:
		print(len(dna))
		dna.append(random.choice(genes))

	return ''.join(dna)


def get_fitness(guess):
	fitness = 0

	for a, b in zip(guess, target):
		if a == b:
			fitness += 1

	return fitness



def mutate(parent):
	block = random.randint(0, len(parent) - 1)
	child_genes = list(parent)

	new_gene = random.choice(genes)
	child_genes[block] = new_gene

	return ''.join(child_genes)



def display(guess):
	print("{}: {}".format(guess, get_fitness(guess)))



best_parent = generate_parent(len(target))
best_fitness = get_fitness(best_parent)
display(best_parent)


while True:
	child = mutate(best_parent)
	child_fitness = get_fitness(child)

	if best_fitness >= child_fitness:
		continue

	display(child)

	if child_fitness >= len(best_parent):
		break
	best_fitness = child_fitness
	best_parent = child