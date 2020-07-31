from flask import Flask, render_template, jsonify, request

app = Flask(__name__, template_folder="templates", static_folder= "static")

# Function for testing page
@app.route('/')
def Index():
    return render_template('main.html')

# Function for API call
@app.route('/test', methods= ['POST'])
def Test():
    returnable = {}
    returnable["return_string"] = chop(request.json["string_to_cut"])
    print(returnable)
    return jsonify(returnable)

# Function to work on string
def chop(string):
    returnable = ""
    for c in range(len(string)):
        if c % 3 == 2:
            returnable += string[c]
    return returnable

print(chop("003003003003003003")) #for testing

app.run(debug=True, host="0.0.0.0", port=5000)
