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
  # strip line - remove front and back whitespaces
  line = line.lstrip()
  # Check for comments. 
  # First check for // comments
  comment_pos = line.find('//')
  if (comment_pos == 0):
    continue

  if (comment_pos > 0):
    line = line[:comment_pos]

  contents = line.split()
  for token in contents:
    outfile.write(token)
    outfile.write(' ')
  outfile.write('\n')

file.close()  
outfile.close()