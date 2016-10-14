# !usr/bin/python2.7 -tt
#Create a folder "diary" where this code is located 
import os
import glob
from pprint import pprint

print('='*70)
print("Hello Welcome to Your Personal Diary")
print('='*70)
'''
def createKey():
    writeKey = open('key.encrypt','w')
    writePin = open('writePin.encrypt','w')
    myKey = input("Enter username : ")
    myPin = input("Enter password : ")
    writeKey.write(myKey)
    writePin.write(myPin)
    writeKey.close()
    writePin.close()
    print("Credential created")
'''


def myDiary():
    print(" A) Add Entry")
    print(" V) View Entry")
    print(" C) Display Content")
    choice = input("\t\tEnter you choice: ")
    if choice == 'A' or choice == 'a':
        pageDetail = input("Enter title: ")
        dEntry = open('diary'+'/'+pageDetail+'.txt','w')
        content = input("Enter content and hit enter to exit " )
        dEntry.write(content+'\n')
        dEntry.close()
    elif choice == 'V' or choice == 'v':
        print(os.listdir('./diary'))
        choice = input("Enter page title: ")
        try:
            dview = open(choice+'.txt','r')
            print(dview.readline())
        except FileNotFoundError:
            print("Please give proper file name")
    elif choice == 'C' or choice == 'c':
        for i in glob.glob('/diary/.txt'):
            print(i)
       
'''
if __name__ == '__main__':
    cache = []
    if len(cache) == 0:
        createKey()
        else:
            readkey = open('key.encrypt','r')
            readpin = open('pin.encrypt','r')
            readkey = readkey.readline()
            readpin = readpin.readline()
            database = [[readkey,readpin]]
            username = input("Enter username: " )
            password = input("Enter password: ")
            if [username,password] in database:
                myDiary()
                
            else:
                print("You are not authorize")
        cache.append('~!@#$%^')
'''
while True:
    if __name__ == '__main__':
        myDiary()
