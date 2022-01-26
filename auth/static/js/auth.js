function printError(Id, Msg) {
    document.getElementById(Id).innerHTML = Msg;
}

function emailValidation() {
    var login = document.getElementById("login");
    var emailErr = true;
    if (login.value == "") {
        printError("emailErr", "This filed is required");
        var elemt = document.getElementById("login");
        elemt.classList.add("input-2");
        elemt.classList.remove("input-1");
        document.getElementById("btnSignUp").setAttribute('disabled', true);
    } else {

        var regex = /[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*@(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?/;
        if (regex.test(login.value) === false) {
            printError("emailErr", "Please enter a valid email address");
            var elemt = document.getElementById("login");
            elemt.classList.add("input-2");
            elemt.classList.remove("input-1");
            document.getElementById("btnSignUp").setAttribute('disabled', true);
        } else {
            printError("emailErr", "");
            emailErr = false;
            var elemt = document.getElementById("login");
            elemt.classList.add("input-1");
            elemt.classList.remove("input-2");
            this.validateFormAuth();
        }
    }
}


function firstNameValidation() {
    var name = document.getElementById("name");
    var nameErr = true;
    if (name.value == "") {
        printError("nameErr", "This filed is required");
        var elemt = document.getElementById("name");
        elemt.classList.add("input-2");
        elemt.classList.remove("input-1");
        document.getElementById("btnSignUp").setAttribute('disabled', true);
    } else {
        var regex = /^[a-zA-Z\s]+$/;
        var len = { min: 3, max: 40 };
        if (regex.test(name.value) === false) {
            printError("nameErr", "Please enter a valid name");
            var elemt = document.getElementById("name");
            elemt.classList.add("input-2");
            elemt.classList.remove("input-1");
            document.getElementById("btnSignUp").setAttribute('disabled', true);
        } else if (name.value.length < len.min) {
            printError("nameErr", "Minimum length of First Name is 3");
            var elemt = document.getElementById("name");
            elemt.classList.add("input-2");
            elemt.classList.remove("input-1");
            document.getElementById("btnSignUp").setAttribute('disabled', true);
        } else if (name.value.length > len.max) {
            printError("nameErr", "Maximum length of First Name is 40");
            var elemt = document.getElementById("name");
            elemt.classList.add("input-2");
            elemt.classList.remove("input-1");
            document.getElementById("btnSignUp").setAttribute('disabled', true);
        } else {
            printError("nameErr", "");
            nameErr = false;
            var elemt = document.getElementById("name");
            elemt.classList.add("input-1");
            elemt.classList.remove("input-2");
            this.validateFormAuth();
        }
    }
}

function lastNameValidation() {
    var last_name = document.getElementById("last_name");
    var lnameErr = true;
    if (last_name.value == "") {
        printError("lnameErr", "This filed is required");
        var elemt = document.getElementById("last_name");
        elemt.classList.add("input-2");
        elemt.classList.remove("input-1");
        document.getElementById("btnSignUp").setAttribute('disabled', true);
    } else {
        var regex = /^[a-zA-Z\s]+$/;
        var len = { min: 3, max: 40 };
        if (regex.test(last_name.value) === false) {
            printError("lnameErr", "Please enter a valid name");
            var elemt = document.getElementById("last_name");
            elemt.classList.add("input-2");
            elemt.classList.remove("input-1");
            document.getElementById("btnSignUp").setAttribute('disabled', true);
        } else if (last_name.value.length < len.min) {
            printError("lnameErr", "Minimum length of Last Name is 3");
            var elemt = document.getElementById("last_name");
            elemt.classList.add("input-2");
            elemt.classList.remove("input-1");
            document.getElementById("btnSignUp").setAttribute('disabled', true);
        } else if (last_name.value.length > len.max) {
            printError("lnameErr", "Maximum length of Last Name is 40");
            var elemt = document.getElementById("last_name");
            elemt.classList.add("input-2");
            elemt.classList.remove("input-1");
            document.getElementById("btnSignUp").setAttribute('disabled', true);
        } else {
            printError("lnameErr", "");
            lnameErr = false;
            var elemt = document.getElementById("last_name");
            elemt.classList.add("input-1");
            elemt.classList.remove("input-2");
            this.validateFormAuth();
        }
    }
}

function telephoneValidation() {
    var mobile = document.getElementById("contact_no");
    var mobileErr = true;
    if (mobile.value == "") {
        printError("mobileErr", "This filed is required");
        var elemt = document.getElementById("contact_no");
        elemt.classList.add("input-2");
        elemt.classList.remove("input-1");
        document.getElementById("btnSignUp").setAttribute('disabled', true);
    } else {
        var regex = /[0-9+]+$/;
        if (regex.test(mobile.value) === false) {
            printError("mobileErr", "Please enter a valid mobile number");
            var elemt = document.getElementById("contact_no");
            elemt.classList.add("input-2");
            elemt.classList.remove("input-1");
            document.getElementById("btnSignUp").setAttribute('disabled', true);
        } else {
            printError("mobileErr", "");
            mobileErr = false;
            var elemt = document.getElementById("contact_no");
            elemt.classList.add("input-1");
            elemt.classList.remove("input-2");
            this.validateFormAuth();
        }
    }
}

function passwordValidation() {
    var password = document.getElementById("password");
    var passwordErr = true;
    if (password.value == "") {
        printError("passwordErr", "This filed is required");
        var elemt = document.getElementById("password");
        elemt.classList.add("input-2");
        elemt.classList.remove("input-1");
        document.getElementById("btnSignUp").setAttribute('disabled', true);
    } else {
        var regex = /^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[#?!@$%^&*-]).{8,}$/;
        if (regex.test(password.value) === false) {
            printError("passwordErr", "At least one upper case English letter." + "<br/>\n" +
                "At least one lower case English letter." + "<br/>\n" +
                "At least one digit." + "<br/>\n" +
                "At least one special character." + "<br/>\n" +
                "Minimum eight in length." + "<br/>\n"
            );
            var elemt = document.getElementById("password");
            elemt.classList.add("input-2");
            elemt.classList.remove("input-1");
            document.getElementById("btnSignUp").setAttribute('disabled', true);
        } else {
            printError("passwordErr", "");
            passwordErr = false;
            var elemt = document.getElementById("password");
            elemt.classList.add("input-1");
            elemt.classList.remove("input-2");
            //this.validateForm();
        }
    }
}

function confirm_passwordValidation() {
    var password = document.getElementById("password");
    var confirm_password = document.getElementById("confirm_password");
    var confirm_passwordErr = true;

    if (confirm_password.value == "") {
        printError("confirm_passwordErr", "This filed is required");
        var elemt = document.getElementById("confirm_password");
        elemt.classList.add("input-2");
        elemt.classList.remove("input-1");
        document.getElementById("btnSignUp").setAttribute('disabled', true);
    } else {
        printError("confirm_passwordErr", "");
        confirm_passwordErr = false;
        var elemt = document.getElementById("confirm_password");
        elemt.classList.add("input-1");
        elemt.classList.remove("input-2");
        this.validateFormAuth();
    }

    //Solution for this error - Uncaught TypeError: Cannot set properties of null (setting 'innerHTML')

    if ((confirm_password.value != "") && (confirm_password.value != password.value)) {
        printError("confirm_passwordErr", "Password did not match");
        var elemt = document.getElementById("confirm_password");
        elemt.classList.add("input-2");
        elemt.classList.remove("input-1");
        document.getElementById("btnSignUp").setAttribute('disabled', true);
    } else if (confirm_password.value == "") {
        printError("confirm_passwordErr", "This filed is required");
        var elemt = document.getElementById("confirm_password");
        elemt.classList.add("input-2");
        elemt.classList.remove("input-1");
        document.getElementById("btnSignUp").setAttribute('disabled', true);
    } else {
        printError("confirm_passwordErr", "");
        confirm_passwordErr = false;
        var elemt = document.getElementById("confirm_password");
        elemt.classList.add("input-1");
        elemt.classList.remove("input-2");
        this.validateFormAuth();
    }

}


function validateFormAuth() {
    if (
        (document.getElementById("emailErr").innerHTML == "") &&
        (document.getElementById("nameErr").innerHTML == "") &&
        (document.getElementById("lnameErr").innerHTML == "") &&
        (document.getElementById("mobileErr").innerHTML == "") &&
        (document.getElementById("passwordErr").innerHTML == "") &&
        (document.getElementById("confirm_passwordErr").innerHTML == "")
    ) {
        document.getElementById("btnSignUp").disabled = false;
    } else {
        document.getElementById("btnSignUp").setAttribute('disabled', true);
    }
}