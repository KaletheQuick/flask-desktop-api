from flask import Flask, render_template, jsonify, request, abort

app = Flask(__name__, template_folder="templates", static_folder= "static")

# Function for testing page
@app.route('/')
def Index():
    return render_template('main.html')

# Function for API call
@app.route('/test', methods= ['POST'])
def Test():
    returnable = {}
    
    if request.is_json and "string_to_cut" in request.json:
        returnable["return_string"] = chop(request.json["string_to_cut"])
    else:
        abort(400)
    return jsonify(returnable)

# Function to work on string
def chop(inputString):
    returnable = ""
    for c in range(len(inputString)):
        if c % 3 == 2:
            returnable += inputString[c]
    return returnable


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
