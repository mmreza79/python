from flask import Flask, render_template
import config
import db

app = Flask(__name__)

@app.route('/', endpoint="homepage", methods=['GET'])
def index():
    # return "<h1>Hello, World!!</h1>"
    return render_template('index.html.j2')

@app.route('/data/create', endpoint="create", methods=['GET'])
def create():
    db.insert_data(["Mohsin", "Reza"])
    
    title='Create record'
    return render_template('create.html.j2', title=title)

@app.route('/data/show', endpoint="show", methods=['GET'])
def show():
    data=db.fetch_data()
    title='Database records'
    return render_template('show.html.j2', title=title, data=data)


if __name__ == '__main__':
    db.create_table()
    app.run(debug=True)