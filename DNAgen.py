
import sys
import random

Nb = 180
FileName = "test_dna.seq"
if len(sys.argv) > 2:
  FileName = sys.argv[1] + ".seq"
  Nb = sys.argv[2]
else:
  raise ValueError("Invalid input parameters. Please provide arguments: FileName Nb when calling DNAgen.py.\nUsage:\npython DNAgen.py test 1231")

def random_seq(Nb=100):
  return ''.join(random.choice('AGCT') for _ in range(Nb))

def write_to_file(FileName, data):
  with open(FileName, 'w') as f:
    f.write(data)

dna_seq = random_seq(int(Nb))

write_to_file(FileName, dna_seq)

print("successfully generated a DNA sequence file - <" + FileName + ">")
