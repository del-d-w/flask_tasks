 // Get references to the form and input elements
        const loginForm = document.getElementById('loginForm');
        const usernameInput = document.getElementById('username');
        const passwordInput = document.getElementById('password');

        // Add event listener to the form's submit event
        loginForm.addEventListener('submit', (event) => {
            event.preventDefault(); // Prevent the form from submitting

            // Get the entered username and password
            const username = usernameInput.value;
            const password = passwordInput.value;

            // Perform your desired login logic here
            // You can use the Fetch API or any other AJAX method to send the login request to the backend

            // Example using Fetch API
            fetch('http://127.0.0.1:5000/login', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({
                    username: username,
                    password: password
                })
            })
            .then(response => response.json())
            .then(data => {
                // Handle the response from the server
                console.log(data); // You can customize this part based on your needs
                
                // Example: Redirect to a different page upon successful login
                if (data.access_token) {
                    localStorage.setItem('accessToken',data.access_token)
                    window.location.href = 'file:///C:/Users/Admin/Desktop/flaskAccessToken/dashboard.html';
                }
            })
            .catch(error => {
                console.error('Error:', error);
                // Handle any errors that occur during the login process
            });
        });