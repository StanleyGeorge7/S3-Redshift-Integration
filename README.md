# Bulk Query Validation

This project is designed to facilitate the validation of bulk queries between data stored in Amazon S3 and Amazon Redshift. It processes large datasets, splits them into manageable chunks, compares the data, and stores the results in a structured manner.

## Project Structure

```
s3-redshift-validation
├── src
│   ├── __init__.py
│   ├── main.py
│   ├── config
│   │   ├── __init__.py
│   │   └── settings.py
│   ├── data
│   │   ├── __init__.py
│   │   ├── s3_handler.py
│   │   ├── redshift_handler.py
│   │   └── split.py
│   ├── processing
│   │   ├── __init__.py
│   │   ├── compare.py
│   │   └── preprocess.py
│   └── utils
│       ├── __init__.py
│       └── helpers.py
├── result
├── .env
├── requirements.txt
└── README.md
```

## Setup Instructions

1. **Clone the Repository**

   ```bash
   git clone https://github.com/StanleyGeorge7/S3-Redshift-Integration.git
   cd s3-redshift-validation
   ```

2. **Create a Virtual Environment**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install Dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Configure Environment Variables**
   Create a `.env` file in the root directory and add your AWS credentials:
   ```
   AWS_ACCESS_KEY_ID=your_access_key
   AWS_SECRET_ACCESS_KEY=your_secret_key
   AWS_REGION=your_region
   ```

## Usage

To run the application, execute the following command:

```bash
python src/main.py
```

This will initiate the process of reading data from S3 and Redshift, performing the necessary comparisons, and saving the results in the `result` directory.

## Features

- **Data Handling**: Efficiently handles large datasets from S3 and Redshift.
- **Data Comparison**: Identifies differences in rows and columns between datasets.
- **Chunk Processing**: Splits large DataFrames into smaller chunks for easier processing.
- **Result Storage**: Saves comparison results in a structured format for easy access.

## Contributing

Contributions are welcome! Please submit a pull request or open an issue for any enhancements or bug fixes.
