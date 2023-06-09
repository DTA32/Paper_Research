# Convert tsp file to data file for the program
# Only deleting the first column, so before running this
# you should delete from row "NAME" to "NODE_COORD_SECTION" first
input_file = "nrw1379.tsp"
output_file = "cities_1379.data"

with open(input_file, "r") as file:
    lines = file.readlines()

output_lines = []
for line in lines:
    # Split the line by whitespace
    data = line.split()
    # Remove the first element from the data list
    data.pop(0)
    # Join the remaining elements with whitespace and add it to the output lines
    output_lines.append(" ".join(data))

with open(output_file, "w") as file:
    file.write("\n".join(output_lines))

print("Output file created:", output_file)