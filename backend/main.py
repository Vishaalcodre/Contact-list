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
@app.route("/create_contact", methods=["POST"])
def create_contact():
    first_name = request.json.get("firstName")
    last_name = request.json.get("lastName")
    email = request.json.get("email")

    if not first_name or not last_name or not email:
        return(
            #Converts the python object into json object and Returns the data
            jsonify({"message": "You must include first name, last name and email"}), 400
        )
    
    new_contact = Contact(first_name= first_name, last_name= last_name, email= email)

    try:
        #Adding the new contact in the DB
        db.session.add(new_contact)

        #Storing the data in the DB
        db.session.commit()

        print(new_contact)

    except Exception as e:
        return jsonify({"message": str(e)}), 400
    
    return(
        #Converts the python object into json object and Returns the data
        jsonify({"message": "Contact Created!"}), 201
        
    )

#Update Decorator
@app.route("/update_contact/<int:user_id>", methods=["PATCH"])
def update_contact(user_id):
    contact = Contact.query.get(user_id)

    if not contact:
        return jsonify({"message": "Contact not found"}), 404
    
    data = request.json

    #if the value is updated contact will be updating new value if not the old value is saved to the contact
    contact.first_name = data.get("firstName", contact.first_name)
    contact.last_name = data.get("lastName", contact.last_name)
    contact.email = data.get("email", contact.email)

    #Storing the updated data in the DB
    db.session.commit()

    #Converts the python object into json object and Returns the data
    return jsonify({"message": "Contact Updated!"}), 200

#Delete decorator
@app.route("/delete_contact/<int:user_id>", methods=["DELETE"])
def delete_contact(user_id):
    contact = Contact.query.get(user_id)

    if not contact:
        return jsonify({"messabe": "Contact not found"}), 404
    
    db.session.delete(contact)
    
    #Storing the updated data in the DB
    db.session.commit()

    #Converts the python object into json object and Returns the data
    return jsonify({"message": "Contact Deleted!"}), 200

if __name__ == "__main__":
    with app.app_context():
        #To create Database
        db.create_all()

    app.run(debug=True)