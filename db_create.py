# project/db_create.py

from project import db
from project.models import Task, User
from datetime import date

# create the database and the db table
db.create_all()

# insert data

# db.session.add(Task("Finish this turial", date(2015, 3, 13), 10, date(2015, 3, 13),1,1))
# db.session.add(Task("Finish Real Python", date(2015, 3, 13), 10, date(2015, 3, 13),1,1))

# commit the changes
db.session.commit()