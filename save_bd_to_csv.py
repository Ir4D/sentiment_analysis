import pandas as pd
import sqlite3

con = sqlite3.connect('DATA.db')
db_posts = pd.read_sql_query("SELECT * FROM post", con)
db_posts.to_csv('posts.csv', sep=';', encoding='utf-8', index=False)

db_comments = pd.read_sql_query("SELECT * FROM comment", con)
db_comments.to_csv('comments.csv', sep=';', encoding='utf-8', index=False)
