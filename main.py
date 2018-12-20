#Flask backend
from os import path
from flask import Flask
import CreateDictDb
import returnRandom
import dailyDict
import selectRand1
app = Flask(__name__)

@app.route("/")
def displayWord():
  if(os.path.isfile('dictionary.db')==True): #check if the main database file exists.
    pass
  else:
    CreateDictDb.main() #if it doesn't exist create new database.
  returnRandom.main() #select 24 random numbers.
  dailyDict.main() #picks out entries from 'dictionary.db'
  selectRand1.selectRand1() #picks out one random number from dailyDict
  print('pass')