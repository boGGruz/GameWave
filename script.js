const loginButton = document.getElementById('loginButton');
const loginPopup = document.getElementById('loginPopup');
const closePopup = document.getElementById('closePopup');
const loginOption = document.getElementById('loginOption');
const accountOption = document.getElementById('accountOption');
const loginForm = document.getElementById('loginForm');
const registrationForm = document.getElementById('registrationForm');
const changeNickButton = document.getElementById('changeNickButton');
const overlay = document.getElementById('overlay');
const changeUsername = document.getElementById('change-username');
const closeChange = document.getElementById('closechange');
const openButtonlibrary = document.getElementById("openButtonlibrary");
const modallibrary = document.getElementById("modal-library");
const closelibrary = document.getElementById("close-library");

let loginFormVisible = false;

loginButton.addEventListener('click', () => {
    loginPopup.style.display = 'block';
    if (!loginFormVisible) {
        loginOption.style.display = 'block'
        accountOption.style.display = 'block'
    }
});

closePopup.addEventListener('click', () => {
    loginPopup.style.display = 'none';
    registrationForm.style.display = 'none';
    loginForm.style.display = 'none';
    loginFormVisible = false;
});

loginOption.addEventListener('click', () => {
    loginForm.style.display = 'block';
    registrationForm.style.display = 'none';
    loginFormVisible = true;
    loginOption.style.display = 'none'
    accountOption.style.display = 'none'
});

accountOption.addEventListener('click', () => {
    registrationForm.style.display = 'block';
    loginForm.style.display = 'none';
    loginFormVisible = true;
    accountOption.style.display = 'none'
    loginOption.style.display = 'none'
});


changeNickButton.addEventListener('click', () => {
    overlay.style.display = 'block';
});
  
closeChange.addEventListener('click', () => {
    overlay.style.display = 'none';
});


openButtonlibrary.addEventListener('click', () => {
    modallibrary.style.display = 'block';
});

closelibrary.addEventListener('click', () => {
    modallibrary.style.display = 'none';
});

window.addEventListener('click', (event) => {
  if (event.target === modallibrary) {
    modallibrary.style.display = 'none';
  }
});

