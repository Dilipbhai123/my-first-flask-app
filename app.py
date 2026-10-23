from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from sqlalchemy import desc
from sqlalchemy import or_

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///todo.db"
# app.config["SQLALCHEMY_TRACK_MODOFICATION"] = False
db = SQLAlchemy(app)

class Todo(db.Model):
    sno = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(200), nullable = False)
    dsc = db.Column(db.String(500), nullable = False)
    create_at = db.Column(db.DateTime, default = datetime.utcnow)


    def __repr__(self):
        return f"{self.sno} - {self.title}"
    
with app.app_context():
    db.create_all()

@app.route("/")
def todos():
    todos = Todo.query.all()
    return render_template('index.html', todos=todos)

@app.route("/add", methods = ["GET", "POST"])
def add():
    if request.method == "POST":
        s = Todo(title=request.form["title"],
                dsc=request.form["dsc"])
        db.session.add(s)
        db.session.commit()
        return redirect("/")

@app.route('/delete/<int:sno>')
def delete(sno):
    todo = Todo.query.filter_by(sno=sno).first()
    db.session.delete(todo)
    db.session.commit()
    return redirect("/")

@app.route("/update/<int:sno>", methods=['GET', 'POST'])
def update(sno):
    updatetodo = Todo.query.filter_by(sno=sno).first_or_404()

    if request.method == "POST":
        updatetodo.title = request.form['title']
        updatetodo.dsc = request.form['dsc']
        db.session.commit()
        return redirect("/")

    return render_template('update.html', updatetodo=updatetodo)

@app.route("/about")
def about():
    return render_template('about.html')

@app.route("/contact")
def contact():
    return render_template('contact.html')

@app.route("/search", methods=['GET', 'POST'])
def search():
    query = None
    results = []
    if request.method == 'POST':
        query = request.form.get('search', '').strip()
        if query:
            results = Todo.query.filter(
                or_(
                    Todo.title.ilike(f"%{query}%"),
                    Todo.dsc.ilike(f"%{query}%")
                )
            ).all()
    return render_template("search.html", query=query, results=results)

if __name__ == "__main__":
    app.run(debug=True)