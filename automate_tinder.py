import requests
import pynder
import pdb
facebook_token = '#your facebook facebook_token'
facebook_id = 'your id'
import time
from random import randint
import unicodedata
import MySQLdb

def get_like_user(user):
    pdb.set_trace()
    conn = MySQLdb.connect(host="localhost",user="root",passwd="",db="myvalentine")
    x = conn.cursor()
    user.like()
    try:
       x.execute("""INSERT INTO lovers VALUES (%s,%d,%s,%s,%d,%s,%s,%s,%s,%s)""",(user.name,user.age,user.birth_date,user.bio,user.distance_km,user.schools[0],'',user.id,user.instagram_username,user.jobs))
       conn.commit()
    except:
       conn.rollback()

def gettinderuser():
    time.sleep(randint(0,9))
    session = pynder.Session(facebook_id, facebook_token)
    users = session.nearby_users()
    for j in range(len(users)):
        pdb.set_trace()
        user = users[j]
        user.bio = str(unicodedata.normalize('NFKD', user.bio).encode('ascii','ignore'))
        get_like_user(user)

def main():
    gettinderuser()

if __name__ == "__main__": 
    main()