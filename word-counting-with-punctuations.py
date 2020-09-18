import string

f_dir = '..\\data\\'
fname = input("Enter the file name: ")
fname = f_dir + fname
count = {}
try:
    f = open(fname)
except:
    print("The file cannot be opened:", fname)

for line in f:
    line = line.rstrip()
    line = line.lower()
    line = line.translate(line.maketrans('', '', string.punctuation))
    words = line.split()
    for word in words:
        count[word] = count.get(word, 0) + 1

f.close()
for k, v in count.items():
    print(k + ':', v)
