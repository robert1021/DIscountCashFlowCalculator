import sqlite3
import os


class StocksDcfDatabase:

    def __init__(self):
        self.db_file_name = 'DiscountCashFlow.db'
        if not os.path.isfile(self.db_file_name):
            self.conn = sqlite3.connect(self.db_file_name)
            self.cursor = self.conn.cursor()
            self.__create_dcf_table()

        else:
            self.conn = sqlite3.connect(self.db_file_name)
            self.cursor = self.conn.cursor()

    def __create_dcf_table(self):
        self.cursor.execute("""CREATE TABLE STOCKS (
                               RESULT_ID   INTEGER UNIQUE,
                               STOCK    TEXT NOT NULL,
                               STOCK_PRICE TEXT NOT NULL,
                               PERIOD_1_REVENUE TEXT NOT NULL,
                               PERIOD_2_REVENUE TEXT NOT NULL,
                               PERIOD_3_REVENUE TEXT NOT NULL,
                               PERIOD_4_REVENUE TEXT,
                               PERIOD_1_NET_INCOME  TEXT NOT NULL,
                               PERIOD_2_NET_INCOME  TEXT NOT NULL,
                               PERIOD_3_NET_INCOME  TEXT NOT NULL,
                               PERIOD_4_NET_INCOME  TEXT,
                               PERIOD_1_FREE_CASH_FLOW  TEXT NOT NULL,
                               PERIOD_2_FREE_CASH_FLOW  TEXT NOT NULL,
                               PERIOD_3_FREE_CASH_FLOW  TEXT NOT NULL,
                               PERIOD_4_FREE_CASH_FLOW  TEXT,
                               YEARS_TO_PROJECT INTEGER NOT NULL,
                               REQUIRED_RETURN  TEXT NOT NULL,
                               PERPETUAL_GROWTH_RATE    TEXT DEFAULT '2.5' NOT NULL,
                               SHARES_OUTSTANDING TEXT NOT NULL,
                               TODAYS_VALUE TEXT NOT NULL,
                               FAIR_VALUE_EQUITY TEXT NOT NULL,
                               MARGIN_SAFETY_25 TEXT NOT NULL,
                               MARGIN_SAFETY_15 TEXT NOT NULL,
                               MARGIN_SAFETY_10 TEXT NOT NULL,
                               TRACK_TIME TIMESTAMP DEFAULT CURRENT_TIMESTAMP NOT NULL,
                               PRIMARY KEY (RESULT_ID AUTOINCREMENT))""")
        self.conn.commit()

    def insert_record_into_db(self, ticker, price, rev1, rev2, rev3, rev4, net1, net2, net3, net4, fcf1, fcf2, fcf3,
                              fcf4, years_to_project, required_return, shares, todays_value, fair_value, safety25,
                              safety15, safety10):
        self.cursor.execute("""INSERT INTO STOCKS ( STOCK, STOCK_PRICE, PERIOD_1_REVENUE, PERIOD_2_REVENUE,
                               PERIOD_3_REVENUE, PERIOD_4_REVENUE, PERIOD_1_NET_INCOME, 
                               PERIOD_2_NET_INCOME, PERIOD_3_NET_INCOME, PERIOD_4_NET_INCOME,
                               PERIOD_1_FREE_CASH_FLOW, PERIOD_2_FREE_CASH_FLOW, PERIOD_3_FREE_CASH_FLOW,
                               PERIOD_4_FREE_CASH_FLOW, YEARS_TO_PROJECT, REQUIRED_RETURN,
                               SHARES_OUTSTANDING, TODAYS_VALUE, FAIR_VALUE_EQUITY,
                               MARGIN_SAFETY_25, MARGIN_SAFETY_15, MARGIN_SAFETY_10)
                               VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                                """, (ticker, price, rev1, rev2, rev3, rev4, net1, net2, net3, net4, fcf1, fcf2, fcf3,
                                      fcf4, years_to_project, required_return, shares, todays_value, fair_value,
                                      safety25, safety15, safety10))
        self.conn.commit()




