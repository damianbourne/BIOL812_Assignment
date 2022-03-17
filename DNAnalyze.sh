#!/bin/bash

# delete the output file and set header
cat /dev/null > dna_output.csv
echo "A,T,G,C" > dna_output.csv

# Loop through and create the 100 input files containing 1000 bases of data called DNAseqNNN.seq
counter=1

while [ $counter -le 100 ]
do

number=$(printf "%03d" $counter)
filename=DNAseq$number

python3 DNAgen.py $filename 1000
python3 BASE.py $filename

if [[ $counter -ne 1 ]]; then
  echo "" >> dna_output.csv
fi

# Merge base files into one output
cat $filename.count >> dna_output.csv

((counter++))

done
