import matplotlib.pyplot as plt

def phred33_to_q(char):
    return ord(char) - 33

def average_read_quality(quality_string):
    if not quality_string:
        return 0
    return sum([phred33_to_q(char) for char in quality_string]) / len(quality_string)

def get_qualities_from_list(quality_strings):
    qualities = []
    for qual in quality_strings:
        avg_q = average_read_quality(qual)
        qualities.append(avg_q)
    return qualities

def read_fastq_qualities(filepath):
    qualities = []
    with open(filepath) as f:
        for i, line in enumerate(f):
            if (i % 4) == 3:
                qualities.append(average_read_quality(line.strip()))
    return qualities

def plot_quality_histogram(qualities):
    plt.hist(qualities, bins=30, color='skyblue', edgecolor='black')
    plt.title("Histogram of Average Read Quality")
    plt.xlabel("Average Read Quality")
    plt.ylabel("Read Count")
    plt.show()

# Example usage:
example_qualities = [
    "IIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIII",
    "BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB",
    "JJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJ"
]
qualities = get_qualities_from_list(example_qualities)
plot_quality_histogram(qualities)
