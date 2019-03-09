import sqlite3
import json

def main():
  openFile=sqlite3.connect("dict24.db")
  db=openFile.cursor()
  db.execute("SELECT name, def FROM dailyTable ORDER BY RANDOM() LIMIT 1")
  row=db.fetchall()
  openFile.commit()
  openFile.close()
  row=str(row[0])
  row=row.strip('()')
  row=row.strip(" '' ")
  row=row.split(',',1)
  for x in range(len(row)):
      row[x]=row[x].strip(" '' ")
      row[x]=row[x].strip(" "" ")
  return row

if __name__=="__main__":
    main()
