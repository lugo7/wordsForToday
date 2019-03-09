#Flask backend
import os.path
import time
from flask import Flask
import createDictDb
import createDailyDb
import selectRand1
app = Flask(__name__)

def splitDef(x):
    pass

#@app.route("/")
def displayWord():
    print('pass')
    if(os.path.isfile('dictionary.db')!=True): #check if the main database file exists.
        createDictDb.main()#if not, create new database.
    if(os.path.isfile('dict24.db')!=True):
        createDailyDb.main() #Creates a database of 24 words.
    row=selectRand1.main() #picks out one random number from dailyDict
    print(row[0])
    print(row[1])
    return row

if __name__ == "__main__":
    #app.run()
    displayWord()
