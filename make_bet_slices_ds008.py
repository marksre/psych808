#!/usr/bin/python

# Create variable for subject ID
subj_id = 2

# Open bet_slices template file
template_file = open("/home/marksre/Projects/local/share/templates/html/bet_slices.html")

# Open output file
output_file = open("/home/marksre/Projects/output/html/sub002_bet_slices.html", "w")

#Create list of lines from template file
template_text = template_file.readlines()
template_file.close()

# Print template file but with subject ID

for line in template_text:
    output_file.write(line.format(subj_id))
output_file.close()

#Another option:
#with open("/home/marksre/Projects/local/share/templates/html/bet_slices.html", "r") as template:
#    for line in template:
#        output_file.write(line.format(17))
#output_file.close()
