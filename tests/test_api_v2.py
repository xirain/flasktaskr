# tests/test_api_v2.py

import os
import unittest

from project import app, db, bcrypt
from project._config import basedir
from project.models import Task, User

from datetime import date

TEST_DB = 'test.db'

class APITests(unittest.TestCase):
    """docstring for APITests"""
    def setUp(self):
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False
        app.config['DEBUG'] = False
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, TEST_DB)
        self.app = app.test_client()
        db.create_all()

        self.assertEquals(app.debug, False)

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def add_tasks(self):
        db.session.add(
            Task(
                    "Run around in circles",
                    date(2015, 10, 22),
                    10,
                    date(2015, 10, 5),
                    1,
                    1
                )
            )

        db.session.commit()

        db.session.add(
            Task(
                    "Finish Real Python",
                    date(2016, 10, 22),
                    10,
                    date(2015, 10, 5),
                    1,
                    1
                )
            )

        db.session.commit()


    def test_connection_endpoint_returns_correct_datas(self):
        self.add_tasks()
        response = self.app.get('api/v2/tasks', follow_redirects=True)
        self.assertEquals(response.status_code, 200)
        self.assertEquals(response.mimetype, 'application/json')
        self.assertIn(b'Run around in circles', response.data)
        self.assertIn(b'Finish Real Python', response.data)

    def test_resource_endpoint_returns_correct_data(self):
        self.add_tasks()
        response = self.app.get('api/v2/task/2', follow_redirects=True)
        self.assertEquals(response.status_code, 200)
        self.assertEquals(response.mimetype, 'application/json')
        self.assertIn(b'Finish Real Python', response.data)
        self.assertNotIn(b'Run around in circles', response.data)

    def test_invalid_resource_endpoint_returns_error(self):
        self.add_tasks()
        response = self.app.get('api/v2/task/209', follow_redirects=True)
        self.assertEquals(response.status_code, 404)
        self.assertEquals(response.mimetype, 'application/json')
        self.assertIn(b'Element does not exist', response.data)

if __name__ == '__main__':
    unittest.main()
