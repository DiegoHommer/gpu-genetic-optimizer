from genetic_operations import *

def run_genetic_algorithm(total_gpus, total_vram, total_types, total_prns, prns, params):
    population_size = params.population_size
    recombination_rate = params.recombination_rate
    population, gpu_population = generate_initial_population(population_size, total_gpus, total_vram, total_types, total_prns, prns)

    i = 0
    while(i < 2):
        new_population = np.empty((population_size, total_prns), dtype=int)
        new_gpu_population = np.empty((population_size, total_gpus), dtype=int)
        for j in range(population_size):
            if (rand.random() <= recombination_rate):
                new_chromosome, new_gpus = recombine_solutions(population[0], population[1], prns, total_prns, gpu_population[0], gpu_population[1], total_gpus, total_vram)
            
        population = np.copy(new_population)
        i += 1

    print(population)