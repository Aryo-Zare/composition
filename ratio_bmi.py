
# %%


# %%

# --- PLOT 1: Plotting with 'bcs' on Y-axis ---

x_variables = ['fwp_d' , 'fvp_ct' , 'owp', 'leakage_average']  # , 'fvp_ct'
y_variable_to_plot = 'bmi'


# %%'

# --- Create the 2x2 Plot Grid ---
fig, axes = plt.subplots( 2, 2, figsize=(12, 12))
axes = axes.flatten() # Makes looping easy

# %%'

for i, x_var in enumerate(x_variables):
    ax = axes[i]
    
    # --- FIX 1: FILTER THE DATA ---
    # Create a temporary dataframe for *this subplot*
    plot_data = df_composition_6.copy()
    
    if x_var == 'leakage_average':
        # Remove the outlier before plotting or calculating stats
        # there is a far outlier ( sample_id 65 in Leonie's table ) in 'leakage_average'.
        plot_data = plot_data[plot_data[x_var] > -5].copy()
        # Set x-limit (still good practice for a clean look)
        ax.set_xlim(left=-1.5)
    
    # Individual data points
    sns.scatterplot(
                    data=plot_data, 
                    x=x_var, 
                    y=y_variable_to_plot, 
                    ax=ax, 
                    # alpha=0.5, 
                    # jitter=True, 
                    
                    # --- YOUR CHANGES ---
                    color='blue', # Fill color (e.g., 'blue', or a nicer blue)
                    edgecolor='gray',     # Edge color
                    linewidth=1,          # Width of the edge (needed to see it)
                    s=50               # Increased size 
    )
    
    
# %%  LOWESS

sns.regplot(
            data=df_composition_6.copy(), 
            x='owp', 
            y='bmi', 
            lowess=True,         # This tells seaborn to use a LOESS curve
            ci=None, 
            scatter=False,       # Don't re-plot the scatter points
            line_kws={
                        'color': 'red' , 
                        'linestyle': '--' ,
                        'lw' : 4 # width
                      } ,
            ax=axes[2]                # Plot on the same axis
)

# %%'
    
axes[0].set_title(f'Fat weight % ( dissection ) versus BMI', fontsize=18)
axes[1].set_title(f'Fat volume % ( CT ) versus BMI', fontsize=18)
axes[2].set_title(f'Oocyte weight % versus BMI', fontsize=18)
axes[3].set_title(f'Leakage average versus BMI', fontsize=18)

# %%'

axes[0].set_xlabel( 'Fat weight % ( dissection )' , fontsize=18 , loc='right' )
axes[1].set_xlabel( 'Fat volume % ( CT )' , fontsize=18 , loc='right' )
axes[2].set_xlabel( 'Oocyte weight % ' , fontsize=18 , loc='right' )
axes[3].set_xlabel( 'Leakage average (μA)' , fontsize=18 , loc='right' )

# %%'

for ax in axes :
    ax.set_ylabel( 'body mass index' , fontsize=18 , loc='top' )

# %%' add subplot indexing letters

# add subplot indexing letters.

# import string
letters = list( string.ascii_uppercase )  # ['A','B','C','D',...]

# ha , va : text alignment relative to the (x, y) coordinates you gave :
    # ha='right' means the right edge of the letter is anchored at x=-0.1.
    # va='bottom' means the bottom edge of the letter is anchored at y=1.05.
# That combination places the letter just above and slightly to the left of the subplot, with the text extending leftward and upward from that anchor point.
for ax , letter in zip( axes , letters ):
    ax.text(                           # the most important part !
            -0.1, 1.05, letter,        # position relative to each axis.
            transform=ax.transAxes,    # use axes fraction coords
            fontsize=20, fontweight='bold',
            va='bottom', ha='right'
    )


# %%'

plt.suptitle(  'Distribution of various parameters in relation to body mass index (BMI)' , fontsize=20 )

plt.tight_layout()

# %%'

# --- PLOT 2: Plotting with 'sex' on Y-axis ---

# To create a new plot, you just change one line and rerun!
# (Assuming 'sex' is in df_subset)
y_variable_to_plot = 'sex' 
# ... (rest of the code is the same)

# %%'

plt.savefig( r'F:\OneDrive - Uniklinik RWTH Aachen\DEXA\composition\plot\ratio_bmi_LOWESS.pdf' )
plt.savefig( r'F:\OneDrive - Uniklinik RWTH Aachen\DEXA\composition\plot\ratio_bmi_LOWESS.svg' )

# %%



# %%

