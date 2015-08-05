# project/api/views_v2.py

from functools import wraps
from flask import flash, redirect, jsonify, session, url_for, Blueprint, make_response

from flask_restful import Resource, Api

from project import db, app
from project.models import Task

################
#### config ####
################


api = Api(app)

###############################
###### helper functions #######
###############################

def login_required(test):
    @wraps(test)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return test(*args, **kwargs)

        else:
            flash('You need to login first.')
            return redirect(url_for('users.login'))

    return wrap


#######################
###### Resouces #######
#######################

class TaskResource(Resource):
    """docstring for Task"""
    
    def get(self, task_id=None):
        result = db.session.query(Task).filter_by(task_id=task_id).first()
        if result:
            result = {
                'task_id': result.task_id,
                'task name': result.name,
                'due date': str(result.due_date),
                'priority': result.priority,
                'posted date': str(result.posted_date),
                'status': result.status,
                'user id': result.user_id
            }
            return result
        else:
            result = {"error": "Element does not exist"}            
            return result, 404


class TasksResource(Resource):
    def get(self):
        results = db.session.query(Task).limit(10).offset(0).all()
        json_results = []
        for result in results:
            data = {
                'task_id': result.task_id,
                'task name': result.name,
                'due date': str(result.due_date),
                'priority': result.priority,
                'posted date': str(result.posted_date),
                'status': result.status,
                'user id': result.user_id
            }
            json_results.append(data)

        return json_results

api.add_resource(TaskResource, '/api/v2/task/<int:task_id>')
api.add_resource(TasksResource, '/api/v2/tasks/', endpoint='Tasks')
