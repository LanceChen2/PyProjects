
# read elements in txt file into a list
NUM = 1000  #change number for different file(s)
with open(f"C:\\Users\\user\\Python Projects\\unsorted_list_generation\\unsorted_list_of_{NUM}.txt") as file: 
    lines = [line.rstrip() for line in file]

# check if there is any duplicates for comparison
print(lines)
print(len(lines))
lines = list(set(lines))
print(len(lines))
