python3 ./src/main.py \
    --population-size 100 \
    --crossover-rate 0.8 \
    --mutation-rate 0.3 \
    --max-iterations 20000 \
    --elitism-rate 0.2 \
    --selection-pressure 1.5 \
    --stagnation-limit 20000 \
    --seed 0 \
    test.txt < example_instances/dog_test.txt 