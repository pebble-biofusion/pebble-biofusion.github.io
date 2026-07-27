# adjust_beta_by_cell_composition.R
# Adjust GSE41037 beta values by regressing out estimated blood cell proportions
#
# Requires: estimate_cell_composition.R must be run first
#
# For each CpG: beta ~ B + NK + CD4T + CD8T + Mono + Neutro + Eosino
# Adjusted beta = residual + mean(beta_j)
#
# Usage: Rscript scripts/adjust_beta_by_cell_composition.R

# Paths
beta_path <- "results/tables/GSE41037_horvath_cpg_beta.csv"
celltypes_path <- "results/tables/GSE41037_estCellTypes.csv"
out_path <- "results/tables/GSE41037_adjustedbetas.csv"

# Read beta matrix
beta <- read.csv(beta_path, row.names = 1, check.names = FALSE)
cat("Beta matrix:", nrow(beta), "CpGs x", ncol(beta), "samples\n")

# Read cell type proportions
ct <- read.csv(celltypes_path, row.names = 1, check.names = FALSE)
cat("Cell types:", ncol(ct), "types x", nrow(ct), "samples\n")

# Ensure sample alignment
common_samples <- intersect(colnames(beta), rownames(ct))
cat("Common samples:", length(common_samples), "\n")
beta <- beta[, common_samples, drop = FALSE]
ct <- ct[common_samples, , drop = FALSE]

# For each CpG, fit linear model and get adjusted beta (residual + mean)
beta_mat <- as.matrix(beta)
adj_betas <- matrix(NA, nrow = nrow(beta_mat), ncol = ncol(beta_mat))
rownames(adj_betas) <- rownames(beta_mat)
colnames(adj_betas) <- colnames(beta_mat)

pb <- txtProgressBar(min = 0, max = nrow(beta_mat), style = 3)
for (i in seq_len(nrow(beta_mat))) {
  y <- beta_mat[i, ]
  valid <- !is.na(y)
  if (sum(valid) < 10) {
    adj_betas[i, ] <- NA
    next
  }

  # Fit linear model
  fit <- lm(y[valid] ~ B + NK + CD4T + CD8T + Mono + Neutro + Eosino,
            data = ct[valid, ])

  # Adjusted = residual + overall mean
  resid_vals <- residuals(fit)
  beta_mean <- mean(y, na.rm = TRUE)

  adj_betas[i, valid] <- resid_vals + beta_mean
  if (any(!valid)) {
    adj_betas[i, !valid] <- NA
  }
  setTxtProgressBar(pb, i)
}
close(pb)

# Write output
adj_df <- as.data.frame(adj_betas)
write.csv(adj_df, out_path)
cat("\nAdjusted beta matrix saved to:", out_path, "\n")

# Summary stats
adj_vals <- as.vector(adj_betas)
cat("Adjusted beta range: [", round(min(adj_vals, na.rm = TRUE), 4), ",",
    round(max(adj_vals, na.rm = TRUE), 4), "]\n")
cat("Adjusted beta mean:", round(mean(adj_vals, na.rm = TRUE), 4), "\n")

n_outside <- sum(adj_vals < 0 | adj_vals > 1, na.rm = TRUE)
cat("Values outside [0,1]:", n_outside, "/", sum(!is.na(adj_vals)),
    sprintf("(%.2f%%)", 100 * n_outside / sum(!is.na(adj_vals))), "\n")
