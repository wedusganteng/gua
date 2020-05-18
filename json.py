import requests as r
import json
 
user = input('username : ')
req = r.get('https://instagram.com/'+user+'/?__a=1')
js = req.json()['graphql']['user']['full_name']
jss = req.json()['graphql']['user']['edge_followed_by']['count']
jsss = req.json()['graphql']['user']['edge_follow']['count']
 
print ('username :'+user)
print ('Nama :', js)
print ('Follower :', jss)
print ('Following :', jsss)