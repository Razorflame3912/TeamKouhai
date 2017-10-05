from flask import Flask, render_template, request, session, redirect

app = Flask(__name__)
app.secret_key = 'THE TING GO SKRRRA PA PA KA KA KA'


@app.route('/', methods=['GET','POST'])
def root():
    if 'logout' in request.form:
        session.pop('user')
        session.pop('pass')
    elif 'user' in session:
        return redirect('/welcome')

    return render_template('login.html')

@app.route('/welcome', methods=['GET','POST'])
def welcome():

    if 'user' not in session:
        if 'username' not in request.form:
            return 'you stupid: go to root'
        elif request.form['username'] != u'':
            enteredUser = request.form['username']
            #print repr(enteredUser)
        else:
            return 'you stupid: no user'
    
        if 'pass' not in request.form:
            return 'you stupid: go to root'
        elif request.form['pass'] != u'':
            enteredPass = request.form['pass']
            print enteredPass
        else:
            return 'you stupid: no pass'
        session['user'] = enteredUser
        session['pass'] = enteredPass

    return render_template('welcome.html',name=session['user'])

if __name__ == '__main__':
    app.debug = True
    app.run()
