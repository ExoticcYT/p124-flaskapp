from flask import Flask, jsonify, request

app = Flask(__name__)
contacts = [
    {
        "id": 1,
        "name": u"Anish",
        "contact": u"7734569876",
        "done": False
    },
    {
        "id": 2,
        "name": u"Aarav",
        "contact": u"8578592515",
        "done": False
    }
]
@app.route("/add-data",methods = ["POST"]) 
def add_task():
    if not request.json:
        return jsonify({
            "status": "error",
            "message": "buddy, who the frik you contacting?"
        }, 400)
#400 is error code
    contact = {
        "id": contacts[-1]['id']+1,
        "name": request.json['name'],
        "contact": request.json.get('contact', ''),
        "done": False
    }
    contacts.append(contact)
    return jsonify({
        "status": "success",
        "message": "we got your contacts successfully"
    })
@app.route("/get-data")
def get_task():
    return jsonify({
        "data": contacts
    })
if(__name__ == "__main__"):
    app.run(debug = True)