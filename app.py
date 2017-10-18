from flask import Flask, render_template, request, json
app = Flask(__name__)

@app.route("/")
def main():
	return render_template('designs/UI/index.html')


@app.route('/showSignUp')
def showSignUp():
	return render_template('designs/UI/UserReg.html')

#takes the user to the login page
@app.route('/showLogin')
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
	
	credentials= {username:pwd, email:pwd}

	#validation of the data received
	if pwd == conpwd:
		return render_template('designs/UI/RecipeCategories.html' , uname = username)
		pass
	else:
		return render_template('designs/UI/UserReg.html', errorMessage = "!!YOUR CONFIRMATION PASSWORD DOESN'T MATCH YOUR PASSWORD!!")

#handles User logins
@app.route('/userLogin', methods = ['POST'])	
def userLogin():
	#fetching login credentials
	username = request.form['username']
	pwd = request.form['password']


	#test login details
	credentials = {'redlion':'ericardo47'}

	#validating the user
	if credentials.get(username, None) == None or pwd != credentials[username]:
		return render_template('designs/UI/LoginPage.html', errorMessage ="username or password not match")
	else:
		return render_template('designs/UI/RecipeCategories.html', uname = username)


if __name__ == '__main__':
	app.run()
