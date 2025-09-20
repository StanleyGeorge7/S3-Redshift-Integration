def dataframe_preprocessing(df1, df2):
    sorted_cols_1 = sorted(df1.columns.tolist())
    sorted_cols_2 = sorted(df2.columns.tolist())

    df1 = df1.reindex(columns=sorted_cols_1)
    df2 = df2.reindex(columns=sorted_cols_2)

    df1 = df1.sort_values(by='values').reset_index(drop=True)
    df2 = df2.sort_values(by='values').reset_index(drop=True)

    return df1, df2

def add_identifiers(df):
    import numpy as np
    values = np.random.permutation(df.shape[0]) + 1
    df['values'] = values
    return df