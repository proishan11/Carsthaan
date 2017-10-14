from flask import Flask, render_template
from flask_googlemaps import GoogleMaps
from flask_googlemaps import Map, icons

app = Flask(__name__, template_folder="templates")

GoogleMaps(app, key="AIzaSyD37xDW-B9hSPmuVH-p1u1VfH9bi_146j8")

@app.route('/')
def mymap():
    mymap = Map(
                identifier="view-side",
                varname="mymap",
                style="height:720px;width:1100px;margin:0;", # hardcoded!
                lat=37.4419, # hardcoded!
                lng=-122.1419, # hardcoded!
                zoom=15,
                markers=[(37.4419, -122.1419)] # hardcoded!
            )
    return render_template('first.html', mymap=mymap)


if __name__ == "__main__":
    app.run(debug=True, use_reloader=True)