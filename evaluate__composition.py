

# %%

list ( df_composition_5.columns )
    # Out[23]: 
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
    #  'body_volume_ct',
    #  'fwp_d',
    #  'fvp_ct',
    #  'bmi',
    #  'owp',
    #  'wli']

# %%

corr_matrix = df_composition_5[[
                                     'bcs',
                                     'fwp_d',
                                     'fvp_ct',
                                     'owp',
                                     'leakage',
                                     'bmi',
                                     'wli'                                  
                                  ]].corr(method='spearman')

sns.heatmap(corr_matrix, annot=True, cmap='coolwarm')


# %%

plt.savefig( r'F:\OneDrive - Uniklinik RWTH Aachen\DEXA\composition\plot\corr_matrix.pdf' )
plt.savefig( r'F:\OneDrive - Uniklinik RWTH Aachen\DEXA\composition\plot\corr_matrix.svg' )


# %%

