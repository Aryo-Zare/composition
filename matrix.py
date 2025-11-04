

# %%''

list ( df_composition_6.columns )
    # Out[29]: 
    # ['species',
    #  'sex',
    #  'animal_id',
    #  'condition',
    #  'day',
    #  'repetition',
    #  'date',
    #  'bcs',
    #  'bw',
    #  'ncl',
    #  'fatbody',
    #  'fatbody_censored',
    #  'oocytes',
    #  'oocytes_censored',
    #  'fat_volume_ct',
    #  'body_volume_ct',
    #  'fwp_d',
    #  'fvp_ct',
    #  'bmi',
    #  'owp',
    #  'wli',
    #  'leakage_average',
    #  'bcs_str'
    #  'bcs_Int64',
    #  'bcs_Int64_str']           



df_composition_6.dtypes
    # Out[39]: 
    # species              object
    # sex                 float64
    # animal_id            object
    # condition            object
    # day                 float64
    # repetition          float64
    # date                 object
    # bcs                 float64
    # bw                  float64
    # ncl                 float64
    # fatbody             float64
    # fatbody_censored    float64
    # oocytes             float64
    # oocytes_censored    float64
    # fat_volume_ct       float64
    # body_volume_ct      float64
    # fwp_d               float64
    # fvp_ct              float64
    # bmi                 float64
    # owp                 float64
    # wli                 float64
    # leakage_average     float64
    # bcs_str              object
    # bcs_Int64              Int64
    # bcs_Int64_str       category
    # dtype: object

# %%''
# %%'' Pandas correlation

# --- 1. Your existing correlation matrix ---
# (Assuming df_composition_6 is loaded)
columns_to_corr = [
                    'bcs',
                    'fwp_d',
                    'fvp_ct',
                    'owp',
                    'leakage_average',
                    'bmi',
                    'wli'   
]

corr_matrix = df_composition_6[columns_to_corr].corr(method='spearman')

corr_matrix
    # Out[28]: 
    #                       bcs     fwp_d    fvp_ct       owp  leakage_average  \
    # bcs              1.000000 -0.055174 -0.235903  0.653528        -0.151952   
    # fwp_d           -0.055174  1.000000  0.816883 -0.103640        -0.245165   
    # fvp_ct          -0.235903  0.816883  1.000000 -0.700000        -0.200000   
    # owp              0.653528 -0.103640 -0.700000  1.000000         0.071199   
    # leakage_average -0.151952 -0.245165 -0.200000  0.071199         1.000000   
    # bmi              0.742163 -0.231049 -0.511688  0.565642        -0.054347   
    # wli              0.257611  0.357996  0.141558  0.369863        -0.060157   
    
    #                       bmi       wli  
    # bcs              0.742163  0.257611  
    # fwp_d           -0.231049  0.357996  
    # fvp_ct          -0.511688  0.141558  
    # owp              0.565642  0.369863  
    # leakage_average -0.054347 -0.060157  
    # bmi              1.000000  0.306074  
    # wli              0.306074  1.000000  


# --- 2. Define the new, full-text labels ---
# We create a dictionary to map short names to long names
label_map = {
            'bcs': 'body condition score',
            'fwp_d': 'fat weight % ( dissection )',
            'fvp_ct': 'fat volume % ( CT )',
            'owp': 'oocyte weight %',
            'leakage_average': 'Leakage average',
            'bmi': 'BMI',
            'wli': 'weight_length index'
}

# Create the list of labels *in the same order* as your matrix
new_labels = [label_map[col] for col in corr_matrix.columns]


# new_labels
    # Out[15]: 
    # ['body condition score',
    #  'fat weight % ( dissection )',
    #  'fat volume % ( CT )',
    #  'oocyte weight %',
    #  'Leakage average',
    #  'BMI',
    #  'weight_length index']


# --- 3. Create the plot with all your modifications ---

# Request #3: Define the size of the figure
plt.figure(figsize=(14, 12)) # (width, height) in inches

# Draw the heatmap
ax = sns.heatmap(
                    corr_matrix, 
                    annot=True, 
                    cmap='coolwarm',
                    
                    # Request #1: Use the new, long labels
                    xticklabels=new_labels,
                    yticklabels=new_labels,
                    
                    # Request #4: Decrease font size of numbers inside
                    annot_kws={"size": 13} # You can change 9 to 8 or 10
)

# Request #2: Rotate x-axis labels
# We use plt.xticks() to adjust the x-axis properties
plt.xticks(rotation=45, ha='right') # 'ha' (horizontal alignment) is key

# Also ensure y-axis labels are horizontal
plt.yticks(rotation=0)

# Add a title
ax.set_title('Pairwise Spearman ranked correlation coefficients \n', fontsize=20)

# CRITICAL: Use tight_layout() to make room for the long labels
plt.tight_layout()


# %%''


plt.savefig( r'F:\OneDrive - Uniklinik RWTH Aachen\DEXA\composition\plot\corr_matrix_3.pdf' )
plt.savefig( r'F:\OneDrive - Uniklinik RWTH Aachen\DEXA\composition\plot\corr_matrix_3.svg' )


# %%''
# %% pingouin correlation

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import pingouin as pg  # <-- Import pingouin
import numpy as np

# %%'

# --- 1. Define columns and labels (from your previous work) ---
columns_to_corr = [
                    'bcs',
                    'fwp_d',
                    'fvp_ct',
                    'owp',
                    'leakage_average',
                    'bmi',
                    'wli'   
]


# (Make sure df_composition_6 is loaded)
df_to_corr = df_composition_7[columns_to_corr]

# df_to_corr.shape
    # Out[49]: (101, 7)

label_map = {
            'bcs': 'body condition score',
            'fwp_d': 'fat weight % ( dissection )',
            'fvp_ct': 'fat volume % ( CT )',
            'owp': 'oocyte weight %',
            'leakage_average': 'Leakage average',
            'bmi': 'BMI',
            'wli': 'weight_length index'
}

# %%' alternative Pingouin function

# don't use.
# alternative Pingouin function
    # just to test the other function.
    # the output of this function deems to be difficlt to modify for my purpose.
    
    
                # # --- 2. Get Correlations AND p-values using pingouin ---
                # # This one command does all the work, handling NaNs correctly
                # corr_results = pg.rcorr(df_to_corr, method='spearman')
                
                
                # # explore
                # corr_results
                #     # Out[15]: 
                #     #                     bcs   fwp_d  fvp_ct    owp leakage_average    bmi  wli
                #     # bcs                   -                    ***                    ***    *
                #     # fwp_d            -0.055       -     ***                             *  ***
                #     # fvp_ct           -0.236   0.817       -                             *     
                #     # owp               0.654  -0.104    -0.7      -                    ***   **
                #     # leakage_average  -0.152  -0.245    -0.2  0.071               -            
                #     # bmi               0.742  -0.231  -0.512  0.566          -0.054      -   **
                #     # wli               0.258   0.358   0.142   0.37           -0.06  0.306    -
                
                # type(corr_results)
                #     # Out[16]: pandas.core.frame.DataFrame
                
                # corr_results.shape
                #     # Out[17]: (7, 7)
                
                # corr_results.columns
                #     # Out[18]: Index(['bcs', 'fwp_d', 'fvp_ct', 'owp', 'leakage_average', 'bmi', 'wli'], dtype='object')


# %%'


# --- 2. Get Correlations in Long-Format (This is the fix) ---
# This calculates all pairs, handling NaNs, and gives r and p-val.
long_format_corrs = pg.pairwise_corr(df_to_corr, method='spearman')

long_format_corrs
    # Out[23]: 
    #                   X                Y    method alternative   n         r  \
    # 0               bcs            fwp_d  spearman   two-sided  84 -0.055174   
    # 1               bcs           fvp_ct  spearman   two-sided  21 -0.235903   
    # 2               bcs              owp  spearman   two-sided  77  0.653528   
    # 3               bcs  leakage_average  spearman   two-sided  63 -0.151952   
    # 4               bcs              bmi  spearman   two-sided  92  0.742163   
    # 5               bcs              wli  spearman   two-sided  92  0.257611   
    # 6             fwp_d           fvp_ct  spearman   two-sided  21  0.816883   
    # 7             fwp_d              owp  spearman   two-sided  67 -0.103640   
    # 8             fwp_d  leakage_average  spearman   two-sided  60 -0.245165   
    # 9             fwp_d              bmi  spearman   two-sided  82 -0.231049   
    # 10            fwp_d              wli  spearman   two-sided  82  0.357996   
    # 11           fvp_ct              owp  spearman   two-sided   5 -0.700000   
    # 12           fvp_ct  leakage_average  spearman   two-sided   5 -0.200000   
    # 13           fvp_ct              bmi  spearman   two-sided  21 -0.511688   
    # 14           fvp_ct              wli  spearman   two-sided  21  0.141558   
    # 15              owp  leakage_average  spearman   two-sided  63  0.071199   
    # 16              owp              bmi  spearman   two-sided  74  0.565642   
    # 17              owp              wli  spearman   two-sided  74  0.369863   
    # 18  leakage_average              bmi  spearman   two-sided  63 -0.054347   
    # 19  leakage_average              wli  spearman   two-sided  63 -0.060157   
    # 20              bmi              wli  spearman   two-sided  92  0.306074   
    
    #              CI95%    p-unc    power  
    # 0    [-0.27, 0.16] 0.618145 0.078851  
    # 1    [-0.61, 0.22] 0.303259 0.179830  
    # 2      [0.5, 0.77] 0.000000 0.999999  
    # 3     [-0.39, 0.1] 0.234499 0.222508  
    # 4     [0.63, 0.82] 0.000000 1.000000  
    # 5     [0.06, 0.44] 0.013170 0.704789  
    # 6      [0.6, 0.92] 0.000006 0.998598  
    # 7    [-0.34, 0.14] 0.403936 0.133143  
    # 8    [-0.47, 0.01] 0.059024 0.477287  
    # 9   [-0.43, -0.01] 0.036756 0.556650  
    # 10    [0.15, 0.53] 0.000959 0.917341  
    # 11   [-0.98, 0.48] 0.188120 0.279784  
    # 12   [-0.92, 0.83] 0.747060 0.065341  
    # 13   [-0.77, -0.1] 0.017736 0.686292  
    # 14   [-0.31, 0.54] 0.540488 0.093943  
    # 15   [-0.18, 0.31] 0.579229 0.085861  
    # 16     [0.39, 0.7] 0.000000 0.999742  
    # 17    [0.15, 0.55] 0.001181 0.908425  
    # 18     [-0.3, 0.2] 0.672264 0.070602  
    # 19    [-0.3, 0.19] 0.639541 0.075372  
    # 20    [0.11, 0.48] 0.003005 0.850253  

long_format_corrs.columns
    # Out[24]: Index(['X', 'Y', 'method', 'alternative', 'n', 'r', 'CI95%', 'p-unc', 'power'], dtype='object')

# %%'

# --- 3. Pivot to get the R-value matrix ---
# This creates a matrix with r-values in the lower-left
corr_matrix_sparse = long_format_corrs.pivot(index='X', columns='Y', values='r')


# corr_matrix_sparse
    # Out[41]: 
    # Y                     bmi    fvp_ct     fwp_d  leakage_average       owp  \
    # X                                                                          
    # bcs              0.742163 -0.235903 -0.055174        -0.151952  0.653528   
    # bmi                   NaN       NaN       NaN              NaN       NaN   
    # fvp_ct          -0.511688       NaN       NaN        -0.200000 -0.700000   
    # fwp_d           -0.231049  0.816883       NaN        -0.245165 -0.103640   
    # leakage_average -0.054347       NaN       NaN              NaN       NaN   
    # owp              0.565642       NaN       NaN         0.071199       NaN   
    
    # Y                     wli  
    # X                          
    # bcs              0.257611  
    # bmi              0.306074  
    # fvp_ct           0.141558  
    # fwp_d            0.357996  
    # leakage_average -0.060157  
    # owp              0.369863  


# We make it symmetrical by copying the lower triangle to the upper
    # symmetrical : like the symmetrical color matrix ( each correlation is repeated once symmetrically along the diagonal line ).
corr_matrix = corr_matrix_sparse.combine_first(corr_matrix_sparse.T)

# Create the list of labels *in the same order* as your matrix
new_labels = [ label_map[col] for col in corr_matrix.columns ]

# %%'

# explore
corr_matrix
    # Out[46]: 
    #                       bcs       bmi    fvp_ct     fwp_d  leakage_average  \
    # bcs                   NaN  0.779040 -0.235903 -0.055174        -0.151952   
    # bmi              0.779040       NaN -0.511688 -0.231049        -0.054347   
    # fvp_ct          -0.235903 -0.511688       NaN  0.816883        -0.200000   
    # fwp_d           -0.055174 -0.231049  0.816883       NaN        -0.245165   
    # leakage_average -0.151952 -0.054347 -0.200000 -0.245165              NaN   
    # owp              0.653528  0.565642 -0.700000 -0.103640         0.071199   
    # wli              0.379163  0.557132  0.141558  0.357996        -0.060157   
    
    #                       owp       wli  
    # bcs              0.653528  0.379163  
    # bmi              0.565642  0.557132  
    # fvp_ct          -0.700000  0.141558  
    # fwp_d           -0.103640  0.357996  
    # leakage_average  0.071199 -0.060157  
    # owp                   NaN  0.369863  
    # wli              0.369863       NaN   

# %%'

# Fill the diagonal with 1s
np.fill_diagonal(corr_matrix.values, 1)

# --- 4. Pivot to get the P-value matrix ---
p_values_sparse = long_format_corrs.pivot(index='X', columns='Y', values='p-unc')
# Make it symmetrical
p_values = p_values_sparse.combine_first(p_values_sparse.T)
# Fill the diagonal (value doesn't matter, our loop skips it)
np.fill_diagonal(p_values.values, 1)

# %%'

# --- 5. Create a custom annotation matrix (This code is now correct) ---
labels = corr_matrix.round(2).astype(str)

for col in p_values.columns:
    for idx in p_values.index:
        p = p_values.loc[idx, col]
        if idx != col: # Don't add stars to the diagonal
            if p < 0.001:
                labels.loc[idx, col] += ' ***'
            elif p < 0.01:
                labels.loc[idx, col] += ' **'
            elif p < 0.05:
                labels.loc[idx, col] += ' *'

# %%'

# explore

# labels
    # Out[43]: 
    #                       bcs       bmi    fvp_ct     fwp_d leakage_average  \
    # bcs                   1.0  0.74 ***     -0.24     -0.06           -0.15   
    # bmi              0.74 ***       1.0   -0.51 *   -0.23 *           -0.05   
    # fvp_ct              -0.24   -0.51 *       1.0  0.82 ***            -0.2   
    # fwp_d               -0.06   -0.23 *  0.82 ***       1.0           -0.25   
    # leakage_average     -0.15     -0.05      -0.2     -0.25             1.0   
    # owp              0.65 ***  0.57 ***      -0.7      -0.1            0.07   
    # wli                0.26 *   0.31 **      0.14  0.36 ***           -0.06   
    
    #                       owp       wli  
    # bcs              0.65 ***    0.26 *  
    # bmi              0.57 ***   0.31 **  
    # fvp_ct               -0.7      0.14  
    # fwp_d                -0.1  0.36 ***  
    # leakage_average      0.07     -0.06  
    # owp                   1.0   0.37 **  
    # wli               0.37 **       1.0  

# %%'

# --- 6. Plot the heatmap (This code is also correct) ---
plt.figure(figsize=(12, 10))
ax = sns.heatmap(
                    corr_matrix, 
                    annot=labels,     # Use our new custom labels (e.g., "0.75 ***")
                    fmt='',           # IMPORTANT: Set fmt='' to use string annotations
                    
                    cmap='coolwarm',
                    vmin=-1, 
                    vmax=1,
                    
                    xticklabels=new_labels,
                    yticklabels=new_labels,
                    annot_kws={"size": 11} 
)

plt.xticks(rotation=45, ha='right')
plt.yticks(rotation=0)
ax.set_title(' Pairwise Spearman ranked correlation coefficients \n', fontsize=20)
plt.tight_layout()


# %%'

plt.savefig( r'F:\OneDrive - Uniklinik RWTH Aachen\DEXA\composition\plot\corr_matrix_6.pdf' )
plt.savefig( r'F:\OneDrive - Uniklinik RWTH Aachen\DEXA\composition\plot\corr_matrix_6.svg' )


# %%'

