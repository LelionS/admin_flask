from flask import Flask, render_template
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from database import db, app
from models import User

app.config['SECRET_KEY'] = 'b\xc3\xf3\xd1*^\xea\xb8\xb0J\x97\x9f\x1b\x03\xe7\xf3\xdc\xdd\x0ec9l\x90h\x08'
# Initialize Flask-Admin
admin = Admin(app, name='Admin Portal', template_mode='bootstrap3')
admin.add_view(ModelView(User, db.session))

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
