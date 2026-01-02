#write a program for making a single page webapp using flask
from flask import Flask, render_template
app = Flask(__name__)
@app.route('/')
def home():
    return render_template('index.html')
if __name__ == '__main__':
    app.run(debug=True)
# The above code creates a simple Flask web application that serves a single page.
# You need to create an 'index.html' file in a folder named 'templates' in the same directory as this script.
# The 'index.html' file can contain any HTML content you want to display on the web page.
# Example content for 'index.html':
'''
<!DOCTYPE html>
<html>
<head>
    <title>My Single Page Webapp</title>
</head>
<body>
    <h1>Welcome to My Webapp!</h1>
    <p>This is a simple single page web application using Flask.</p>
</body>
</html>
'''
# Save the above HTML content in 'templates/index.html' to see it rendered by the Flask app.

    