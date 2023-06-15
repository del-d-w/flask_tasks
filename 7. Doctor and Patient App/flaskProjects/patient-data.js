const patientForm = document.getElementById("patientForm");
const errorMessage = document.getElementById("errorMessage");

patientForm.addEventListener("submit", (event) => {
  event.preventDefault();

  const firstName = document.getElementById("firstName").value;
  const lastName = document.getElementById("lastName").value;
  const dob = document.getElementById("dob").value;
  const username = document.getElementById("username").value;
  const password = document.getElementById("password").value;
  const address = document.getElementById("address").value;
  const phoneNumber = document.getElementById("phoneNumber").value;
  const email = document.getElementById("email").value;

  fetch("http://127.0.0.1:5000/register/patient", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({
      first_name: firstName,
      last_name: lastName,
      dob: dob,
      user_name: username,
      password: password,
      address: address,
      phone_number: phoneNumber,
      email_id: email,
    }),
  })
  .then((response) => response.json())
  .then((data) => {
    // Registration failed, display error message
    if (data.message=="Username already exists!") {
      errorMessage.textContent = data.message;
      
    } else {
      // Registration successful
      alert("Patient registered successfully!");
      window.location.href =
        "C:/Users/Admin/Desktop/flaskProjects/login-registration.html";
    }
  })
  .catch((error) => {
    console.error("Error:", error);
  });
});