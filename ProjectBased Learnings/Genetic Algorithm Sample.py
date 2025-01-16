import pygame
import random
import math

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Genetic Algorithm Simulation")

# Colors for display
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Genetic Algorithm Parameters
POPULATION_SIZE = 150  # Number of agents in the population
GENE_LENGTH = 100  # Number of steps each agent takes (genes)
MUTATION_RATE = 0.01  # Probability of mutation in a gene
TARGET = (WIDTH // 2, HEIGHT // 10)  # The target position on the screen

# Agent class represents an individual agent in the population
class Agent:
    def __init__(self):
        # Initialize agent's starting position and random genes
        self.position = [WIDTH // 2, HEIGHT - 50]  # Start position at the bottom center
        self.genes = [self.random_gene() for _ in range(GENE_LENGTH)]  # List of genes (steps)
        self.fitness = 0  # Fitness score
        self.step = 0  # Step counter to track movement through genes

    @staticmethod
    def random_gene():
        # Random step in the range of -2 to 2 for both x and y directions
        return [random.uniform(-2, 2), random.uniform(-2, 2)]

    def move(self):
        # Move the agent according to the current gene (step)
        if self.step < len(self.genes):
            self.position[0] += self.genes[self.step][0]
            self.position[1] += self.genes[self.step][1]
            self.step += 1  # Move to the next gene (step)

    def calculate_fitness(self):
        # Fitness is calculated based on the distance to the target
        distance = math.sqrt((self.position[0] - TARGET[0])**2 + (self.position[1] - TARGET[1])**2)
        self.fitness = 1 / (distance + 1)  # Fitness is the inverse of the distance to avoid division by zero

# Genetic Algorithm functions
def crossover(parent1, parent2):
    # Perform crossover between two parent agents to create a child agent
    split = random.randint(0, GENE_LENGTH - 1)  # Random crossover point
    child = Agent()  # Create a new agent (child)
    child.genes = parent1.genes[:split] + parent2.genes[split:]  # Combine genes from both parents
    return child

def mutate(agent):
    # Mutate the genes of an agent with a certain probability (mutation rate)
    for i in range(len(agent.genes)):
        if random.random() < MUTATION_RATE:
            agent.genes[i] = agent.random_gene()  # Replace gene with a new random gene

# Main function for running the simulation
def main():
    clock = pygame.time.Clock()  # Clock object to control the frame rate
    population = [Agent() for _ in range(POPULATION_SIZE)]  # Create the initial population of agents
    generation = 0  # Start at generation 0

    running = True
    while running:
        screen.fill(BLACK)  # Fill the screen with black background
        pygame.draw.circle(screen, RED, TARGET, 10)  # Draw the target as a red circle

        # Event handling to close the window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False  # Stop the loop when the window is closed

        # Update agents' positions
        for agent in population:
            if agent.step < GENE_LENGTH:  # Move agent if it has not completed all steps
                agent.move()
            pygame.draw.circle(screen, BLUE, (int(agent.position[0]), int(agent.position[1])), 5)  # Draw agent as a blue circle

        # If all agents have finished their movement (i.e., all agents have completed their genes)
        if all(agent.step >= GENE_LENGTH for agent in population):
            # Calculate fitness for each agent
            for agent in population:
                agent.calculate_fitness()

            # Selection (roulette wheel selection)
            population.sort(key=lambda x: x.fitness, reverse=True)  # Sort agents by fitness (best first)
            new_population = [population[0]]  # Keep the best agent (elitism)

            # Create new population using crossover and mutation
            while len(new_population) < POPULATION_SIZE:
                parent1, parent2 = random.choices(population, weights=[a.fitness for a in population], k=2)  # Select parents based on fitness
                child = crossover(parent1, parent2)  # Crossover to create a child agent
                mutate(child)  # Mutate the child agent
                new_population.append(child)  # Add the child to the new population

            population = new_population  # Replace old population with the new one
            generation += 1  # Increment generation count
            print(f"Generation {generation} - Best Fitness: {population[0].fitness:.4f}")  # Print best fitness of the generation

        # Display generation count on the screen
        font = pygame.font.SysFont(None, 36)  # Font for displaying text
        text = font.render(f"Generation: {generation}", True, WHITE)  # Render the text
        screen.blit(text, (10, 10))  # Display the text on the screen

        pygame.display.flip()  # Update the screen
        clock.tick(120)  # Control the frame rate (120 FPS)

    pygame.quit()  # Quit Pygame when the simulation ends

# Run the main function if the script is executed
if __name__ == "__main__":
    main()
