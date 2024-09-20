from collections import defaultdict

# File paths
input_file = 'ni_03_zn_01.xyz'

# Read the original data from the file
with open(input_file, 'r') as file:
    lines = file.readlines()

# Initialize group-based counters
group_counts = defaultdict(lambda: defaultdict(int))
total_counts = defaultdict(int)

# Process each line of the file (ignoring header lines)
for line in lines[2:]:  # Assuming the first two lines are header lines
    elements = line.split()
    atom_type = elements[0]
    group_id = int(elements[-1])
    
    # Increment the count for the atom type in the specific group
    group_counts[group_id][atom_type] += 1
    
    # Increment the total count for the atom type
    total_counts[atom_type] += 1

# Output group-wise counts
print("Counts for each group:")
for group_id, counts in sorted(group_counts.items()):
    print(f"Group {group_id}: ", end="")
    for atom_type, count in sorted(counts.items()):
        print(f"{atom_type} = {count}, ", end="")
    print()

# Output total counts across all groups
print("\nTotal counts across all groups:")
for atom_type, count in sorted(total_counts.items()):
    print(f"{atom_type} = {count}")
