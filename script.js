const loginButton = document.getElementById('loginButton');
const loginPopup = document.getElementById('loginPopup');
const closePopup = document.getElementById('closePopup');
const loginOption = document.getElementById('loginOption');
const accountOption = document.getElementById('accountOption');
const loginForm = document.getElementById('loginForm');
const registrationForm = document.getElementById('registrationForm');

loginButton.addEventListener('click', () => {
    loginPopup.style.display = 'block';
});

closePopup.addEventListener('click', () => {
    loginPopup.style.display = 'none';
});

loginOption.addEventListener('click', () => {
    loginForm.style.display = 'block';
    registrationForm.style.display = 'none';
});

accountOption.addEventListener('click', () => {
    registrationForm.style.display = 'block';
    loginForm.style.display = 'none';
});

window.addEventListener('click', (event) => {
    if (event.target === loginPopup) {
        loginPopup.style.display = 'none';
    }
});
