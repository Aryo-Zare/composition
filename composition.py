

# %%

import os

# %%


# --- Setup Paths ---

# Use a raw string (r"...") to correctly handle backslashes in Windows paths
folder_path = r"F:\OneDrive - Uniklinik RWTH Aachen\DEXA\composition"

# Create the full paths to the files
file1_path = os.path.join(folder_path, "P092_Talbot_Datei.xlsx")
file2_path = os.path.join(folder_path, "CT.xlsx")

# %%


# Use the 'sheet_name' parameter to load *only* the 'Data_query' sheet.
# 'header=0' tells pandas to use the first row (index 0) as the header, 
# which is the default behavior.
df_composition = pd.read_excel(file1_path, 
                          sheet_name='Data_query', 
                          header=0)

# C:\Users\azare\AppData\Local\miniconda3\envs\env_23\Lib\site-packages\openpyxl\worksheet\_read_only.py:85: 
#     UserWarning: Data Validation extension is not supported and will be removed
#   for idx, row in parser.parse():

# %%


# 'header=0' is also the default here.
df_ct = pd.read_excel(file2_path, 
                      header=0)
    

# %%
# %%

df_composition.shape
    # Out[17]: (271, 19)

df_composition[:4]
    # Out[15]: 
    #           species      sex animal_id condition      day  repetition  \
    # 0  Xenopus laevis 1.000000         1   Wiemuth 1.000000    1.000000   
    # 1  Xenopus laevis 1.000000         1   Wiemuth 1.000000    2.000000   
    # 2  Xenopus laevis 1.000000         1   Wiemuth 1.000000    3.000000   
    # 3  Xenopus laevis 1.000000         2   Wiemuth 1.000000    1.000000   
    
    #                   date      bcs   bw       ncl  fatbody  fatbody_censored  \
    # 0  2022-11-28 00:00:00 1.000000   77  9.500000 5.700000               NaN   
    # 1  2022-11-28 00:00:00      NaN  NaN       NaN      NaN               NaN   
    # 2  2022-11-28 00:00:00      NaN  NaN       NaN      NaN               NaN   
    # 3  2022-11-28 00:00:00 5.000000  194 13.200000 5.200000               NaN   
    
    #     oocytes  oocytes_censored  leakage  leakage_censored  Unnamed: 16  \
    # 0  3.700000               NaN      NaN          1.000000          NaN   
    # 1       NaN               NaN      NaN          1.000000          NaN   
    # 2       NaN               NaN      NaN          1.000000          NaN   
    # 3 47.700000               NaN 0.130000               NaN          NaN   
    
    #    Unnamed: 17 comment  
    # 0          NaN     NaN  
    # 1          NaN     NaN  
    # 2          NaN     NaN  
    # 3          NaN     NaN  


list( df_composition.columns )
Out[19]: 
['species',
 'sex',
 'animal_id',
 'condition',
 'day',
 'repetition',
 'date',
 'bcs',
 'bw',
 'ncl',
 'fatbody',
 'fatbody_censored',
 'oocytes',
 'oocytes_censored',
 'leakage',
 'leakage_censored',
 'Unnamed: 16',
 'Unnamed: 17',
 'comment']

# %%
# %%

df_ct
    # Out[20]: 
    #    Unnamed: 0     sex  fat body volume mm^3  body volume mm^3
    # 0    LT-KW-1x  female           1285.000000     119461.000000
    # 1    LT-KW-2x  female           3971.000000     108727.000000
    # 2    LT-KW-3x  female           6141.000000     151991.000000
    # 3    LT-KW-4x  female           2278.000000     104448.000000
    # 4    LT-KW-5x  female           4480.000000      85779.000000
    # 5    LT-KM-1x    male           1370.000000      44786.000000
    # 6    LT-KM-2x    male           1425.000000      28669.000000
    # 7    LT-KM-3x    male           1728.000000      32078.000000
    # 8    LT-KM-4x    male           1400.000000      30288.000000
    # 9    LT-KM-5x    male           2189.000000      39366.000000
    # 10   LT-KM-6x    male           1583.000000      37542.000000
    # 11   LT-KM-7x    male            819.000000      36769.000000
    # 12   LT-KM-8x    male           1588.000000      41833.000000
    # 13   LT-KM-9x    male           1804.000000      34536.000000
    # 14  LT-KM-10x    male           4469.000000      50685.000000
    # 15  LT-KM-11x    male           1628.000000      30501.000000
    # 16  LT-KM-12x    male           3255.000000      32800.000000
    # 17  LT-KM-13x    male           1708.000000      28313.000000
    # 18  LT-KM-14x    male           2385.000000      39840.000000
    # 19  LT-KM-15x    male           1763.000000      39073.000000
    # 20  LT-KM-16x    male           1726.000000      34441.000000
    # 21        NaN     NaN                   NaN               NaN
    # 22        NaN     NaN                   NaN               NaN
    # 23        NaN     NaN                   NaN               NaN
    # 24        NaN     NaN                   NaN               NaN
    # 25    LT-072x  female          17624.000000     168884.000000
    # 26    LT-073x  female           4199.000000     136315.000000
    # 27    LT-074x  female             66.000000      52080.000000

list( df_ct.columns )
    # Out[22]: ['animal_id', 'sex', 'fat body volume mm^3', 'body volume mm^3']

# %%

# .iloc[rows, columns]
# : means 'all rows'
# :-3 means 'all columns from the start up to, but not including, the last 3'

df_composition_2 = df_composition.iloc[:, :-3]


# Rename 'Unnamed: 0' to 'animal_id'
df_ct = df_ct.rename(columns={'Unnamed: 0': 'animal_id'})


df_ct = df_ct.rename( columns={
                                'fat body volume mm^3' : 'fat_volume_ct' , 
                                'body volume mm^3' : 'body_volume_ct' 
})

# %%

# Drop all rows that have one or more NaN values
df_ct = df_ct.dropna()

# Chain the prefix and suffix removals
df_ct['animal_id'] = df_ct['animal_id'].str.removeprefix('LT-').str.removesuffix('x')

# %%

df_ct
    # Out[26]: 
    #    animal_id     sex  fat_volume_ct  body_volume_ct
    # 0       KW-1  female    1285.000000   119461.000000
    # 1       KW-2  female    3971.000000   108727.000000
    # 2       KW-3  female    6141.000000   151991.000000
    # 3       KW-4  female    2278.000000   104448.000000
    # 4       KW-5  female    4480.000000    85779.000000
    # 5       KM-1    male    1370.000000    44786.000000
    # 6       KM-2    male    1425.000000    28669.000000
    # 7       KM-3    male    1728.000000    32078.000000
    # 8       KM-4    male    1400.000000    30288.000000
    # 9       KM-5    male    2189.000000    39366.000000
    # 10      KM-6    male    1583.000000    37542.000000
    # 11      KM-7    male     819.000000    36769.000000
    # 12      KM-8    male    1588.000000    41833.000000
    # 13      KM-9    male    1804.000000    34536.000000
    # 14     KM-10    male    4469.000000    50685.000000
    # 15     KM-11    male    1628.000000    30501.000000
    # 16     KM-12    male    3255.000000    32800.000000
    # 17     KM-13    male    1708.000000    28313.000000
    # 18     KM-14    male    2385.000000    39840.000000
    # 19     KM-15    male    1763.000000    39073.000000
    # 20     KM-16    male    1726.000000    34441.000000
    # 25       072  female   17624.000000   168884.000000
    # 26       073  female    4199.000000   136315.000000
    # 27       074  female      66.000000    52080.000000

# %%

# Strip all leading '0' characters from 'animal_id'
df_ct['animal_id'] = df_ct['animal_id'].str.lstrip('0')
    # Out[28]: 
    #    animal_id     sex  fat_volume_ct  body_volume_ct
    # 0       KW-1  female    1285.000000   119461.000000
    
    # ...
    
    # 20     KM-16    male    1726.000000    34441.000000
    # 25        72  female   17624.000000   168884.000000
    # 26        73  female    4199.000000   136315.000000
    # 27        74  female      66.000000    52080.000000

# %%

df_ct.to_pickle( r'F:\OneDrive - Uniklinik RWTH Aachen\DEXA\composition\df_ct.pkl' )

df_composition_2.to_pickle( r'F:\OneDrive - Uniklinik RWTH Aachen\DEXA\composition\df_composition_2.pkl' )

df_composition_2 = pd.read_pickle( r'F:\OneDrive - Uniklinik RWTH Aachen\DEXA\composition\df_composition_2.pkl' )


# %%

# Drop duplicates based on 'animal_id', keeping the first row
df_composition_3 = df_composition_2.drop_duplicates(subset=['animal_id'], keep='first')

# %%

df_composition_3.shape
    # Out[33]: (101, 16)

df_composition_3[:4]
    # Out[34]: 
    #           species      sex animal_id condition      day  repetition  \
    # 0  Xenopus laevis 1.000000         1   Wiemuth 1.000000    1.000000   
    # 3  Xenopus laevis 1.000000         2   Wiemuth 1.000000    1.000000   
    # 6  Xenopus laevis 1.000000         3   Wiemuth 1.000000    1.000000   
    # 9  Xenopus laevis 1.000000         4   Wiemuth 1.000000    1.000000   
    
    #                   date      bcs         bw       ncl   fatbody  \
    # 0  2022-11-28 00:00:00 1.000000         77  9.500000  5.700000   
    # 3  2022-11-28 00:00:00 5.000000        194 13.200000  5.200000   
    # 6  2022-11-07 00:00:00 4.000000 150.200000       NaN 16.200000   
    # 9  2022-12-12 00:00:00 3.000000 116.200000 11.400000  2.700000   
    
    #    fatbody_censored   oocytes  oocytes_censored   leakage  leakage_censored  
    # 0               NaN  3.700000               NaN       NaN          1.000000  
    # 3               NaN 47.700000               NaN  0.130000               NaN  
    # 6               NaN 10.700000               NaN       NaN          1.000000  
    # 9               NaN  7.700000               NaN -0.200000               NaN  

# %%

df_composition_3.to_pickle( r'F:\OneDrive - Uniklinik RWTH Aachen\DEXA\composition\df_composition_3.pkl' )

# %%

# 1. (Optional but recommended)
# To make the merge efficient, create a smaller dataframe from df_ct
    # that only has the key ('animal_id') and the columns you want to add.
columns_to_add = ['animal_id', 'fat_volume_ct', 'body_volume_ct']
df_ct_subset = df_ct[columns_to_add]


# 2. Perform the merge
# We merge 'df_composition_3' (left) with 'df_ct_subset' (right)
# 'on' specifies the key column to match
# 'how='left'' keeps all rows from df_composition_3
df_composition_4 = pd.merge(
                            df_composition_3, 
                            df_ct_subset, 
                            on='animal_id', 
                            how='left'
)

# %%

df_composition_4.shape
    # Out[38]: (101, 18)

list( df_composition_4.columns )
    # Out[39]: 
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
    #  'leakage',
    #  'leakage_censored',
    #  'fat_volume_ct',
    #  'body_volume_ct']


df_composition_4.dtypes
    # Out[36]: 
    # species              object
    # sex                 float64
    # animal_id            object
    # condition            object
    # day                 float64
    # repetition          float64
    # date                 object
    # bcs                 float64
    # bw                   object
    # ncl                 float64
    # fatbody             float64
    # fatbody_censored    float64
    # oocytes             float64
    # oocytes_censored    float64
    # leakage              object
    # leakage_censored    float64
    # fat_volume_ct       float64
    # body_volume_ct      float64
    # dtype: object



df_composition_4[-4:]
    # Out[37]: 
    #             species      sex animal_id condition      day  repetition  \
    # 97   Xenopus laevis 2.000000     KM-13  Hausmann 1.000000    1.000000   
    # 98   Xenopus laevis 2.000000     KM-14  Hausmann 1.000000    1.000000   
    # 99   Xenopus laevis 2.000000     KM-15  Hausmann 1.000000    1.000000   
    # 100  Xenopus laevis 2.000000     KM-16  Hausmann 1.000000    1.000000   
    
    #                     date      bcs        bw      ncl  fatbody  \
    # 97   2025-09-02 00:00:00 2.000000 31.900000 7.200000 1.880000   
    # 98   2025-09-10 00:00:00 3.000000 42.700000 7.500000 2.100000   
    # 99   2025-09-10 00:00:00 3.000000 43.800000 7.800000 1.600000   
    # 100  2025-09-10 00:00:00 3.000000        38 7.200000 2.200000   
    
    #      fatbody_censored  oocytes  oocytes_censored leakage  leakage_censored  \
    # 97                NaN      NaN               NaN     NaN               NaN   
    # 98                NaN      NaN               NaN     NaN               NaN   
    # 99                NaN      NaN               NaN     NaN               NaN   
    # 100               NaN      NaN               NaN     NaN               NaN   
    
    #      fat_volume_ct  body_volume_ct  
    # 97     1708.000000    28313.000000  
    # 98     2385.000000    39840.000000  
    # 99     1763.000000    39073.000000  
    # 100    1726.000000    34441.000000  


# %%

df_composition_4.to_pickle( r'F:\OneDrive - Uniklinik RWTH Aachen\DEXA\composition\df_composition_4.pkl' )

# %% 

df_composition_4['fatbody'].dtype
    # Out[16]: dtype('float64')


# You've found the exact problem! dtype('O') means 'Object,' which is pandas' way of saying it's storing text (strings), not numbers.
# This is why the division failed.
df_composition_4['bw'].dtype
    # Out[17]: dtype('O')


# If your data uses commas as decimal separators (common in Europe), 
    # you must replace them with periods before you convert the column to a numeric type.
df_composition_4['bw'] = df_composition_4['bw'].str.replace(',', '.')

df_composition_4['bw'][50:60]
    # Out[27]: 
    # 50      NaN
    # 51      NaN
    # 52      NaN
    # 53      NaN
    # 54      NaN
    # 55      NaN
    # 56    248.2
    # 57      NaN


Out[26]: 
    # 30      NaN
    # 31      NaN
    # 32      NaN
    # 33      NaN
    # 34      NaN
    # 35      NaN
    # 36      NaN
    # 37      NaN
    # 38      NaN
    # 39      NaN
    # 40      NaN
    # 41      NaN
    # 42      NaN
    # 43    131.9
    # 44      NaN

# %%

df_composition_4[['fatbody' , 'bw']][:10]
    # Out[13]: 
    #     fatbody         bw
    # 0  5.700000         77
    # 1  5.200000        194
    # 2 16.200000 150.200000
    # 3  2.700000 116.200000
    # 4       NaN        282
    # 5  3.300000  69.300000
    # 6  2.700000 170.200000
    # 7  2.300000 117.400000
    # 8  3.000000 145.700000
    # 9       NaN  86.300000


# %%


# 1. Define your master list of all columns that *should* be numbers
numeric_cols_list = [
    'bcs',
    'bw',
    'ncl',
    'fatbody',
    'oocytes',
    'leakage',
    'fat_volume_ct',
    'body_volume_ct'
    # Add any other columns you know should be numeric
]

# 2. Loop through your list and apply the 3-step fix to each one
print("--- Starting data type conversion ---")
for col_name in numeric_cols_list:
    # Check that the column actually exists before trying to fix it
    # astype(str) must be written first, otherwise, most of the data will be turned to NaN !
    if col_name in df_composition_4.columns:
        # Apply the fix
        df_composition_4[col_name] = pd.to_numeric(
            df_composition_4[col_name].astype(str).str.replace(',', '.'),
            errors='coerce'
        )
        print(f"  > Column '{col_name}' fixed.")
    else:
        print(f"  ! Warning: Column '{col_name}' not found.")

# 3. Now, check your dataframe's types again
print("\n--- All Types After Conversion ---")
print(df_composition_4.dtypes)

# %%

    # --- Starting data type conversion ---
    #   > Column 'bcs' fixed.
    #   > Column 'bw' fixed.
    #   > Column 'ncl' fixed.
    #   > Column 'fatbody' fixed.
    #   > Column 'oocytes' fixed.
    #   > Column 'leakage' fixed.
    #   > Column 'fat_volume_ct' fixed.
    #   > Column 'body_volume_ct' fixed.
    
    
    # --- All Types After Conversion ---
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
    # leakage             float64
    # leakage_censored    float64
    # fat_volume_ct       float64
    # body_volume_ct      float64
    # dtype: object

# %%

df_composition_5 = df_composition_4.copy()

df_composition_5.to_pickle( r'F:\OneDrive - Uniklinik RWTH Aachen\DEXA\composition\df_composition_5.pkl' )

# %% ratio

# fwpd = fat weight percentage _ dissection
df_composition_5['fwp_d'] =  ( df_composition_5['fatbody'] /  df_composition_5['bw'] ) * 100 
# TypeError: unsupported operand type(s) for /: 'float' and 'str'
    # this was because some columns had _,_ instead of _ as decimal.
    # hence : dtype : object : string.


# fat volume percentage  _ ct
df_composition_5['fvp_ct'] = ( df_composition_5['fat_volume_ct'] /  df_composition_5['body_volume_ct'] ) * 100 

# body mass index 
df_composition_5['bmi'] =  df_composition_5['bw'] / ( df_composition_5['ncl'] ** 2 )

# wli : weight-length index.
df_composition_5['wli'] =  df_composition_5['bw'] / ( df_composition_5['ncl'] ** 3 )

# owp : oocytes' weight %
df_composition_5['owp'] =  ( df_composition_5['oocytes'] /  df_composition_5['bw'] ) * 100 

# %%

df_composition_5.to_pickle( r'F:\OneDrive - Uniklinik RWTH Aachen\DEXA\composition\df_composition_5.pkl' )


# %%

df_composition_5[['fatbody' , 'bw']][:10]
    # Out[12]: 
    #    fatbody     bw
    # 0      5.7   77.0
    # 1      5.2  194.0
    # 2     16.2  150.2
    # 3      2.7  116.2
    # 4      NaN  282.0
    # 5      3.3   69.3
    # 6      2.7  170.2
    # 7      2.3  117.4
    # 8      3.0  145.7
    # 9      NaN   86.3


# %%

df_composition_5[[ 'fwp_d' , 'fvp_ct' , 'bmi' , 'owp' ]][:4]
    # Out[17]: 
    #        fwp_d  fvp_ct       bmi        owp
    # 0   7.402597     NaN  0.853186   4.805195
    # 1   2.680412     NaN  1.113407  24.587629
    # 2  10.785619     NaN       NaN   7.123835
    # 3   2.323580     NaN  0.894121   6.626506


df_composition_5[[ 'fwp_d' , 'fvp_ct' , 'bmi' , 'owp' ]][-4:]
    # Out[18]: 
    #         fwp_d    fvp_ct       bmi  owp
    # 97   5.893417  6.032565  0.615355  NaN
    # 98   4.918033  5.986446  0.759111  NaN
    # 99   3.652968  4.512067  0.719921  NaN
    # 100  5.789474  5.011469  0.733025  NaN

# %%


# %%

df_composition_5['oocytes'][:4]
    # Out[15]: 
    # 0     3.7
    # 1    47.7
    # 2    10.7
    # 3     7.7
    # Name: oocytes, dtype: float64

# %%



