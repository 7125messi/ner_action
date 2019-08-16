import pandas as pd

df = pd.read_excel('../data/index.xlsx',header=None)
df.columns = ['pitfall_c1','pitfall_c2','pitfall_c3','pitfall_c4','pitfall_c5','pitfall_name','pitfall_class','pitfall_nums_man','pitfall_prob','influence_class','season_class','pitfall_code']
print(df.head())

def dataProcessing(row):
    if row['pitfall_name'] == row['pitfall_c1']:
        ind = 1
    elif row['pitfall_name'] == row['pitfall_c2']:
        ind = 1
    elif row['pitfall_name'] == row['pitfall_c3']:
        ind = 1
    elif row['pitfall_name'] == row['pitfall_c4']:
        ind = 1
    elif row['pitfall_name'] == row['pitfall_c5']:
        ind = 1
    else:
        ind = 0
    return ind

df['ind'] = df.apply(dataProcessing,axis=1)
print(len(df))
df_txt = df.loc[df['ind'] == 0,'pitfall_name']
print(len(df_txt))
df_txt.to_csv('../data/result.txt',sep='\t',index=False)