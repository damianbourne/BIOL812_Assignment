
import sys
from collections import Counter

comma = ","
FileName = "test_dna"
if len(sys.argv) > 1:
  FileName = sys.argv[1]
else:
  raise ValueError("Invalid input parameters. Please provide arguments: FileName when calling BASE.py.\nUsage:\npython BASE.py test")

def read_file(FileName):
  lines = ""
  with open(FileName + ".seq") as f:
    lines = f.read()
  return lines

def write_to_file(FileName, data):
  with open(FileName, 'w') as f:
    f.write(data)
	
dna_seq = read_file(FileName)

counter = Counter(dna_seq)

output_counters = str(counter['A']) + comma + str(counter['G']) + comma + str(counter['C']) + comma + str(counter['T'])

print(output_counters)

output_fileName = FileName + ".count"
write_to_file(output_fileName, output_counters)

print("successfully generated counter file - <" + output_fileName + ">")

