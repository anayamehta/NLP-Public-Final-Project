import random
import sys


input_file = sys.argv[1]
output_file = sys.argv[2]

f = open(input_file, "r")
fout = open(output_file, "w")

length = -1
if len(sys.argv) == 4:
    length = sys.argv[3]

total = 0
for line in f:
    random_num = random.randint(0, 1)
    if random_num:
        total+=1
        fout.write(line)
    if int(length) == total:
        break

fout.close()