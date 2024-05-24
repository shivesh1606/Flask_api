import unittest
import requests

BASE_URL = "http://127.0.0.1:5000/accounts"

class TestAccountAPI(unittest.TestCase):

    def setUp(self):
        # Create a test account to use for some of the tests
        self.test_account = {
            "first_name": "Test",
            "last_name": "User",
            "email": "testuser@example.com",
            "company": "TestCompany",
            "age": 30,
            "city": "TestCity",
            "state": "TS",
            "zip": "12345",
            "web": "http://testuser.com"
        }
        response = requests.post(BASE_URL, data=self.test_account)
        self.assertEqual(response.status_code, 200)
        self.account_id = response.json().get("id")

    def tearDown(self):
        # Delete the test account
        response = requests.delete(f"{BASE_URL}/{self.account_id}")
        self.assertEqual(response.status_code, 200)

    def test_get_accounts(self):
        response = requests.get(BASE_URL)
        self.assertEqual(response.status_code, 200)
        self.assertIn("accounts", response.json())

    def test_create_account(self):
        new_account = {
            "first_name": "John",
            "last_name": "Doe",
            "email": "johndoe@example.com",
        }
        response = requests.post(BASE_URL, data=new_account)
        self.assertEqual(response.status_code, 200)
        self.assertIn("id", response.json())
        account_id = response.json()["id"]
        response = requests.delete(f"{BASE_URL}/{account_id}")
        self.assertEqual(response.status_code, 200)

    def test_get_account_by_id(self):
        response = requests.get(f"{BASE_URL}/{self.account_id}")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["first_name"], self.test_account["first_name"])

    def test_update_account(self):
        update_data = {
            "first_name": "UpdatedName"
        }
        response = requests.put(f"{BASE_URL}/{self.account_id}", data=update_data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["first_name"], "UpdatedName")

    def test_delete_account(self):
        new_account = {
            "first_name": "Jane",
            "last_name": "Smith",
            "email": "janesmith@example.com",
        }
        response = requests.post(BASE_URL, data=new_account)
        self.assertEqual(response.status_code, 200)
        account_id = response.json()["id"]
        response = requests.delete(f"{BASE_URL}/{account_id}")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["message"], f"Account with Id \"{account_id}\" deleted successfully!")

if __name__ == "__main__":
    unittest.main()
