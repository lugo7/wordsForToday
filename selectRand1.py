import sqlite3

def selectRand1():
  openFile=sqlite3.connect("dict24.db")
  db=openFile.cursor()
  db.execute("SELECT name, def FROM dailyTable ORDER BY RANDOM() LIMIT 1")
  row=db.fetchall()
  openFile.commit()
  openFile.close()
  print(len(row))
  print(row)
  row=str(row[0])
  row=row.split(',',1)
  newDef={row[0]:row[1]}
  print(len(row))
  print(type(row))
  print(newDef)
  return newDef

def main():
  selectRand1()
  
if __name__=="__main__":
  main()