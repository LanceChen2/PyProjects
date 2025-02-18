import random

NUM = 5 

unsorted_list_generate = random.sample(range(1, NUM+1), NUM)

with open(f'C:\\Users\\user\\Python Projects\\unsorted_list_generation\\unsorted_list_of_{NUM}.txt', 'w') as f: 
    for _ in unsorted_list_generate: 
        f.write(f"{_}\n")