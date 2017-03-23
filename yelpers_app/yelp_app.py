from flask import Flask, render_template, request, jsonify
from yelper import get_businesses

app = Flask(__name__)

@app.route('/', methods =['GET'])
def home():
    return render_template("home.html")






@app.route('/pull/<string:location>/<string:type>', methods =['GET'])
def pull(location='Denver',type='food'):
    '''This endpoint gets the data from the api - you need to make the home.html button to submit reference this endpoint and
    pass the location and type (which in this case will default to food), it will return that info and you can either generate a new
    page with the info as you did in your other project or use jquery/ajax to update the same page over and over

    '''

    bus = get_businesses(location=location,term=type)
    for x in bus:
        print(x)
    return render_template('home.html', businesses=bus)
if __name__ == "__main__":
    app.run(host="localhost")
   