const patientForm = document.getElementById('patientForm');

patientForm.addEventListener('submit', (event) => {
    event.preventDefault();

    const firstName = document.getElementById('firstName').value;
    const lastName = document.getElementById('lastName').value;
    const dob = document.getElementById('dob').value;
    const username = document.getElementById('username').value;
    const password = document.getElementById('password').value;
    const address = document.getElementById('address').value;
    const phoneNumber = document.getElementById('phoneNumber').value;
    const email = document.getElementById('email').value;

    fetch('http://127.0.0.1:5000/register/patient', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            first_name: firstName,
            last_name: lastName,
            dob: dob,
            username: username,
            password: password,
            address: address,
            phone_number: phoneNumber,
            email: email
        })
    })
    .then(response => response.json())
    .then(data => {
        alert('Patient registered successfully!');
        window.location.href = 'C:/Users/Admin/Desktop/flaskAccessToken/loginregistration.html';
    })
    .catch(error => {
        console.error('Error:', error);
    });
});
