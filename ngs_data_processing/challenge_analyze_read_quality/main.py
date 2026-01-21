def count_high_quality_reads(fastq_lines, threshold):
    reads = fastq_lines[3::4]
    scores = []
    for read in reads:
        read = [ord(char) - 33 for char in read]
        scores.append(sum(read) / len(read))
    return len([score for score in scores if score > threshold])

sample_fastq = [
    "@SEQ_ID1",
    "GATTTGGGGTTCAAAGCAGTATCGATCAAATAGTAAATTTTGGGGTTCAAAGCAGTATCGATCAAATAGTAA",
    "+",
    "IIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIII",
    "@SEQ_ID2",
    "AGCTTAGCTAGCTACCTATATCTTGGTCTTGGCCG",
    "+",
    "IIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIII",
    "@SEQ_ID3",
    "CGTAGCTAGCTAGCTGACTGATCGATCGTAGCTAGC",
    "+",
    "########IIIIIIIIIIIIIIIIIIIIIIIIIIIII"
]

threshold_value = 30
result = count_high_quality_reads(sample_fastq, threshold_value)
print(result)
