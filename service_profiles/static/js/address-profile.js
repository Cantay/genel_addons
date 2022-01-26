
function addressStreetValidation() {
    let inputID = 'street'
    let validationID = 'validation_street'
    let btnID = 'addressNextBtn'
    let regex = /^[a-zA-Z0-9-_\\//s]+$/;
    checkRegexMinMaxValidations(inputID, validationID, btnID, regex, 2, 12, validateAddressForm);
}

function addressStreet2Validation() {
    let inputID = 'street2'
    let validationID = 'validation_street2'
    let btnID = 'addressNextBtn'
    let regex = /^[a-zA-Z0-9-_\\//s]+$/;
    checkRegexMinMaxValidations(inputID, validationID, btnID, regex, 2, 12, validateAddressForm);
}

function addressCityValidation() {
    let inputID = 'city'
    let validationID = 'validation_city'
    let btnID = 'addressNextBtn'
    let regex = /^[a-zA-Z\s]+$/;
    checkRegexMinMaxValidations(inputID, validationID, btnID, regex, 3, 20, validateAddressForm);
}

function addressZipValidation() {
    let inputID = 'zip'
    let validationID = 'validation_zip'
    let btnID = 'addressNextBtn'
    let regex = /^[a-zA-Z0-9-_\s]+$/;
    checkRegexMinMaxValidations(inputID, validationID, btnID, regex, 3, 12, validateAddressForm);
}
function addressPhoneValidation() {
    let inputID = 'phone'
    let validationID = 'validation_phone'
    let btnID = 'addressNextBtn'
    let regex = /[0-9+]+$/;
    checkRegexMinMaxValidations(inputID, validationID, btnID, regex, 3, 12, validateAddressForm);
}

function addressMobileValidation() {
    let inputID = 'mobile'
    let validationID = 'validation_mobile'
    let btnID = 'addressNextBtn'
    let regex = /[0-9+]+$/;
    checkRegexMinMaxValidations(inputID, validationID, btnID, regex, 3, 12, validateAddressForm);
}

function addressEmailValidation() {
    let inputID = 'email'
    let validationID = 'validation_email'
    let btnID = 'addressNextBtn'
    let regex = /[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*@(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?/
    checkRegexMinMaxValidations(inputID, validationID, btnID, regex, 3, 50);
}

function validateAddressForm() {
    if (
        (document.getElementById("validation_street").innerHTML == "") &&
        (document.getElementById("validation_street2").innerHTML == "") &&
        (document.getElementById("validation_city").innerHTML == "") &&
        (document.getElementById("validation_zip").innerHTML == "") &&
        (document.getElementById("validation_phone").innerHTML == "") &&
        (document.getElementById("validation_mobile").innerHTML == "") &&
        (document.getElementById("validation_email").innerHTML == "")
    ) {
        document.getElementById("addressNextBtn").disabled = false;
        console.log("form is valid");
    } else {
        console.log("forms is in-valid");
        document.getElementById("addressNextBtn").setAttribute('disabled', true);
    }
}