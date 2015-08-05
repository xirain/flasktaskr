# project/tasks/forms.py

from flask_wtf import Form
from wtforms import StringField, PasswordField, DateField, IntegerField, SelectField
from wtforms.validators import DataRequired

class AddTaskForm(Form):
    """docstring for AddTaskForm"""
    task_id = IntegerField()
    name = StringField('Task Name', validators=[DataRequired()])
    due_date = DateField(
        'Due Date (mm/dd/yyyy)',
        validators=[DataRequired()], format='%m/%d/%Y')

    priority = SelectField(
            'Priority',
            validators=[DataRequired()],
            choices=[tuple([str(x), str(x)]) for x in range(1, 11) ]
        )

    status = IntegerField('Status')