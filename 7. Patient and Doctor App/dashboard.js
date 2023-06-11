const logoutBtn = document.getElementById("logoutBtn");
const welcomeMessage = document.getElementById("welcomeMessage");
logoutBtn.addEventListener("click", () => {
  localStorage.removeItem('message')
  window.location.href =
    "C:/Users/Admin/Desktop/flaskAccessToken/loginAndRegistration.html";
});
const responseMessage = localStorage.getItem("message");

let userType = "";
if (responseMessage.includes("Doctor")) {
  userType = "Doctor";
} else if (responseMessage.includes("Patient")) {
  userType = "Patient";
}

welcomeMessage.textContent = `Welcome ${userType} to the Dashboard`;
