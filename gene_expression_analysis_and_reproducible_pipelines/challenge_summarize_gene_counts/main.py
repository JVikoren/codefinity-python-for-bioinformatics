import pandas as pd

def summarize_gene_counts(counts_df):
    result = {}
    result["total_counts_per_gene"] = counts_df.sum(axis=1)
    result["total_counts_per_sample"] = counts_df.sum(axis=0)
    result["mean_gene_total"] = sum(result["total_counts_per_gene"]) / len(result["total_counts_per_gene"])
    result["median_gene_total"] = result["total_counts_per_gene"].median()
    result["mean_sample_total"] = sum(result["total_counts_per_sample"]) / len(result["total_counts_per_sample"])
    result["median_sample_total"] = result["total_counts_per_sample"].median()
    return result
    
# Example usage:
data = {
    "Sample1": [100, 200, 300],
    "Sample2": [150, 250, 350],
    "Sample3": [120, 220, 320]
}
genes = ["GeneA", "GeneB", "GeneC"]
counts_df = pd.DataFrame(data, index=genes)

summary = summarize_gene_counts(counts_df)

gene_totals_print = summary["total_counts_per_gene"]
sample_totals_print = summary["total_counts_per_sample"]
mean_gene_total_print = summary["mean_gene_total"]
median_gene_total_print = summary["median_gene_total"]
mean_sample_total_print = summary["mean_sample_total"]
median_sample_total_print = summary["median_sample_total"]

print(gene_totals_print)
print(sample_totals_print)
print(mean_gene_total_print)
print(median_gene_total_print)
print(mean_sample_total_print)
print(median_sample_total_print)
