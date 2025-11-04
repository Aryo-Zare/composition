

# %%'

import os

# %%'


# --- Setup Paths ---

# Use a raw string (r"...") to correctly handle backslashes in Windows paths
folder_path = r"F:\OneDrive - Uniklinik RWTH Aachen\DEXA\composition"

# Create the full paths to the files
file1_path = os.path.join(folder_path, "P092_Talbot_Datei.xlsx")
file2_path = os.path.join(folder_path, "CT.xlsx")

# %%'


# Use the 'sheet_name' parameter to load *only* the 'Data_query' sheet.
# 'header=0' tells pandas to use the first row (index 0) as the header, 
# which is the default behavior.
df_composition = pd.read_excel(file1_path, 
                          sheet_name='Data_query', 
                          header=0)

# C:\Users\azare\AppData\Local\miniconda3\envs\env_23\Lib\site-packages\openpyxl\worksheet\_read_only.py:85: 
#     UserWarning: Data Validation extension is not supported and will be removed
#   for idx, row in parser.parse():

# %%'


# 'header=0' is also the default here.
df_ct = pd.read_excel(file2_path, 
                      header=0)
    

# %%'
# %%'

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

# %%'
# %%'

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

# %%'

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

# %%'

# Drop all rows that have one or more NaN values
df_ct = df_ct.dropna()

# Chain the prefix and suffix removals
df_ct['animal_id'] = df_ct['animal_id'].str.removeprefix('LT-').str.removesuffix('x')

# %%'

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

# %%'

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

# %%'

df_ct.to_pickle( r'F:\OneDrive - Uniklinik RWTH Aachen\DEXA\composition\df_ct.pkl' )

df_composition_2.to_pickle( r'F:\OneDrive - Uniklinik RWTH Aachen\DEXA\composition\df_composition_2.pkl' )

df_composition_2 = pd.read_pickle( r'F:\OneDrive - Uniklinik RWTH Aachen\DEXA\composition\df_composition_2.pkl' )

# %%' leakage_averages

df_composition_2['leakage'] = pd.to_numeric(
    df_composition_2['leakage'].astype(str).str.replace(',', '.'),
    errors='coerce'
)
        
leakage_average = df_composition_2.groupby('animal_id')['leakage'].mean()

type( leakage_average )
    # Out[14]: pandas.core.series.Series


# after aggregation, the number of rows shreinked to about 1/3 , as expected.
leakage_average.shape
    # Out[17]: (101,)

df_composition_2.shape
    # Out[18]: (271, 16)

leakage_average[:4]
    # Out[15]: 
    # animal_id
    # 1         NaN
    # 2    0.120000
    # 3         NaN
    # 4   -0.336667
    # Name: leakage, dtype: float64

leakage_average[-4:]
    # Out[19]: 
    # animal_id
    # KW-2   -0.213333
    # KW-3   -0.280000
    # KW-4   -0.046667
    # KW-5   -0.063333
    # Name: leakage, dtype: float64

# Convert this from a Series into a DataFrame, naming the new column
leakage_average_df = leakage_average.reset_index(name='leakage_average')

leakage_average_df[:4]
    # Out[23]: 
    #   animal_id  leakage_average
    # 0         1              NaN
    # 1         2         0.120000
    # 2         3              NaN
    # 3         4        -0.336667

# this coes from later stages of this file.
    # this is because this part was a revision of the previous stages !
df_composition_6 = pd.merge(
                            df_composition_5, 
                            leakage_average_df, 
                            on='animal_id', 
                            how='left'
)

df_composition_6.drop( columns=['leakage' , 'leakage_censored'] , inplace=True )

df_composition_6.to_pickle( r'F:\OneDrive - Uniklinik RWTH Aachen\DEXA\composition\df_composition_6.pkl' )


# %%'

# Drop duplicates based on 'animal_id', keeping the first row
df_composition_3 = df_composition_2.drop_duplicates(subset=['animal_id'], keep='first')

# %%'

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

# %%'

df_composition_3.to_pickle( r'F:\OneDrive - Uniklinik RWTH Aachen\DEXA\composition\df_composition_3.pkl' )

# %%'

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

# %%'

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


# %%'

df_composition_4.to_pickle( r'F:\OneDrive - Uniklinik RWTH Aachen\DEXA\composition\df_composition_4.pkl' )

# %%' 

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

# %%'

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


# %%'


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

# %%'

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

# %%'

df_composition_5 = df_composition_4.copy()

df_composition_5.to_pickle( r'F:\OneDrive - Uniklinik RWTH Aachen\DEXA\composition\df_composition_5.pkl' )

# %%' ratio

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

# %%'

df_composition_5.to_pickle( r'F:\OneDrive - Uniklinik RWTH Aachen\DEXA\composition\df_composition_5.pkl' )


# %%'

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


# %%'

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

# %%'


# %%'

df_composition_5['oocytes'][:4]
    # Out[15]: 
    # 0     3.7
    # 1    47.7
    # 2    10.7
    # 3     7.7
    # Name: oocytes, dtype: float64

# %%'
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
    #  'leakage_average']


# %%'


# List of the identifier and grouping columns you want to keep
id_columns = [
               'sex',
               'animal_id',
               'condition',
               'date',
              ]

# List of the measurement columns you want to analyze
readout_parameters = [
                        'bcs',
                        'fwp_d',
                        'fvp_ct',
                        'owp',
                        'leakage_average',
                        'bmi',
                        'wli'  
]

# Create the new, focused DataFrame
df_subset = df_composition_6[ id_columns + readout_parameters ]

# %%'

# Melt the DataFrame to convert it to a long format
df_composition_6_tidy = pd.melt(
                                df_subset,
                                id_vars=id_columns,              # Columns to keep as they are (identifiers)
                                value_vars=readout_parameters,   # Columns to "unpivot" into rows
                                var_name='metric',               # Name of the new column for the measurement type
                                value_name='value'               # Name of the new column for the measurement value
)

# %%'

# 2025-10-27 __ 13:34
df_composition_6_tidy.shape
    # Out[37]: (707, 6)

# %%'

df_composition_6_tidy.to_pickle( r'F:\OneDrive - Uniklinik RWTH Aachen\DEXA\composition\df_composition_6_tidy.pkl' )

# %%'
# %%'

list( df_composition_6_tidy.columns ) 
    # Out[44]: ['sex', 'animal_id', 'condition', 'date', 'metric', 'value']

# %%'

# create a new column with the string-type of bcs.
# This ensures Seaborn treats it as a distinct category (1, 2, 3...)
# and not as a continuous number (which would create one giant violin).
df_composition_6['bcs_str'] = df_composition_6['bcs'].astype(str)

# %%'

df_composition_6['bcs'].unique()
Out[55]: array([ 1.,  5.,  4.,  3.,  2., nan])

df_composition_6['bcs'].dtype
    # Out[57]: dtype('float64')

# the problem here : there is a : .0 : decimal after each category !
df_composition_6['bcs_str'].unique()
# Out[54]: array(['1.0', '5.0', '4.0', '3.0', '2.0', 'nan'], dtype=object)

# %% Int64 : remove decimal !

# 1. Go back to the ORIGINAL float 'bcs' column.
#    Convert it to a nullable integer ('Int64' with a capital 'I').
#    This turns 1.0 into 1 and NaN into <NA>.
df_composition_6['bcs_Int64'] = df_composition_6['bcs'].astype('Int64')

df_composition_6['bcs_Int64'].unique()
    # Out[15]: 
    # <IntegerArray>
    # [1, 5, 4, 3, 2, <NA>]
    # Length: 6, dtype: Int64

# 2. Now, convert that integer column to a string.
#    This turns 1 into '1' and <NA> into the string '<NA>'.
df_composition_6['bcs_Int64_str'] = df_composition_6['bcs_Int64'].astype(str)

df_composition_6['bcs_Int64_str'].unique()
    # Out[17]: array(['1', '5', '4', '3', '2', '<NA>'], dtype=object)

# 3. (Optional) Replace the '<NA>' string with 'nan' to match your old output.
df_composition_6['bcs_Int64_str'] = df_composition_6['bcs_Int64_str'].replace('<NA>', 'nan')

# --- Check your result ---
df_composition_6['bcs_Int64_str'].unique()
# Out[19]: array(['1', '5', '4', '3', '2', 'nan'], dtype=object)

# %%'
# %% order bcs


bcs_Int64_str_order = [ '1', '2', '3', '4', '5', 'nan' ]
df_composition_6['bcs_Int64_str'] = pd.Categorical(
                                            df_composition_6['bcs_Int64_str'],
                                            categories=bcs_Int64_str_order,
                                            ordered=True
)


df_composition_6['bcs_Int64_str'].unique()
    # Out[21]: 
    # ['1', '5', '4', '3', '2', 'nan']
    # Categories (6, object): ['1' < '2' < '3' < '4' < '5' < 'nan']

# %%'

df_composition_6.to_pickle( r'F:\OneDrive - Uniklinik RWTH Aachen\DEXA\composition\df_composition_6.pkl' )


# %%'

df_composition_6['leakage_average'].sort_values()[:4]
    # Out[73]: 
    # 64   -13.233333
    # 23    -1.243333
    # 7     -1.076667
    # 34    -0.843333
    # Name: leakage_average, dtype: float64

# %%' oocyte_censored

oocyte_censored = df_composition_6[[ 'animal_id' , 'bcs' , 'oocytes_censored']].dropna()

oocyte_censored
    # Out[15]: 
    #    animal_id      bcs  oocytes_censored
    # 30        31 1.000000          1.000000
    # 46        47 2.000000          1.000000
    # 53        54 2.000000          1.000000
    # 56        57 5.000000          1.000000

# %%'
# %% supplemantory data

# this is the data that Leonie had sent me afterwards, to be added to the existing one.
    # it contains data before 2022, related to the previous publication.

# Use a raw string (r"...") to correctly handle backslashes in Windows paths
folder_path = r"F:\OneDrive - Uniklinik RWTH Aachen\DEXA\composition"

# Create the full paths to the files
# supp : supplemantory 
supp_file_path = os.path.join(folder_path, "ergänzende Datensets für BMI.xlsx")

# Use the 'sheet_name' parameter to load *only* the 'Data_query' sheet.
# 'header=0' tells pandas to use the first row (index 0) as the header, 
# which is the default behavior.
df_supp = pd.read_excel( supp_file_path, header=0)

# %%'

df_supp.shape
    # Out[13]: (62, 4)

df_supp[:4]
    # Out[14]: 
    #    Unnamed: 0  BCS     lengt     weight
    # 0           1    2 11.000000 111.000000
    # 1           2    2 10.500000 100.000000
    # 2           3    3 11.000000 112.300000
    # 3           4    3 12.000000 146.400000


df_supp.dtypes
    # Out[17]: 
    # Unnamed: 0      int64
    # BCS             int64
    # lengt         float64
    # weight        float64
    # dtype: object

df_supp.columns
    # Out[18]: Index(['Unnamed: 0', 'BCS', 'lengt', 'weight'], dtype='object')

# %%'


# --- Assuming 'df_composition_6' and 'df_supp' are loaded ---

# --- 1. Create a copy to avoid changing your original df_supp ---
df_supp_cleaned = df_supp.copy()

# --- 2. Rename columns ---
new_column_names = {
                    'Unnamed: 0': 'animal_id',
                    'BCS': 'bcs',
                    'lengt': 'ncl',
                    'weight': 'bw'
}

df_supp_cleaned = df_supp_cleaned.rename( columns=new_column_names )

# --- 3. Add 'supp_' prefix to 'animal_id' ---
# We convert to string first, just in case the IDs are numbers
df_supp_cleaned['animal_id'] = 'supp_' + df_supp_cleaned['animal_id'].astype(str)

df_supp_cleaned['animal_id'][:4]
    # Out[24]: 
    # 0    supp_1
    # 1    supp_2
    # 2    supp_3
    # 3    supp_4
    # Name: animal_id, dtype: object

# --- 4. Create the new 'bcs' columns ---
# (This follows the 'Method 1' we used before, which is robust)
# a. Convert to nullable integer
df_supp_cleaned['bcs_Int64'] = df_supp_cleaned['bcs'].astype('Int64')
# b. Convert that integer to a string
df_supp_cleaned['bcs_Int64_str'] = df_supp_cleaned['bcs_Int64'].astype(str)
# c. Replace the <NA> string with 'nan' (if any)
df_supp_cleaned['bcs_Int64_str'] = df_supp_cleaned['bcs_Int64_str'].replace('<NA>', 'nan')


df_supp_cleaned.to_pickle( r'F:\OneDrive - Uniklinik RWTH Aachen\DEXA\composition\df_supp_cleaned.pkl' )

# %%


df_supp_cleaned['bcs'].unique()
    # Out[36]: array([2, 3, 4, 5, 1])


df_supp_cleaned['bcs'].value_counts()
    # Out[37]: 
    # bcs
    # 5    24
    # 4    18
    # 3    16
    # 2     3
    # 1     1
    # Name: count, dtype: int64

# %%

# --- 5. Save the categorical order from your MAIN dataframe ---
# This is the answer to your question! We save the order first.

# try:
#     # Get the existing categories and their order
#     bcs_category_order = df_composition_6['bcs_Int64_str'].cat.categories
#     print(f"Saved existing category order: {bcs_category_order}")
# except AttributeError:
#     print("Warning: 'bcs_Int64_str' in df_composition_6 is not categorical.")
#     print("Will set a default sort order ('1', '2', ... 'nan').")
#     # Manually define the order if it wasn't categorical for some reason
#     bcs_category_order = sorted(
#                                 df_composition_6['bcs_Int64_str'].unique(), 
#                                 key=lambda x: (x.isdigit(), x)
    )


# %%
    
# --- 6. Concatenate the dataframes ---
# This creates df_composition_7
# ignore_index=True re-calculates the index (0, 1, 2, ...)
df_composition_7 = pd.concat(
                                [ df_composition_6, df_supp_cleaned ], 
                                ignore_index=True
)

# %% order bcs


# When you use pd.concat(), pandas has to merge the two columns.
    # df_composition_6['bcs_Int64_str'] is a special Categorical type.
    # df_supp_cleaned['bcs_Int64_str'] is a plain object (string) type.
    # To merge them, pandas will "break" the Categorical type and create a new, simple object column in df_composition_7. 
    # All your special ordering will be lost.
# Hence, you should define the order again :

bcs_Int64_str_order = [ '1', '2', '3', '4', '5', 'nan' ]

# --- 7. Re-apply the categorical order ---
# When you concatenated, the 'bcs_Int64_str' column lost its order.
# We now re-apply it to the entire column in the new dataframe.
df_composition_7['bcs_Int64_str'] = pd.Categorical(
                                                    df_composition_7['bcs_Int64_str'],
                                                    categories=bcs_Int64_str_order,
                                                    ordered=True
)


df_composition_7['bcs_Int64_str'].unique()
    # Out[29]: 
    # ['1', '5', '4', '3', '2', 'nan']
    # Categories (6, object): ['1' < '2' < '3' < '4' < '5' < 'nan']

# %%'

df_composition_7.shape
    # Out[30]: (163, 25)


df_composition_7.dtypes
    # Out[31]: 
    # species               object
    # sex                  float64
    # animal_id             object
    # condition             object
    # day                  float64
    # repetition           float64
    # date                  object
    # bcs                  float64
    # bw                   float64
    # ncl                  float64
    # fatbody              float64
    # fatbody_censored     float64
    # oocytes              float64
    # oocytes_censored     float64
    # fat_volume_ct        float64
    # body_volume_ct       float64
    # fwp_d                float64
    # fvp_ct               float64
    # bmi                  float64
    # owp                  float64
    # wli                  float64
    # leakage_average      float64
    # bcs_str               object
    # bcs_Int64              Int64
    # bcs_Int64_str       category
    # dtype: object

df_composition_7['bcs_Int64_str'].dtype
    # Out[32]: CategoricalDtype(categories=['1', '2', '3', '4', '5', 'nan'], ordered=True, categories_dtype=object)

# %%'

# body mass index 
df_composition_7['bmi'] =  df_composition_7['bw'] / ( df_composition_7['ncl'] ** 2 )

# wli : weight-length index.
df_composition_7['wli'] =  df_composition_7['bw'] / ( df_composition_7['ncl'] ** 3 )


# %%'

df_composition_7.to_pickle( r'F:\OneDrive - Uniklinik RWTH Aachen\DEXA\composition\df_composition_7.pkl' )


# %%'




