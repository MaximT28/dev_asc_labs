import csv
import itertools
a=['DES','3DES','AES-128']
b=['DH2','DH5','DH14']
c=['md5','sha']
combo = [a,b,c]
# https://docs.python.org/3/library/itertools.html#itertools.product
combinations = [combination for combination in itertools.product(*combo)] #return a list of tuples
with open('text.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    print(f'Created {len(combinations)} combinations')
    for combination in combinations:
        # print(combination)
        writer.writerow(combination)
