from sqlite3.dbapi2 import Connection, Cursor
import sys
import sqlite3

db_name = "budget_tool.db"
table_names = ['Expenses', 'Income', 'Categories']

class Expense:
    def __init__(self,id,date,catId,title,amount):
        self.expense_Id = id
        self.transaction_date = date
        self.category_Id = catId
        self.title = title
        self.amount = amount



def connect_db():
    conn = sqlite3.connect(db_name)
    return conn.cursor()

def save_changes(conn: Connection):
    conn.commit()
    # conn.close()

def init_db(conn: Connection):
    c: Cursor = conn.cursor()

    c.execute("PRAGMA foreign_keys = 1")
    conn.commit()
    
    c.execute("""
        CREATE TABLE IF NOT EXISTS Categories {
            category_Id     INTEGER PRIMARY KEY,
            name            text    NOT NULL,
        }

        CREATE TABLE IF NOT EXISTS Expenses {
            expense_Id          INTEGER     PRIMARY KEY,
            transaction_date    text        NOT NULL,
            category_Id         INTEGER     NOT NULL,
            title               text,
            amount              REAL        NOT NULL,
            FOREIGN KEY (category_Id) REFERENCES CATEGORIES (category_Id)
        }

        CREATE TABLE IF NOT EXISTS Income{
            income_Id           INTEGER     PRIMARY KEY,
            transaction_date    text        NOT NULL,
            category_Id         INTEGER     NOT NULL,
            title               text,
            amount              REAL        NOT NULL,
            FOREIGN KEY (category_Id) REFERENCE CATEGORIES (category_Id)
        }
    """)
    conn.commit()

