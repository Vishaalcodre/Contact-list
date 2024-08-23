import { useState } from "react";

const ContactForm = ({}) => {
  const [firstName, setFirstName] = useState("");
  const [lastName, setLastName] = useState("");
  const [email, setEmail] = useState("");

  const onSubmit = async (e) => {
    //Avoid Refreshing page automatically
    e.preventDefault()

    const data = {
        firstName,
        lastName,
        email,
    }

    const url = "http://127.0.0.1:5000/create_contact"

    const options = {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify(data)
    }

    const response = await fetch(url, options)
    if (response.status !== 201 && response.status !== 200) {
        const data = await response.json()
        alert(data.message)
    }
    else {
        //successful message
        

    }
    console.log(data);
  }

  return (
    <form onSubmit={onSubmit}>
      <div>
        <label htmlFor="firstName">First Name:</label>
        <input
          type="text"
          name="firstName"
          value={firstName}
          id="firstName"
          onChange={(e) => setFirstName(e.target.value)}
        />
      </div>
      <div>
        <label htmlFor="lastName">Last Name:</label>
        <input
          type="text"
          name="lastName"
          value={lastName}
          id="lastName"
          onChange={(e) => setLastName(e.target.value)}
        />
      </div>
      <div>
        <label htmlFor="email">Email:</label>
        <input
          type="email"
          name="email"
          value={email}
          id="email"
          onChange={(e) => setEmail(e.target.value)}
        />
      </div>
      <button type="submit">
        Create Contact
      </button>
    </form>
  );
};

export default ContactForm;
