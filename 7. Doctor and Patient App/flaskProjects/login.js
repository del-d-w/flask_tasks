const loginForm = document.getElementById("loginForm");
const usernameInput = document.getElementById("username");
const passwordInput = document.getElementById("password");
loginForm.addEventListener("submit", (event) => {
  event.preventDefault();
  const username = usernameInput.value;
  const password = passwordInput.value;
  fetch("http://127.0.0.1:5000/login", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({
      user_name: username,
      password: password,
    }),
  })
    .then((response) => response.json())
    .then((data) => {
      console.log(data);
      localStorage.setItem("message", data.message);
      window.location.href =
        "C:/Users/Admin/Desktop/flaskProjects/dashboard.html";
    })
    .catch((error) => {
      console.error("Error:", error);
    });
});