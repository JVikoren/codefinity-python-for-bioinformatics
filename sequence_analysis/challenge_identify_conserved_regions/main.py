def find_conserved_positions(alignment):
    if not alignment:
        return []
    
    alignment_length = len(alignment[0])

    positions = []
    for i in range(alignment_length):
        column = [sequence[i] for sequence in alignment]
        matches = [c for c in column if c == column[0]]
        if len(matches) == len(column):
            positions.append(i)
    return positions
            

# Sample calls
alignment1 = [
    "ATGCT",
    "ATGCT",
    "ATGCT"
]
result1 = find_conserved_positions(alignment1)
print(result1)

alignment2 = [
    "ATGCT",
    "ATGCA",
    "ATGCC"
]
result2 = find_conserved_positions(alignment2)
print(result2)

alignment3 = [
    "AACGTA",
    "AACGTA",
    "AACGTA"
]
result3 = find_conserved_positions(alignment3)
print(result3)

alignment4 = [
    "AACGTA",
    "AGCGTA",
    "AACGTA"
]
result4 = find_conserved_positions(alignment4)
print(result4)
