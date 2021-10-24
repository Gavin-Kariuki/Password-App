import pyperclip

class User:
    '''class that generates new instances of users'''

    user_list = [] #empty user list

    def __init__(self, username, password) -> None:
        '''blueprint that defines the properties of a user'''

        self.username = username
        self.password = password

    def save_user(self):
        '''save_user method saves contact objects into user_list'''
        
        User.user_list.append(self)

    def delete_user(self):
        '''delete_user method deletes contact objects in the user_list'''

        User.user_list.remove(self)