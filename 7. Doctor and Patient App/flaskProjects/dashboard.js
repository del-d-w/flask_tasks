const logoutBtn = document.getElementById("logoutBtn");
const welcomeMessage = document.getElementById("welcomeMessage");
logoutBtn.addEventListener("click", () => {
  localStorage.removeItem('message')
  window.location.href =
    "C:/Users/Admin/Desktop/flaskProjects/login-registration.html";
});
const responseMessage = localStorage.getItem("message");
const name = responseMessage.split(' ')[1];
let userType = "";
if (responseMessage.includes("Doctor")) {
  userType = "Doctor " + name;
} else if (responseMessage.includes("Patient")) {
  userType = name;
}


welcomeMessage.textContent = `Welcome ${userType} to the Dashboard`;