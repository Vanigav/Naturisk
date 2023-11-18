from flask import Flask, render_template, request, redirect
import csv
app = Flask(__name__)
print(__name__)

@app.route('/')
def home():
    return render_template('index.html')
'''
@app.route('/login', methods=['POST', 'GET'])
def login():
    error = None
    if request.method == 'POST':
        if valid_login(request.form['username'],
                       request.form['password']):
            return log_the_user_in(request.form['username'])
        else:
            error = 'Invalid username/password'
    # the code below is executed if the request method
    # was GET or the credentials were invalid
    return render_template('login.html', error=error)
'''
@app.route('/Submitted', methods = ['POST', 'GET'])
def submit():
    if request.method == 'POST':
        data = request.form.to_dict()
        write_database(data)
        return redirect('/Thanks.html')
    else:
        return 'Please try again!'

def write_database(data):
    with open('DiseaseRequest.csv', mode='a', newline = '') as my_file:
        email = data['email']
        subject = data['subject']
        message = data['message']
        csv_writer = csv.writer(my_file, delimiter = ',', quotechar = '"', quoting = csv.QUOTE_MINIMAL)
        csv_writer.writerow([email, subject, message])

@app.route('/index.html')
def index():
    return render_template('index.html')

@app.route('/contact.html')
def contact():
    return render_template('contact.html')

@app.route('/Thanks.html')
def Thanks():
    return render_template('Thanks.html')

@app.route('/NeedleBlight.html')
def NeedleBlight():
    return render_template('NeedleBlight.html')

@app.route('/Cankers.html')
def Cankers():
    return render_template('Cankers.html')

@app.route('/TarSpots.html')
def TarSpots():
    return render_template('TarSpots.html')

@app.route('/Anthracnose.html')
def Anthracnose():
    return render_template('Anthracnose.html')

@app.route('/HardwoodDecay.html')
def HardwoodDecay():
    return render_template('HardwoodDecay.html')
