

# %%'

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

# %%'
# %%' correlation

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


# %%'


plt.savefig( r'F:\OneDrive - Uniklinik RWTH Aachen\DEXA\composition\plot\corr_matrix_3.pdf' )
plt.savefig( r'F:\OneDrive - Uniklinik RWTH Aachen\DEXA\composition\plot\corr_matrix_3.svg' )


# %%'
# %%' bcs

# --- Your Wide-Format DataFrame ---

# %%' fat , oocyte , leakage  -  bcs

# 'bcs' column has NaN values that get irrelevantly plotted on the y axis as a separate category.
# hence, you should remnove them 1st :

df_plot_bcs =  df_composition_6.dropna( subset='bcs' ).copy()

# %%'

# --- PLOT 1: Plotting with 'bcs' on Y-axis ---

x_variables = ['fwp_d' , 'owp', 'leakage_average']  # , 'fvp_ct'
y_variable_to_plot = 'bcs_str'

y_order = sorted( df_plot_bcs['bcs_str'].unique() )

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
                    order=y_order ,
                    
                    # --- YOUR CHANGES ---
                    color='blue', # Fill color (e.g., 'blue', or a nicer blue)
                    edgecolor='gray',     # Edge color
                    linewidth=1,          # Width of the edge (needed to see it)
                    size=6               # Increased size (you had size=3) 
    )
    
    
    # Violin Plot (KDE)
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
                    
                    order=y_order
    )

    
    # for 'bcs' to ascend from bottom to top !
    ax.invert_yaxis()
    
# %%'
    
axes[0].set_title(f'Distribution of fat weight % ( dissection ) by body condition score', fontsize=14)
axes[1].set_title(f'Distribution of oocyte weight % by body condition score', fontsize=14)
axes[2].set_title(f'Distribution of leakage average by body condition score', fontsize=14)

# %%'

axes[0].set_xlabel( 'fat weight % ( dissection )' , fontsize=14 , loc='right' )
axes[1].set_xlabel( 'oocyte weight % ' , fontsize=14 , loc='right' )
axes[2].set_xlabel( 'leakage average' , fontsize=14 , loc='right' )

# %%'

axes[0].set_ylabel( 'body condition score' , fontsize=14)
axes[1].set_ylabel( 'body condition score' , fontsize=16)
axes[2].set_ylabel( 'body condition score' , fontsize=14)

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

plt.savefig( r'F:\OneDrive - Uniklinik RWTH Aachen\DEXA\composition\plot\bcs_6.pdf' )
plt.savefig( r'F:\OneDrive - Uniklinik RWTH Aachen\DEXA\composition\plot\bcs_6.svg' )


# %%'
# %% bmi - bcs

# 'bcs' column has NaN values that get irrelevantly plotted on the y axis as a separate category.
# hence, you should remnove them 1st :
# note : you can not remove string 'nan' by the drop-na method !

    
# Select rows where 'bcs_str' is NOT 'nan' and make a new dataframe
mask_nan_string = df_composition_6['bcs_Int64_str'] != 'nan'
df_plot_bcs = df_composition_6[ mask_nan_string ].copy()

df_plot_bcs['bcs_Int64_str'].unique()
    # Out[28]: 
    # ['1', '5', '4', '3', '2']
    # Categories (6, object): ['1' < '2' < '3' < '4' < '5' < 'nan']

# Remove any categories that no longer have data
# without doing this, seaborn still plots the 'nan' at the y-axis as an empty row !
df_plot_bcs['bcs_Int64_str'] = df_plot_bcs['bcs_Int64_str'].cat.remove_unused_categories()

df_plot_bcs['bcs_Int64_str'].unique()
    # Out[33]: 
    # ['1', '5', '4', '3', '2']
    # Categories (5, object): ['1' < '2' < '3' < '4' < '5']



# %%'

fig, ax = plt.subplots( figsize=(8, 6) ) 

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


# Violin Plot (KDE)
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
                errorbar='sd',

)


ax.invert_yaxis()

# %%'

ax.set_xlabel( 'Body mass index' , fontsize=18 , loc='right' )

ax.set_ylabel( 'body condition score' , fontsize=18)

ax.set_title(f'Distribution of Body mass index versus body condition score', fontsize=20)

plt.tight_layout()

# %%'

plt.savefig( r'F:\OneDrive - Uniklinik RWTH Aachen\DEXA\composition\plot\bmi_bcs.pdf' )
plt.savefig( r'F:\OneDrive - Uniklinik RWTH Aachen\DEXA\composition\plot\bmi_bcs.svg' )


# %%


