
# %%

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import itertools  # We'll use this to create the pairs
import string     # For the subplot letters [cite: 27]

# %%

# --- Setup ---
# Assuming 'df_composition_6' is your main DataFrame 

# 1. Define the variables and their pretty names
plot_vars = ['fwp_d', 'fvp_ct', 'owp', 'leakage_average']

# for AUTOMATIC assignment of text on axes & subplot titles.
label_map = {
                'fwp_d': 'Fat weight % ( dissection )',
                'fvp_ct': 'Fat volume % ( CT )',
                'owp': 'Oocyte weight %',
                'leakage_average': 'Leakage average (μA)'
}

# 2. Automatically create all 6 unique pairs
# (e.g., ('fwp_d', 'fvp_ct'), ('fwp_d', 'owp'), ...)
pairs = list(itertools.combinations(plot_vars, 2))

# --- Create the 2x3 Plot Grid ---
# We have 6 plots, so a 2x3 grid is perfect
fig, axes = plt.subplots(2, 3, figsize=(18, 10))
axes = axes.flatten() # Makes looping easy

# --- Loop through each PAIR ---

for i, (x_var, y_var) in enumerate(pairs):
    ax = axes[i]
    
    # --- Filter Data (from your script) ---
    plot_data = df_composition_6.copy()
    
    # Check if *either* variable is leakage_average to filter [cite: 18, 19]
    if x_var == 'leakage_average' or y_var == 'leakage_average':
        # Remove the outlier before plotting [cite: 19]
        plot_data = plot_data[plot_data['leakage_average'] > -5].copy()
        
        # Also adjust the limits if this variable is on an axis
        if x_var == 'leakage_average':
            ax.set_xlim(left=-1.5)
        if y_var == 'leakage_average':
            ax.set_ylim(bottom=-1.5)
    
    # --- Individual data points ---
    sns.scatterplot(
                    data=plot_data, 
                    x=x_var, 
                    y=y_var, 
                    ax=ax, 
                    color='blue',       # Style from your script [cite: 21]
                    edgecolor='gray',   # Style from your script [cite: 21]
                    linewidth=1,        # Style from your script [cite: 21]
                    s=50                # Style from your script [cite: 22]
    )
    
    # --- Set Labels using the map ---
    ax.set_xlabel(label_map[x_var], fontsize=12)
    ax.set_ylabel(label_map[y_var], fontsize=12)
    ax.set_title(f'{label_map[y_var]} vs. {label_map[x_var]}', fontsize=14)

# --- Add subplot indexing letters ---
letters = list(string.ascii_uppercase) # [cite: 27]
for ax, letter in zip(axes, letters):
    ax.text(                           
            -0.1, 1.05, letter,            # Position [cite: 30]
            transform=ax.transAxes,        # Use axes fraction coords [cite: 30]
            fontsize=20, fontweight='bold', # Style [cite: 31]
            va='bottom', ha='right'        # Alignment [cite: 31]
    )

plt.tight_layout(rect=[0, 0, 1, 0.96]) # Add rect to make room for suptitle

plt.suptitle('Pairwise Scatterplots of Key Variables', fontsize=20)

# %%  LOWESS

sns.regplot(
            data=df_composition_6.copy(),  # don't put : plot_data : here.
                                                # it may have alread been filtered for : leakage !
            x='fwp_d', 
            y='fvp_ct', 
            lowess=True,         # This tells seaborn to use a LOESS curve
            ci=None, 
            scatter=False,       # Don't re-plot the scatter points
            line_kws={
                        'color': 'red' , 
                        'linestyle': '--' ,
                        'lw' : 4 # width
                      } ,
            ax=axes[0]                # Plot on the same axis
)


# as the LOESS plot overwrites the formerly assigned axis text.
axes[0].set_xlabel( 'Fat weight % ( dissection )' , fontsize=12 , loc='right' )
axes[0].set_ylabel( 'Fat volume % ( CT )' , fontsize=12 , loc='top' )


# %%

plt.savefig( r'F:\OneDrive - Uniklinik RWTH Aachen\DEXA\composition\plot\ratio_pairs_LOESS.pdf' )
plt.savefig( r'F:\OneDrive - Uniklinik RWTH Aachen\DEXA\composition\plot\ratio_pairs_LOESS.svg' )

# %%


