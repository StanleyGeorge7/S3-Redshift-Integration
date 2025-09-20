import os
import pandas as pd
from dotenv import load_dotenv
from data.s3_handler import S3Handler
from data.redshift_handler import RedshiftHandler
from data.split import split_dataframe
from processing.preprocess import dataframe_preprocessing
from processing.compare import compare_df

def main():
    load_dotenv()

    # Initialize S3 and Redshift handlers
    s3_handler = S3Handler()
    redshift_handler = RedshiftHandler()

    # Read data from S3 and Redshift
    df1 = s3_handler.download_data('s3.csv')
    df2 = redshift_handler.query_data('SELECT * FROM consolidation.loandata;')

    # Preprocess the data
    df1, df2 = dataframe_preprocessing(df1, df2)

    # Split the data into smaller chunks
    df1_chunks = split_dataframe(df1)
    df2_chunks = split_dataframe(df2)

    # Compare the data and save results
    for i, (chunk1, chunk2) in enumerate(zip(df1_chunks, df2_chunks)):
        df1_only_rows, df1_only_columns, df2_only_rows, df2_only_columns = compare_df(chunk1, chunk2)
        output_folder = f'result/folder_{i + 1}'
        os.makedirs(output_folder, exist_ok=True)

        df1_only_rows.to_csv(os.path.join(output_folder, 'Rows_in_df1_not_found_in_df2.csv'), index=False)
        df2_only_rows.to_csv(os.path.join(output_folder, 'Rows_in_df2_not_found_in_df1.csv'), index=False)
        df1_only_columns.to_csv(os.path.join(output_folder, 'Columns_in_df1_not_found_in_df2.csv'), index=False)
        df2_only_columns.to_csv(os.path.join(output_folder, 'Columns_in_df2_not_found_in_df1.csv'), index=False)

if __name__ == '__main__':
    main()