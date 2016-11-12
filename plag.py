# Code Plagiarism detection in source codes
# Supports C, C++, Python, Java, Javascript, MATLAB
# Can be extended easily to support other languages 
# by adding the keywords in that language

# @autor binu jasim: bnjasim@gmail.com
# date: 12-Nov-2016 - 
# Open Source software: MIT License

file = open('res/btree.c')
outfile = open('res/out.c', 'w')

for line in file:
  cont = line.split()
  for token in cont:
    outfile.write(token)
    outfile.write(' ')
  outfile.write('\n')

file.close()  
outfile.close()