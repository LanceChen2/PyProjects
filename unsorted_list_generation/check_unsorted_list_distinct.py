
# read elements from txt file into a list
NUM = 1000  #change number for different file(s)
with open(f"C:\\Users\\user\\Python Projects\\unsorted_list_generation\\unsorted_list_of_{NUM}.txt") as file: 
    lines = [line.rstrip() for line in file]


# to write a function with 2 different variables for comparison
# check if there is any duplicates via set function for comparison
print(lines)
print(len(lines))
lines = list(set(lines))
print(len(lines))
