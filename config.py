from flask import config


import sqlite3

try:
    database = sqlite3.connect('shortcodes.db')
except:
    print("Issue creating or opening SQLite database")
    exit(1)