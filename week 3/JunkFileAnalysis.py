
infile = open("junk.txt", "r", encoding="utf-8")

new_context = ""
for line in infile:
    new_context += line.strip().lower() + "\n"
new_context += "text file nanalyssis"

print("Total number of lines: ", new_context.count("\n"))
print("New context: \n", new_context)
outfile = open("junk.txt", "w")
outfile.write(new_context)
outfile.close()
infile.close()