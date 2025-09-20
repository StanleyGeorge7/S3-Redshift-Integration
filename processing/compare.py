def compare_df(df1, df2):
    df1_only_rows = df1[~df1.isin(df2)].dropna()
    df2_only_rows = df2[~df2.isin(df1)].dropna()

    df1_only_columns = df1.loc[:, ~(df1.columns.isin(df2.columns))]
    df2_only_columns = df2.loc[:, ~(df2.columns.isin(df1.columns))]

    return df1, df2, df1_only_rows, df1_only_columns, df2_only_rows, df2_only_columns