def split_dataframe(df, chunk_size):
    chunks = []
    for start in range(0, len(df), chunk_size):
        end = start + chunk_size
        chunks.append(df.iloc[start:end])
    return chunks

def save_chunks_to_csv(chunks, base_filename, output_dir):
    for i, chunk in enumerate(chunks):
        chunk.to_csv(f"{output_dir}/{base_filename}_chunk_{i}.csv", index=False)