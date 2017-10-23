#!/usr/bin/python
# encoding: utf-8

import sys
import sqlite3
from workflow import Workflow

def main(wf):
    query=None
    if len(wf.args):
        query=wf.args[0]
    path="/Users/guozirui/Documents/EBook/"
    Database = sqlite3.connect(path+'metadata.db')
    DatabaseCursor = Database.cursor()
    Query = "select books.title,books.path,authors.name,data.format,data.name from data,books,authors,books_authors_link where title like \"%" + query + "%\" and books.id=books_authors_link.book and authors.id=books_authors_link.author and data.book=books.id"
    DatabaseCursor.execute(Query)
    values = DatabaseCursor.fetchall()
    for row in values:
        a=row[1]
        b=row[4]
        # a=a.replace(' ','\\ ')
        # a=a.replace('(','\\(')
        # a=a.replace(')','\\)')
        # b=b.replace(' ','\\ ')
        # b=b.replace('(','\\(')
        # b=b.replace(')','\\)')
        a=path+a+"/"
        wf.add_item(title=row[0]+"."+row[3].lower(), subtitle=row[2],arg=a+b+"."+row[3],valid=True,icon=a+"/cover.jpg")
    wf.send_feedback()


if __name__ == '__main__':
    wf = Workflow()
    sys.exit(wf.run(main))