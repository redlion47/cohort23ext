from flask import Flask, render_template, request, json
app = Flask(__name__)

#start the home page
@app.route("/")
def main():
	return render_template('designs/UI/index.html')

#take the users to the registration page
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
		return render_template('designs/UI/ViewPage.html' , uname = username, result ={})
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
	if username== None and pwd == None:#credentials.get(username, None) == None or pwd != credentials[username]:
		return render_template('designs/UI/LoginPage.html', errorMessage ="username or password not match")
	else:
		return render_template('designs/UI/ViewPage.html', uname = username, result ={})

#adding recipe category
"""@app.route('/addCategory')
def addCategory():
	return render_template('designs/UI/addCategory.html')

#adds categories to the site
@app.route('/categoryAdded', methods = ['POST'])
def addedCategory():

	category = list()
	category.append(str(request.form['categoryName']))#adds the entered category to a list

	return render_template('designs/UI/RecipeCategories.html', result = category)"""

#adding recipe to the list
@app.route('/addRecipe')
def addRecipe():
	return render_template('designs/UI/addRecipe.html')


#adds recipe to the site
@app.route('/recipeAdded', methods = ['POST'])
def addedRecipe():

	recipe_name = str(request.form['recipeName'])
	ingredients = str(request.form['ingredients'])
	instructions = str(request.form['instructions'])


	#category = list()
	category = {}
	category['recipeName'] = recipe_name
	category['Ingredients'] = ingredients
	category['Instructions'] = instructions
	#category.append(str(request.form['recipeName']))#adds the entered category to a list

	return render_template('designs/UI/ViewPage.html', result = category)

if __name__ == '__main__':
     app.run()