from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=True, nullable=False)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        user_name = request.form['user_name']
        user = User(name=user_name)
        db.session.add(user)
        db.session.commit()
        return 'User added'
    else:
        return '<form method="POST"><input name="user_name"><button type="submit">Add user</button></form>'

if __name__ == '__main__':
    app.run()