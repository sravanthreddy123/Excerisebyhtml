from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///form_submissions.db'
db = SQLAlchemy(app)

class Submission(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(50), nullable=False)
    submission_time = db.Column(db.DateTime, default=datetime.utcnow)

db.create_all()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form.get('name')
    email = request.form.get('email')

    new_submission = Submission(name=name, email=email)
    db.session.add(new_submission)
    db.session.commit()

    return f'Thank you, {name}! email ({email}) has been submitted.'

@app.route('/submissions')
def display_submissions():
    submissions = Submission.query.all()
    return render_template('submissions.html', submissions=submissions)

if __name__ == '__main__':
    app.run(debug=True)
