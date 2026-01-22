def find_differentially_expressed_genes(control_counts, treatment_counts, gene_names, fold_change_threshold):
    return [
        gene
        for c, t, gene in zip(control_counts, treatment_counts, gene_names)
        if (t / c if c else t) > fold_change_threshold
    ]
    

control_counts = [100, 50, 200, 0]
treatment_counts = [300, 50, 1000, 10]
gene_names = ["GeneA", "GeneB", "GeneC", "GeneD"]
fold_change_threshold = 2.0

result = find_differentially_expressed_genes(control_counts, treatment_counts, gene_names, fold_change_threshold)
print(result)
