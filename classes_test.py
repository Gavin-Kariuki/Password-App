from classes import User, Credentials  # importing both of my classes
import unittest

class TestUser(unittest.TestCase):

    def setUp(self) -> None:
        '''
        set up method to run before each test cases

        '''
        self.new_user = User("genichiro21", "password")

    def test_init(self):
        '''
        test to check whether the class has been initialized

        '''
        self.assertEqual(self.new_user.username, "genichiro21")
        self.assertEqual(self.new_user.password, "password")

    def test_save_user(self):
        '''
        test_save_user test case to check whether a new user has been saved into the user list

        '''

        self.new_user.save_user()  # saving the new user
        self.assertEqual(len(User.user_list), 1)

    def tearDown(self) -> None:
        '''
        tear down method that does clean up after each test case

        '''

        User.user_list = []

    def test_delete_user(self):
        '''test_delete_user case to check whether a user has been deleted from the user list'''

        self.new_user.save_user()
        test_user = User("genichiro21", "password")

        test_user.save_user()

        self.new_user.delete_user()  # deleting a user object
        self.assertEqual(len(User.user_list), 1)

    def test_display_users(self):
        ''' test_display_users case to test whether users have been displayed '''

        self.assertEqual(User.display_users(), User.user_list)


class TestCredentials(unittest.TestCase):
    def setUp(self) -> None:
        '''
        test case to run before each test case

        '''
        self.new_credentials = Credentials("Reddit", "genichiro21", "password")

    
    def test_save_credentials(self):
        '''
        test case to check if credentials have been added to the credentials list

        '''
        self.new_credentials.save_credentials()  # saving the credentials
        self.assertEqual(len(Credentials.credentials_list), 1)

    def tearDown(self) -> None:
        '''
        test case that does clean up after every test case

        '''

        Credentials.credentials_list = []

    def test_delete_credentials(self):
        '''test case to check if credentials have been deleted from the credentials list'''

        self.new_credentials.save_credentials()
        test_credentials = Credentials("Reddit", "genichiro21", "password")

        test_credentials.save_credentials()

        self.new_credentials.delete_credentials()
        self.assertEqual(len(Credentials.credentials_list), 1)

    def test_display_credentials(self):
        ''' test case to test whether credentials have been displayed '''

        self.assertEqual(Credentials.display_credentials(), Credentials.credentials_list)

    def test_save_multiple_credentials(self):
        ''' test case to test whether multiple credentials have been saved '''

        self.new_credentials.save_credentials()
        test_multiple = Credentials("Reddit", "genichiro21", "password")

        test_multiple.save_credentials()
        self.assertEqual(len(Credentials.credentials_list), 2)

    def test_find_credentials_by_account(self):
        ''' test case to test whether a credential could be found '''

        self.new_credentials.save_credentials()
        test_credentials = Credentials("Reddit", "genichiro21", "password")

        test_credentials.save_credentials()
        
        found_credentials = Credentials.find_by_account("Reddit")

        self.assertEqual(found_credentials.account, test_credentials.account)

    def test_username_exists(self):
        ''' test case that checks if the username exists '''

        self.new_credentials.save_credentials()
        test_username = Credentials("Reddit", "genichiro21", "password")

        test_username.save_credentials()

        username_exists = Credentials.username_exists("genichiro21")

        self.assertTrue(username_exists)

if __name__ == '__main__':
    unittest.main()