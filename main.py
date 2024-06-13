from bs4 import BeautifulSoup
import requests
import pandas as pd
import numpy as np
from datetime import datetime as dt
import sqlite3
url = "https://web.archive.org/web/20230908091635/https://en.wikipedia.org/wiki/List_of_largest_banks"
output_csv_path = "./Largest_banks_data.csv"
table_name = "Largest_banks"
table_attr = ["Name","MC_USD_Billions"]
table_attr_final = ["Name","MC_USD_Billions","MC_GBP_Billions","MC_EUR_Billions","MC_INR_Billions"]
def log_process(message):
    timestamp = '%Y-%h-%d-%H:%M:%S'
    now = dt.now()
    now = now.strftime(timestamp)
    with open('code_log.txt',"a") as f:
        f.write(now + " : " + message)
def extract(url,table_attr):
    response = requests.get(url).text
    soup = BeautifulSoup(response,'html.parser')
    data = soup.find(lambda tag:tag.name == 'h2' and "By market capitalization" in tag.text)
    table = data.find_next("table")
    tb = table.find("tbody")
    rows = tb.find_all('tr')
    df = pd.DataFrame(columns=table_attr)
    for row in rows[1:]:
        cols = row.find_all('td')
        if len(cols) > 1:  # Ensure the row has data cells
            name = cols[1].get_text(strip=True)
            mc_usd = cols[2].get_text(strip=True).replace(",", "")
            mc_usd = float(mc_usd) if mc_usd else None
            df1 = pd.DataFrame({"Name": name, "MC_USD_Billion": mc_usd},index=[0])
            df = pd.concat([df,df1], ignore_index=True)
    log_process("DATA    EXTRACTED!!")
    return df
def transform(df):
    df2 = pd.read_csv("./exchange_rate.csv")
    ex = df2.set_index('Currency').to_dict()["Rate"]
    x = df["MC_USD_Billion"].to_list()
    df["MC_GBP_Billion"] = [np.round(i*ex["GBP"],2) for i in x]
    df["MC_EUR_Billion"] = [np.round(i*ex["EUR"],2) for i in x]
    df["MC_INR_Billion"] = [np.round(i*ex["INR"],2) for i in x]
    log_process("DATA_TRANSFORMED!")
    return df
def load_to_csv(df,output_csv_path):
    df.to_csv(output_csv_path)
    log_process("LOADED TO LOCAL CSV FILE PATH : {}!".format(output_csv_path))
def load_to_db(df,sql_connection,table_name):
    df.to_sql(table_name,sql_connection,if_exists="replace",index=False)
    log_process("LOADED TO DATABASE : {} TABLE : {}!".format("Banks",table_name))
def run_query(query_statement,sql_connection):
    log_process("EXECUTED AN SQL QUERY...")
    output = pd.read_sql(query_statement,sql_connection)
    print(output)
