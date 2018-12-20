#turn dictionary.txt into python dictionary
#using python3.6.1
import sqlite3

def dictList():
  '''Parses a text file into a list, and strips newlines, and NULL entries.'''
  with open('dictionary.txt','r') as doc:
    wordsList=doc.read().splitlines()
  temp=list(map(lambda each: each.strip('\n'),wordsList))
  temp=list(map(lambda each: each.strip(),temp))
  return(temp)

def dictify(x):
  tempDict={}
  for item in x:
    #if the length of the current string is only a single character, assume this character has no definition.
    if(len(item)==1):
      tempDict.update({item:item})
    #Otherwise split the string on the first space, making the latter section the definition.
    else:
      a,b=item.split(" ",1)
      tempDict.update({a:b})
  return(tempDict)

def createDb(newDict):
  dictDb=sqlite3.connect('dictionary.db') #opens database
  cursor=dictDb.cursor() #Used for database traversal
  try:
    cursor.execute("DROP TABLE wordList")
  except:
    pass
  cursor.execute("CREATE TABLE wordList(generated_id INTEGER PRIMARY KEY,name text,def text)")
  for key, value in newDict.items():
    cursor.execute("INSERT INTO wordList(name, def)VALUES(?,?)",(key, value))
  dictDb.commit()
  dictDb.close()

def showDb():
  dictDb=sqlite3.connect('dictionary.db')
  cursor=dictDb.cursor()
  words=cursor.execute("SELECT name, def FROM wordList")
  print(cursor.fetchall())

def main():
  workingList = dictList() #Creates a string from a textfile
  workingList=list(filter(None,workingList)) #removes empty list entries
  newDict=dictify(workingList) #Takes in list, returns dictionary
  print("pass")
  createDb(newDict)
  showDb()
  
if __name__=="__main__":
  main()