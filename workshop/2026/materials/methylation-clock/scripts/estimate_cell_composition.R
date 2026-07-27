# estimate_cell_composition.R
# Estimate blood cell type proportions from GSE41037 beta matrix using EpiDISH
#
# Required: R with EpiDISH installed (BiocManager::install('EpiDISH'))
#
# Usage: Rscript scripts/estimate_cell_composition.R

library(EpiDISH)

# Paths
beta_path <- "results/tables/GSE41037_horvath_cpg_beta.csv"
full_beta_path <- "Data/GSE41037_series_matrix.txt/GSE41037_series_matrix.txt"
cache_path <- "results/tables/GSE41037_full_beta_for_epidish.csv"
out_path <- "results/tables/GSE41037_estCellTypes.csv"

# Try loading the cached full beta matrix first, or extract from series matrix
if (file.exists(cache_path)) {
  beta_full <- read.csv(cache_path, row.names = 1, check.names = FALSE)
  cat("Loaded full beta from cache:", nrow(beta_full), "CpGs x", ncol(beta_full), "samples\n")
} else if (file.exists(full_beta_path)) {
  cat("Extracting full beta matrix from series matrix...\n")
  lines <- readLines(full_beta_path)
  start <- grep("!series_matrix_table_begin", lines)
  end <- grep("!series_matrix_table_end", lines)
  data_str <- paste(lines[(start+1):(end-1)], collapse = "\n")
  beta_full <- read.csv(text = data_str, sep = "\t", row.names = 1, check.names = FALSE)
  write.csv(beta_full, cache_path)
  cat("Full beta:", nrow(beta_full), "CpGs x", ncol(beta_full), "samples (cached)\n")
} else {
  stop("Full series matrix not found at: ", full_beta_path)
}

# Use as matrix
beta.m <- as.matrix(beta_full)

# Remove rows with NA
na_rows <- rowSums(is.na(beta.m)) > 0
if (sum(na_rows) > 0) {
  cat("Removing", sum(na_rows), "CpGs with NA values\n")
  beta.m <- beta.m[!na_rows, ]
}

# Use only CpGs present in both the reference and our data
common_cpgs <- intersect(rownames(beta.m), rownames(centDHSbloodDMC.m))
cat("Common CpGs with reference:", length(common_cpgs), "/", nrow(centDHSbloodDMC.m), "\n")
beta.m <- beta.m[common_cpgs, , drop = FALSE]

# Run EpiDISH (RPC method)
out.l <- epidish(beta.m = beta.m, ref.m = centDHSbloodDMC.m, method = "RPC")

# Save estimated cell fractions
estF <- out.l$estF
write.csv(estF, out_path)
cat("Cell type proportions saved to:", out_path, "\n")
cat("Dimensions:", nrow(estF), "samples x", ncol(estF), "cell types\n")
cat("Cell types:", colnames(estF), "\n")
cat("Proportion range:", round(range(estF), 4), "\n")
cat("Row sums range:", round(range(rowSums(estF)), 4), "\n")
