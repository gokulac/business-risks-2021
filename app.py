from flask import Flask,render_template, jsonify, request
import random
import json
import business


app  = Flask(__name__)
PORT = 3000

@app.route("/", methods=["GET","POST"])
def startpy():

    result = {

        "Greetings" : "Tactlabs welcomes you"
    }

    # return jsonify(result)
    return render_template("radial-bar.html")

@app.route("/bar", methods=["GET","POST"])
def bar_chart():

    result = {

        "Greetings" : "Tactlabs welcomes you"
    }

    # return jsonify(result)
    return render_template("bar.html") 

@app.route("/column", methods=["GET","POST"])
def column_chart():

    result = {

        "Greetings" : "Tactlabs welcomes you"
    }

    # return jsonify(result)
    return render_template("column.html") 

@app.route("/pie", methods=["GET","POST"])
def pie_chart():

    result = {

        "Greetings" : "Tactlabs welcomes you"
    }

    # return jsonify(result)
    return render_template("pie.html") 

@app.route("/donut", methods=["GET","POST"])
def donut_chart():

    result = {

        "Greetings" : "Tactlabs welcomes you"
    }

    # return jsonify(result)
    return render_template("donut.html") 

@app.route("/cylinder", methods=["GET","POST"])
def cylinder_chart():

    result = {

        "Greetings" : "Tactlabs welcomes you"
    }

    # return jsonify(result)
    return render_template("cylinder.html") 

@app.route("/line", methods=["GET","POST"])
def line_chart():

    result = {

        "Greetings" : "Tactlabs welcomes you"
    }

    # return jsonify(result)
    return render_template("line.html") 

@app.route("/Responses", methods=["GET","POST"])
def Responses_chart():

    result = {

        "Greetings" : "Tactlabs welcomes you"
    }

    # return jsonify(result)
    return render_template("Responses.html") 

@app.route("/stacked-Responses", methods=["GET","POST"])
def staccked_Responses_chart():

    result = {

        "Greetings" : "Tactlabs welcomes you"
    }

    # return jsonify(result)
    return render_template("stacked-Responses.html") 


@app.route("/semi-circle-donut", methods=["GET","POST"])
def semi_circle_donut():

    result = {

        "Greetings" : "Tactlabs welcomes you"
    }

    # return jsonify(result)
    return render_template("semi-circle-donut.html") 



'''
http://0.0.0.0:3000/api/data
'''

@app.route("/api/data", methods=["GET"])
def api_get_data():

    result = business.get_data()

    # result_dict = {

    #     'year'       : year,
    #     'pytorch'    : pytorch,
    #     'tensorFlow' : tensorFlow

    # }

    return jsonify(result)

'''
http://0.0.0.0:3000/api/add
http://0.0.0.0:3000/api/add?year=2017&ontario_tourist=20345&quebec_tourist=200
http://0.0.0.0:3000/api/add?year=2021&pytorch=180&tensorFlow=90
'''
@app.route("/api/add", methods=["GET"])
def api_add_data():

    Risk           = request.values.get('Risk')
    Responses            = request.values.get('Responses')

    result = {
        'Risk'          : Risk,
        'Responses'           : Responses
    }
    result_data = business.add_row(Risk,Responses)

    return jsonify(result)


if __name__ == "__main__":
    app.run(debug = True,host="0.0.0.0",port = PORT)