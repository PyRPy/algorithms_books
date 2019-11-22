from sys import argv
from os.path import exists

script, from_file, to_file = argv

print(f"copying from {from_file} to {to_file}")

# we could do these two on one line, how ?
in_file = open(from_file)
indata = in_file.read()

print(f"the input file is {len(indata)} bytes long")

print(f"does the output file exist? {exists(to_file)}")
print("ready, hit RETURN to continue, CTRL to abort.")
input()

outfile = open(to_file, 'w')
outfile.write(indata)

print("alright, all done.")

outfile.close()
in_file.close()
