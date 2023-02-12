function formValidation() {
  return validateFirstname() &&
      validateLastname() &&
      validateUsername() &&
      validateEmail() &&
      validatePassword();
}



function validateFirstname() {
    let firstname = document.forms["register"]["id_first_name"];
    if (firstname.value.trim() === '') {
        errorMessageDisplay(firstname, 'firstname-error-message', 'please enter your firstname');
        return false;
    } else if (containsNumbers(firstname.value.trim())) {
        errorMessageDisplay(firstname, 'firstname-error-message', 'firstname should contain letters only');
        return false;
    } else {
        errorMessageRemove(firstname, 'firstname-error-message')
        return true;
    }
}

function validateLastname() {
    let lastname = document.forms["register"]["id_last_name"];
    if (lastname.value.trim() === '') {
        errorMessageDisplay(lastname, 'lastname-error-message', 'Please enter your lastname');
        return false;
    } else if (containsNumbers(lastname.value.trim())) {
        errorMessageDisplay(lastname, 'lastname-error-message', 'lastname should contain letters only');
        return false;
    } else {
        errorMessageRemove(lastname, 'lastname-error-message')
        return true;
    }
}

function validateUsername() {
    let username = document.forms['register']['id_username'];
    if (isNaN(username.value.trim()) || username.value.trim().length !== 8) {
        errorMessageDisplay(username, 'username-error-message', 'Please enter a valid 8-digit employee ID');
        return false;
    } else {
        errorMessageRemove(username, 'username-error-message')
        return true;
    }
}

function validateEmail() {
    let email = document.forms['register']['id_email'];
    let username = document.forms['register']['id_username'];
    let emailID = email.value.trim().slice(0, 8)
    let emailDomain = 'udst.edu.qa'
    let emailDomainValue = email.value.trim().slice(9, 21)
    if (isNaN(emailID)) {
        errorMessageDisplay(email, 'email-error-message', 'Your email should start with your ID');
        return false;
    } else if (emailID !== username.value.trim()) {
        errorMessageDisplay(email, 'email-error-message', 'Your email ID should match your employee ID');
        return false;
    } else if (emailDomainValue !== emailDomain) {
        errorMessageDisplay(email, 'email-error-message', `Your email should end with \'@${emailDomain}\'`);
        return false;
    } else {
        errorMessageRemove(email, 'email-error-message')
        return true
    }
}

function validatePassword() {
    // Get the password input value
    let password1 = document.forms['register']['id_password1'];
    let password2 = document.forms['register']['id_password2'];
    // Check if the password length is greater than or equal to 8
    if (password1.value.length < 8) {
        // If the password length is less than 8, show an error message
        errorMessageDisplay(password1, 'password1-error-message', 'Password must be at least 8 characters long')
        errorMessageDisplay(password2, 'password2-error-message', '')
        return false;
    }

    // Check if the password contains at least one uppercase letter
    else if (!/[A-Z]/.test(password1.value)) {
        // If the password doesn't contain an uppercase letter, show an error message
        errorMessageDisplay(password1, 'password1-error-message', 'Password must contain at least one uppercase letter')
        errorMessageDisplay(password2, 'password2-error-message', '')
        return false;
    }

    // Check if the password contains at least one number
    else if (!/\d/.test(password1.value)) {
        // If the password doesn't contain a number, show an error message
        errorMessageDisplay(password1, 'password1-error-message', 'Password must contain at least one number');
        errorMessageDisplay(password2, 'password2-error-message', '')
        return false;
    }

    else if (password1.value !== password2.value) {
        errorMessageDisplay(password1, 'password1-error-message', "passwords doesn't match");
        errorMessageDisplay(password2, 'password2-error-message', '');
        return false;
    }

    else {
    // If the password is valid, clear the error message
    errorMessageRemove(password1, 'email-error-message')
    errorMessageRemove(password2, 'email-error-message')
    return true;
    }
}


function errorMessageDisplay(element, errorID, errorMessageContent) {
    element.style.border = '2px solid red';
    let errorMessage = document.getElementById(errorID);
    errorMessage.style.color = 'red';
    errorMessage.innerHTML = errorMessageContent;
}

function errorMessageRemove(element, errorID) {
    element.style.border = '1px solid #ccc';
    let errorMessage = document.getElementById(errorID);
    errorMessage.style.display = 'none';

}

function containsNumbers(str) {
    return /\d/.test(str);
}