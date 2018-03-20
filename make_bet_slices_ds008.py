#!/usr/bin/python

# Create variable for subject ID
subj_id = 2

# Open bet_slices template file
template_file = open("/home/marksre/Projects/local/share/templates/html/bet_slices.html")

# Open output file
output_file = open("/home/marksre/Projects/output/html/sub002_bet_slices.html", "w")

# Find lines that contain Subject ID variable
for line in template_file:
	line.find("{:03d}")
	print line.format(subj_id)
template_file = "\n".join(template_file)

# Print template file but with subject ID
print(template_file.format(subj_id))


output_file.write("test")
output_file.write(print(template_file.format(subj_id)))

# Save contents of print function to output
with open("/home/marksre/Projects/local/share/templates/html/bet_slices.html", "r") as template:
	with open("/home/marksre/Projects/output/html/sub002_bet_slices.html", "w") as output:
		for line in template:
		        line.find("{:03d}")
       		print line.format(subj_id)
			output.write(line)

#output = "\n".join(template)

#output_contents = str(template_file.format(subj_id))
#output.write(output_contents)
#output.close()
