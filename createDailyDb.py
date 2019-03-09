#Creates random dictionary of 24 keys, and values.
#python3.6.1
import random
import sqlite3

def createDaily(rows):
  '''Creates a list of twenty-four random numbers indicating id's in 'dictionary.db'. '''
  list24=[]
  [list24.append(random.randint(1,len(rows))) for i in range(24)]
  return list24

def getWords(dailyId):
  '''Creates a dictionary from the random database id's. Arguments should be list.'''
  openFile=sqlite3.connect("dictionary.db")
  db=openFile.cursor()
  dailyDict={}
  for x in range(24):
    db.execute("SELECT name, def FROM wordList WHERE generated_id=?",(dailyId[x],))
    row=db.fetchall()
    dailyDict.update({row[0][0]:row[0][1]})
  return dailyDict

def createDb(newDict):
  db24=sqlite3.connect('dict24.db')
  cursor=db24.cursor()
  try:
    cursor.execute("DROP TABLE dailyTable")
  except:
    pass
  cursor.execute("CREATE TABLE dailyTable(generated_id INTEGER PRIMARY KEY,name text,def text)")
  for key, value in newDict.items():
    cursor.execute("INSERT INTO dailyTable(name, def)VALUES(?,?)",(key, value))
  db24.commit()
  db24.close()

def main():
  openFile=sqlite3.connect("dictionary.db")
  openFile.row_factory = lambda cursor, row: row[0]
  db=openFile.cursor()
  db.execute("SELECT generated_id FROM wordList")
  rows=db.fetchall()
  dailyId=createDaily(rows)
  openFile.commit()
  openFile.close()
  dict24=getWords(dailyId)
  createDb(dict24)

if __name__=="__main__":
  main()
