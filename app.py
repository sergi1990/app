from flask import Flask, render_template, request
from flask_mysqldb import MySQL

app = Flask(__name__)
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'flask_contacs'

mysql = MySQL(app)


@app.route('/')
def Index():
    return render_template('index.html')

@app.route('/add_contact', methods= ['POST'])
def  add_contact():
    if request.method == 'POST':
     fullname = request.form['fullname']
     phone = request.form['phone']
     email= request.form['email']

     

     return 'received'

@app.route('/edit')
def edit_contact():
    return 'edit contact'

@app.route('/delete')
def delete_contact():
    return 'delete contac'


#if __name__ == '__name__':
 # app.run(port = 5000, debug = True)

# el gay me ayudo