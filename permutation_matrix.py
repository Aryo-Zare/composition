

# %%

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import pingouin as pg
import numpy as np
import itertools # We'll use this to loop through pairs

# %%


# --- 1. Define columns and labels ---
columns_to_corr = [
    'bcs', 'fwp_d', 'fvp_ct', 'owp', 
    'leakage_average', 'bmi', 'wli'
]
df_to_corr = df_composition_6[columns_to_corr]

label_map = {
    'bcs': 'body condition score',
    'fwp_d': 'fat weight % ( dissection )',
    'fvp_ct': 'fat volume % ( CT )',
    'owp': 'oocyte weight %',
    'leakage_average': 'Leakage average',
    'bmi': 'BMI',
    'wli': 'weight_length index'
}
new_labels = [label_map[col] for col in columns_to_corr]


# --- 2. Get Correlations AND Permutation p-values ---

# --- Step 2a: Get the r-value matrix (the easy way) ---
# We still use this because its pairwise NaN handling is correct.
long_format_corrs = pg.pairwise_corr(df_to_corr, method='spearman')
corr_matrix_sparse = long_format_corrs.pivot(index='X', columns='Y', values='r')
corr_matrix = corr_matrix_sparse.combine_first(corr_matrix_sparse.T)
np.fill_diagonal(corr_matrix.values, 1)


# --- Step 2b: Get the p-value matrix (the permutation way) ---
print("Running permutation tests... (this may take a few seconds)")
# Create an empty DataFrame to store our p-values
p_values = pd.DataFrame(index=columns_to_corr, columns=columns_to_corr, dtype=float)

# Get all unique pairs of columns
pairs = list(itertools.combinations(columns_to_corr, 2))

# Loop through each pair
for col_a, col_b in pairs:
    # Drop NaNs *only* for this pair
    temp_df = df_to_corr[[col_a, col_b]].dropna()
    
    # Run the permutation test
    test_result = pg.permutation_test(
        temp_df[col_a], 
        temp_df[col_b], 
        method='spearman',
        n_resamples=1000, # 1000 is a good start, increase for more accuracy
        seed=42
    )
    
    # Get the p-value
    p = test_result['p-val'].iloc[0]
    
    # Store it in our matrix (both sides)
    p_values.loc[col_a, col_b] = p
    p_values.loc[col_b, col_a] = p

# Fill the diagonal with 1s
np.fill_diagonal(p_values.values, 1)
print("...Permutation tests complete.")


# --- 3. Create a custom annotation matrix (This code is unchanged) ---
labels = corr_matrix.round(2).astype(str)

for col in p_values.columns:
    for idx in p_values.index:
        p = p_values.loc[idx, col]
        if idx != col: 
            if p < 0.001:
                labels.loc[idx, col] += '***'
            elif p < 0.01:
                labels.loc[idx, col] += '**'
            elif p < 0.05:
                labels.loc[idx, col] += '*'


# --- 4. Plot the heatmap (This code is unchanged) ---
plt.figure(figsize=(12, 10))
ax = sns.heatmap(
    corr_matrix, 
    annot=labels,     
    fmt='',           
    cmap='coolwarm',
    vmin=-1, vmax=1,
    
    xticklabels=new_labels,
    yticklabels=new_labels,
    annot_kws={"size": 9} 
)

plt.xticks(rotation=45, ha='right')
plt.yticks(rotation=0)
ax.set_title('Spearman Correlation (with Permutation p-values)', fontsize=16)
plt.tight_layout()

# %%


