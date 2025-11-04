
# %%' bcs

# --- Your Wide-Format DataFrame ---

# %%' fat , oocyte , leakage  -  bcs

# 'bcs' column has NaN values that get irrelevantly plotted on the y axis as a separate category.
# hence, you should remnove them 1st :

# df_plot_bcs =  df_composition_6.dropna( subset='bcs' ).copy()

# %%'

# 'bcs' column has NaN values that get irrelevantly plotted on the y axis as a separate category.
# hence, you should remnove them 1st :
# note : you can not remove string 'nan' by the drop-na method !

# Select rows where 'bcs_str' is NOT 'nan' and make a new dataframe
mask_nan_string = df_composition_7['bcs_Int64_str'] != 'nan'
df_plot_bcs = df_composition_7[ mask_nan_string ].copy()

df_plot_bcs['bcs_Int64_str'].unique()
    # Out[28]: 
    # ['1', '5', '4', '3', '2']
    # Categories (6, object): ['1' < '2' < '3' < '4' < '5' < 'nan']

# Remove any categories that no longer have data
# without doing this, seaborn still plots the 'nan' at the y-axis as an empty row !
df_plot_bcs['bcs_Int64_str'] = df_plot_bcs['bcs_Int64_str'].cat.remove_unused_categories()

df_plot_bcs['bcs_Int64_str'].unique()
    # Out[38]: 
    # ['1', '5', '4', '3', '2']
    # Categories (5, object): ['1' < '2' < '3' < '4' < '5']

# %%'

# --- PLOT 1: Plotting with 'bcs' on Y-axis ---

x_variables = ['fwp_d' , 'owp', 'leakage_average']  # , 'fvp_ct'
y_variable_to_plot = 'bcs_Int64_str'

# y_order = sorted( df_plot_bcs['bcs_str'].unique() )

# %%'

# --- Create the 2x2 Plot Grid ---
fig, axes = plt.subplots( 3, 1, figsize=(12, 12))
axes = axes.flatten() # Makes looping easy

# %%'

for i, x_var in enumerate(x_variables):
    ax = axes[i]
    
    # --- FIX 1: FILTER THE DATA ---
    # Create a temporary dataframe for *this subplot*
    plot_data = df_plot_bcs.copy()
    
    if x_var == 'leakage_average':
        # Remove the outlier before plotting or calculating stats
        # there is a far outlier ( sample_id 65 in Leonie's table ) in 'leakage_average'.
        plot_data = plot_data[plot_data[x_var] > -5].copy()
        # Set x-limit (still good practice for a clean look)
        ax.set_xlim(left=-1.5)
    
    # Individual data points
    sns.stripplot(
                    data=plot_data, 
                    x=x_var, 
                    y=y_variable_to_plot, 
                    ax=ax, 
                    alpha=0.5, 
                    jitter=True, 
                    
                    # --- YOUR CHANGES ---
                    color='blue', # Fill color (e.g., 'blue', or a nicer blue)
                    edgecolor='gray',     # Edge color
                    linewidth=1,          # Width of the edge (needed to see it)
                    size=6               # Increased size (you had size=3) 
    )
    
    
    # 
    sns.pointplot(
                    data=plot_data, 
                    x=x_var, 
                    y=y_variable_to_plot, 
                    ax=ax, 
                    color='black',      # This forces all markers/bars to be black
                    # palette='muted',
                    
                    linestyle="none" , # this cancels connecting the points !
                    marker="|", 
                    markersize=20, 
                    markeredgewidth=5,
                    errorbar='sd',
                    
    )


# the trend line ( connecting the means ).
# this should be called separately if you want to plot the trend line & mean+sd lines in different colors.    
    sns.pointplot(
                    data=plot_data, 
                    x=x_var, 
                    y=y_variable_to_plot, 
                    ax=ax, 
                    color='red',      # This forces all markers/bars to be black
                    # palette='muted',
                    
                    linestyle="--" , # this cancels connecting the points !
                    marker=None, 
                    errorbar=None
                    
    )

    
    
    # for 'bcs' to ascend from bottom to top !
    ax.invert_yaxis()
    
# %%'
    
axes[0].set_title(f'Distribution of fat weight % ( dissection ) by body condition score', fontsize=18)
axes[1].set_title(f'Distribution of oocyte weight % by body condition score', fontsize=18)
axes[2].set_title(f'Distribution of leakage average by body condition score', fontsize=18)

# %%'

axes[0].set_xlabel( 'fat weight % ( dissection )' , fontsize=18 , loc='right' )
axes[1].set_xlabel( 'oocyte weight % ' , fontsize=18 , loc='right' )
axes[2].set_xlabel( 'leakage average (μA)' , fontsize=18 , loc='right' )

# %%'

axes[0].set_ylabel( 'body condition score' , fontsize=16)
axes[1].set_ylabel( 'body condition score' , fontsize=16)
axes[2].set_ylabel( 'body condition score' , fontsize=16)

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

plt.suptitle(  'Distribution of various parameters in relation to body condition score' , fontsize=20 )

plt.tight_layout()

# %%'

# --- PLOT 2: Plotting with 'sex' on Y-axis ---

# To create a new plot, you just change one line and rerun!
# (Assuming 'sex' is in df_subset)
y_variable_to_plot = 'sex' 
# ... (rest of the code is the same)

# %%'

plt.savefig( r'F:\OneDrive - Uniklinik RWTH Aachen\DEXA\composition\plot\bcs_7.pdf' )
plt.savefig( r'F:\OneDrive - Uniklinik RWTH Aachen\DEXA\composition\plot\bcs_7.svg' )

# %%

plt.savefig( r'F:\OneDrive - Uniklinik RWTH Aachen\DEXA\composition\plot\bcs_trend.pdf' )
plt.savefig( r'F:\OneDrive - Uniklinik RWTH Aachen\DEXA\composition\plot\bcs_trend.svg' )


# %%'
# %% bmi - bcs

# single plot.

fig, ax = plt.subplots( figsize=(10, 7) ) 

# Individual data points
sns.stripplot(
                data=df_plot_bcs, 
                x='bmi', 
                y='bcs_Int64_str', 
                ax=ax, 
                alpha=0.5, 
                jitter=True, 
                
                # --- YOUR CHANGES ---
                color='blue', # Fill color (e.g., 'blue', or a nicer blue)
                edgecolor='gray',     # Edge color
                linewidth=1,          # Width of the edge (needed to see it)
                size=6               # Increased size (you had size=3) 
)


# mean & SD
sns.pointplot(
                data=df_plot_bcs, 
                x='bmi', 
                y='bcs_Int64_str', 
                ax=ax, 
                color='black',      # This forces all markers/bars to be black
                # palette='muted',
                
                linestyle="none" , # this cancels connecting the points !
                marker="|", 
                markersize=20, 
                markeredgewidth=5,
                errorbar='sd'
)


# the trend line ( connecting the means ).
# this should be called separately if you want to plot the trend line & mean+sd lines in different colors.
sns.pointplot(
                data=df_plot_bcs, 
                x='bmi', 
                y='bcs_Int64_str', 
                ax=ax, 
                color='red',      # the connecting ( trend ) line will be red.
                # palette='muted',
                
                linestyle="--" , #: this cancels connecting the points !
                marker=None, 
                errorbar=None
)

ax.invert_yaxis()

# note : if you pass : errorbar='none' instead of : None : the following error arises :
    # ValueError: The value for `errorbar` must be one of ['ci', 'pi', 'se', 'sd'], but 'None' was passed.

# %%'

ax.set_xlabel( 'Body mass index' , fontsize=18 , loc='right' )

ax.set_ylabel( 'body condition score' , fontsize=18)

ax.set_title(f'Distribution of Body mass index versus body condition score', fontsize=20)

plt.tight_layout()

# %%'

plt.savefig( r'F:\OneDrive - Uniklinik RWTH Aachen\DEXA\composition\plot\bmi_bcs_3.pdf' )
plt.savefig( r'F:\OneDrive - Uniklinik RWTH Aachen\DEXA\composition\plot\bmi_bcs_3.svg' )

# %%


plt.savefig( r'F:\OneDrive - Uniklinik RWTH Aachen\DEXA\composition\plot\bmi_bcs_trend.pdf' )
plt.savefig( r'F:\OneDrive - Uniklinik RWTH Aachen\DEXA\composition\plot\bmi_bcs_trend.svg' )


# %%'


