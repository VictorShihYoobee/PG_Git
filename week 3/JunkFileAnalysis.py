
infile = open("junk.txt", "r")

lines_count = 0
new_context = ""
for line in infile:
    lines_count += 1 
    new_context += line.strip().lower() + "\n"
new_context += "text file nanalyssis"

print("Total number of lines: ", lines_count)
print("New context: ", new_context)
outfile = open("junk.txt", "w")
outfile.write(new_context)
outfile.close()
infile.close()