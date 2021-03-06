import unittest

from flask import json

from app.core import app
from app.model import USER, getUser, GROUP, TUTORSHIP, tutorship_class, group_class, user_class


class AuthTestCase(unittest.TestCase):
    uid = None
    gid = None
    tid = None

    @classmethod
    def setUpClass(cls):
        if getUser(login="admin") is None:
            query = USER.insert().values(login="admin", email="admin@admin.com", role="4", phone="00.00.00.00.00")
            res = query.execute()
            cls.uid = res.lastrowid
            query = GROUP.insert().values(name="test", year="2017", class_long="classe toto", class_short="toto",
                                          department="plop", ressources_dir="/plop/toto", resp_id=cls.uid,
                                          sec_id=cls.uid)
            res = query.execute()
            cls.gid = res.lastrowid
            query = TUTORSHIP.insert().values(student_id=cls.uid, ptutor_id=cls.uid, group_id=cls.gid)
            res = query.execute()
            cls.tid = res.lastrowid

    @classmethod
    def tearDownClass(cls):
        if cls.uid is not None and cls.gid is not None and cls.tid is not None:
            query = TUTORSHIP.delete().where(tutorship_class.id == cls.tid)
            query.execute()
            query = GROUP.delete().where(group_class.id == cls.gid)
            query.execute()
            query = USER.delete().where(user_class.id == cls.uid)
            query.execute()

    def setUp(self):
        self.app = app.test_client()

    def tearDown(self):
        pass

    def login(self, email, password):
        return self.app.post('/api/login',
                             data=json.dumps(
                                 dict(
                                     email=email,
                                     password=password
                                 )
                             ), content_type='application/json')

    def getUserInfo(self):
        return self.app.get('/api/userInfo')

    def logout(self):
        return self.app.delete('/api/login')

    def test_login_logout(self):
        rv = self.login('admin@admin.com', 'admin@admin.com')
        self.assertEqual(rv.status_code, 200, 'Login as admin Failed')

        rv = self.login('admin@admin.com', 'admin@admin.com')
        self.assertEqual(rv.status_code, 201, 'Login as admin succeed but should have already been done')

        rv = self.getUserInfo()
        self.assertEqual(rv.status_code, 200, 'Getting user info failed')
        self.assertEqual({"id": getUser(login="admin")["id"], "login": "admin", "email": "admin@admin.com", "role": "4",
                          "phone": "00.00.00.00.00"}, json.loads(rv.data)['USER'], 'Invalid user info')

        rv = self.logout()
        self.assertEqual(rv.status_code, 200, 'Logout Failed')

        rv = self.login('adminx@admin.com', 'admin@admin.com')
        self.assertEqual(rv.status_code, 401, 'Authentication not failed for the invalid user!')

        rv = self.getUserInfo()
        self.assertEqual(rv.status_code, 200, 'Getting user info failed')
        self.assertIsNone(json.loads(rv.data)['USER'], 'User info should be None')

        rv = self.login('admin@admin.com', 'admin@admin.comx')
        self.assertEqual(rv.status_code, 401,
                         'Authenticationnot failed for the invalid password !')

if __name__ == '__main__':
    unittest.main()
