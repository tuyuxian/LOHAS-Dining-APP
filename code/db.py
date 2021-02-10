"""
Database Connection

Author: Yu-Hsien, Tu
Date: 2021/02/10
Version: 1.0

"""

import mysql.connector
import pandas as pd
from tqdm import tqdm


def connectDB(password_number):
    global mydb
    global cursor
    mydb = mysql.connector.connect(user='root',
                                   password=password_number,
                                   host='localhost',
                                   database='LOHAS-Dining-APP')
    cursor = mydb.cursor()


def update(iid, dining_type, common_name, description, detail):

    sql = "INSERT INTO material (IID, dining_type, common_name, description, detail) VALUES (%s, %s, %s, %s, %s)"
    val = [(iid, dining_type, common_name, description, detail)]

    cursor.executemany(sql, val)
    mydb.commit()


def closeDB():
    mydb.close()


def main():
    connectDB('xxxxxxxx')
    data = pd.read_csv("./整理後_食品營養成分資料集.csv")

    for i in tqdm(range(len(data.樣品名稱))):
        update(data.樣品名稱[i] if type(data.樣品名稱[i]) is not float else '',
               data.食品分類[i] if type(data.食品分類[i]) is not float else '',
               data.俗名[i] if type(data.俗名[i]) is not float else '',
               data.內容物描述[i] if type(data.內容物描述[i]) is not float else '',
               data.分析內容[i] if type(data.分析內容[i]) is not float else '')
    closeDB()


if __name__ == "__main__":
    main()
