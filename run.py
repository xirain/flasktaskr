# coding: UTF-8
# run.py

from project import app
import os
port = int(os.environ.get('PORT', 80))
app.run(host='0.0.0.0', port=port)
