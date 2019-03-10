#Flask backend
import os.path
import time
import re
from flask import Flask, render_template
import createDictDb
import createDailyDb
import selectRand1
app = Flask(__name__)

def splitDef(row):
    temp=[row[0]]
    temp.append((row[1].split('.',1)))
    if(bool(re.search(r'\d', row[1]))==True):
        temp.append(row[1].split(re.search(r'\d')))
    return temp

@app.route("/")
def displayWord():
    if(os.path.isfile('dictionary.db')!=True): #check if the main database file exists.
        createDictDb.main()#if not, create new database.
    if(os.path.isfile('dict24.db')!=True):
        createDailyDb.main() #Creates a database of 24 words.
    row=selectRand1.main() #picks out one random number from dailyDict
    temp=splitDef(row)
    print(temp)
    #print(row[0])
    #print(row[1])
    return render_template('home.html', word=temp[0] , type=temp[1][0]+'.', definition=temp[1][1])

if __name__ == "__main__":
    app.run(debug=True)
    #displayWord()
