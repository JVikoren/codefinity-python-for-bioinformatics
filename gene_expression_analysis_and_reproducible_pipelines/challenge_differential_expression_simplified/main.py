def find_differentially_expressed_genes(control_counts, treatment_counts, gene_names, fold_change_threshold):
    control_counts = [c if c != 0 else fold_change_threshold for c in control_counts]
    fold_change = [t / c for t, c in zip(treatment_counts, control_counts)]
    result = []
    for i in range(len(gene_names)):
        if fold_change[i] > fold_change_threshold:
            result.append(gene_names[i])
    return result
    

control_counts = [100, 50, 200, 0]
treatment_counts = [300, 50, 1000, 10]
gene_names = ["GeneA", "GeneB", "GeneC", "GeneD"]
fold_change_threshold = 2.0

result = find_differentially_expressed_genes(control_counts, treatment_counts, gene_names, fold_change_threshold)
print(result)
