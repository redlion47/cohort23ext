from flask import Flask, render_template, request, json
app = Flask(__name__)

@app.route("/")
def main():
	return render_template('designs/UI/index.html')


@app.route('/UserReg.html')
def showSignUp():
	return render_template('designs/UI/UserReg.html')

#takes the user to the login page
@app.route('/LoginPage.html')
def showLogin():
	return render_template('designs/UI/LoginPage.html')

#a method to enable the use to signup
@app.route('/UserReg' , methods =['POST'])
def signUp():
	#code to get the input entered by the user
	username = request.form['username']
	email = request.form['email']
	pwd = request.form['password']
	conpwd = request.form['conpassword']

	#validation of the data received
	return username, email, pwd, conpwd




if __name__ == '__main__':
	app.run()