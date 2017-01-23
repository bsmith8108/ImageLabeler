from flask import Flask, render_template, request, session
import json
app = Flask(__name__)

@app.route("/")
def image_label():
    """This will return the basic template from which one can label the images"""
    
    return render_template('image_select.html')


if __name__ == "__main__":
    app.run()
