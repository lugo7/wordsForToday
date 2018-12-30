#Flask backend
import os.path
from flask import Flask
import createDictDb
import createDailyDb
import selectRand1
app = Flask(__name__)

@app.route("/")
def displayWord():
    print('pass')
    if(os.path.isfile('dictionary.db')!=True): #check if the main database file exists.
        createDictDb.main()#if not, create new database.
    createDailyDb.main() #Creates a database of 24 words.
    return selectRand1.main() #picks out one random number from dailyDict

if __name__ == "__main__":
    app.run()
