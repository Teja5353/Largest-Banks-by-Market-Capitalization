# Data Engineer Project: Largest Banks by Market Capitalization

## Project Description

As a data engineer at a multi-national firm, your task is to compile a list of the top 10 largest banks in the world ranked by market capitalization in billion USD. You need to transform this data to include market capitalization values in GBP, EUR, and INR, based on provided exchange rate information. The processed data should be saved locally as a CSV file and stored in an SQL database for querying by managers from different countries.

## Project Structure

- `main.py`: Main script to execute the data processing pipeline.
- `exchange_rates.csv`: CSV file containing exchange rate information.
- `code_log.txt`: Log file to track the progress and any issues encountered.
- `Largest_banks_data.csv`: Output CSV file containing the processed data.

## Directions

### Functions

#### 1. Extract Data
**Function Name:** `extract(url, table_attr)`

- **Description:** Extracts tabular information from the given URL under the heading "By Market Capitalization" and saves it to a DataFrame.
- **Parameters:**
  - `url`: URL of the web page to scrape.
  - `table_attr`: List of table attributes to extract.

#### 2. Transform Data
**Function Name:** `transform(df, exchange_rate_path)`

- **Description:** Transforms the DataFrame by adding columns for Market Capitalization in GBP, EUR, and INR, rounded to 2 decimal places, based on the exchange rate information shared as a CSV file.
- **Parameters:**
  - `df`: DataFrame containing the extracted data.
  - `exchange_rate_path`: Path to the CSV file containing exchange rates.

#### 3. Save to CSV
**Function Name:** `save_to_csv(df, output_path)`

- **Description:** Saves the transformed DataFrame to an output CSV file.
- **Parameters:**
  - `df`: Transformed DataFrame.
  - `output_path`: Path where the CSV file will be saved.

#### 4. Save to SQL Database
**Function Name:** `save_to_sql(df, table_name, sql_connection)`

- **Description:** Loads the transformed DataFrame to an SQL database server as a table.
- **Parameters:**
  - `df`: Transformed DataFrame.
  - `table_name`: Name of the SQL table.
  - `sql_connection`: SQLite connection object.

#### 5. Run Queries
**Function Name:** `run_queries(query_statement,sql_connection)`

- **Description:** Runs specific queries on the database table and returns the results.
- **Parameters:**
  - `sql_connection`: SQLite connection object.
  - `query_statement`: query to be executed

#### 6. Log Process
**Function Name:** `log_process(message)`

- **Description:** Logs the progress of the code.
- **Parameters:**
  - `message`: Message to log.

### Execution Steps

1. **Extract Data:** Use the `extract` function to extract data from the URL and save it to a DataFrame.
2. **Transform Data:** Use the `transform` function to add market capitalization columns in GBP, EUR, and INR.
3. **Save to CSV:** Use the `save_to_csv` function to save the transformed DataFrame to a CSV file.
4. **Save to SQL Database:** Use the `save_to_sql` function to save the transformed DataFrame to an SQL database table.
5. **Run Queries:** Use the `run_queries` function to run specific queries on the database table.
6. **Log Process:** Use the `log_process` function to maintain log entries throughout the process.
### Author
TEJA NIDURAM
