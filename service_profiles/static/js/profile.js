let commonMsg = 'This field is required'
let serviceExists = 'This business slug is already taken'
let invalidCharacters = 'Invalid Characters'
let minimumField = "Minimum length of this field is "
let maximumField = "Maximum length of this field is "


function raiseValidationError(inputID, validationID, btnID, msg) {
    var elem = document.getElementById(inputID);
    elem.classList.add("invalid-input-field");
    elem.classList.remove("valid-input-field");
    document.getElementById(validationID).innerHTML = msg;
    document.getElementById(btnID).setAttribute('disabled', true);
}

function clearValidationError(inputID, validationID, btnID, formFunc) {
    var elem = document.getElementById(inputID);
    elem.classList.add("valid-input-field");
    elem.classList.remove("invalid-input-field");
    document.getElementById(validationID).innerHTML = "";
    document.getElementById(btnID).removeAttribute('disabled');
    if (formFunc === undefined) {

    } else {
        formFunc();
    }
}

function checkRegexMinMaxValidations(inputID, validationID, btnID, regex, min, max, validateForm) {
    let inputElement = document.getElementById(inputID);
    if (inputElement.value == "") {
        raiseValidationError(inputID, validationID, btnID, commonMsg);
    } else {
        if (regex.test(inputElement.value) === false) {
            raiseValidationError(inputID, validationID, btnID, invalidCharacters);
        } else if (inputElement.value.length < min) {
            raiseValidationError(inputID, validationID, btnID, minimumField + `${min}`);
        } else if (inputElement.value.length > max) {
            raiseValidationError(inputID, validationID, btnID, maximumField + `${max}`);
        } else {
            clearValidationError(inputID, validationID, btnID, validateForm)
        }
    }
}

function businessNameValidation() {
    let inputID = 'name'
    let validationID = 'validation_name'
    let btnID = 'profileNextBtn'
    let regex = /^[a-zA-Z\s]+$/;
    checkRegexMinMaxValidations(inputID, validationID, btnID, regex, 3, 20, validateForm)
}

function businessSlugValidation() {
    let inputID = 'business_slug'
    let validationID = 'validation_slug'
    let btnID = 'profileNextBtn'
    let regex = /^[a-zA-Z-_\s]+$/;
    let inputElement = document.getElementById(inputID);
    let _data = {
        business_slug: inputElement.value,
    }
    let url = window.location.origin + '/check_business_slug';
    fetch(url, {
            method: "POST",
            body: JSON.stringify(_data),
            headers: {
                "Content-type": "application/json; charset=UTF-8"
            }
        })
        .then(response => response.json())
        .then(json => {
            console.log(json);
            console.log(json.result.data);
            if (json.result.data.exists) {
                raiseValidationError('business_slug', 'validation_slug', 'profileNextBtn', serviceExists);
            } else {
                checkRegexMinMaxValidations(inputID, validationID, btnID, regex, 3, 20, validateForm);
            }
        })
        .catch(err => console.log(err));
}

function descriptionValidation() {
    let inputID = 'description'
    let validationID = 'validation_description'
    let btnID = 'profileNextBtn'
    let regex = /^[a-zA-Z\s]+$/;
    checkRegexMinMaxValidations(inputID, validationID, btnID, regex, 3, 200, validateForm)
}

function validateForm() {
    if (
        (document.getElementById("validation_name").innerHTML == "") &&
        (document.getElementById("validation_slug").innerHTML == "") &&
        (document.getElementById("validation_description").innerHTML == "")
    ) {
        document.getElementById("profileNextBtn").disabled = false;
        console.log("form is valid");
    } else {
        console.log("forms is in-valid");
        document.getElementById("profileNextBtn").setAttribute('disabled', true);
    }
}

$('.input-images-1').imageUploader();