from flask import Flask,jsonify,request

app = Flask(__name__)

tasks = [
    {
        'id': 1, 
        'Contact': u'98247963254', 
        'Name': u'John', 
        'done': False
    },
    {
        'id':2,
        'Contact': u'98242963454',
        'Name':"Shang", 
        'done': False
    }
]

@app.route("/")
def root():
    return "Hello World!"

@app.route("/add-data",methods=["POST"])
def add_data():
    if not request.json:
        return jsonify({ "status":"error", "message": "Please provide the data!" },400)
    task = {'id': tasks[-1]['id'] + 1, 'Contact': request.json['Contact'], 'Name': request.json.get('Name', ""), 'done': False}
    tasks.append(task)
    return jsonify({"status":"Success!","message":"Data added successfully"})

@app.route("/get-data") 
def get_task(): 
    return jsonify({ "data" : tasks })

if __name__ == "__main__":
    app.run(debug=True)