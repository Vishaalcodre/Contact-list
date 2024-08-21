from flask import jsonify, request
from config import db, app
from models import Contact

#GET Contacts Decorator
@app.route("/contacts", methods=["GET"])
def get_contacts():
    #This gives all the data from the database in Python objects
    contacts = Contact.query.all()

    #Creates a list of data from to_json method
    json_contacts = list(map(lambda x: x.to_json(), contacts))

    #Converts the python object into json object and Returns the data
    return jsonify({"contacts": json_contacts}), 200

#Create Contacts Decorator
@app.route("/create_contact", method=["POST"])
def create_contact():
    first_name = request.json.get("firstName")
    last_name = request.json.get("lastName")
    email = request.json.get("email")

    if not first_name or not last_name or not email:
        return(
            jsonify({"message": "You must include first name, last name and email"}), 400
        )
    
    new_contact = Contact(first_name= first_name, last_name= last_name, email= email)

    try:
        db.session.add(new_contact)
        db.session.commit()

    except Exception as e:
        return jsonify({"message": str(e)}), 400
    
    return(
        jsonify({"message": "User Created!"}), 201
    )

if __name__ == "__main__":
    with app.app_context():
        #To create Database
        db.create_all()

    app.run(debug=True)