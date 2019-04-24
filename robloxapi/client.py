import requests
from .User import User
from .Group import Group
def client(cookie=str()):
    global functions
    if cookie:
        cookies = {
            '.ROBLOSECURITY': cookie
        }
        r = requests.get('https://www.roblox.com/game/GetCurrentUser.ashx', cookies=cookies)
        if str(r.text) == 'null':
            print('Rython: Failed to login. Using Rython without login')
            functions = lambda: None
            functions.User = User(False, False)
            functions.Group = Group(False, False)
            return functions
        else:   
            functions = lambda: None
            functions.User = User(cookie, r)
            functions.Group = Group(cookie, r)
            return functions
    else:
        functions = lambda: None
        functions.User = User(False, False)
        functions.Group = Group(False, False)
        return functions



