let advertiserExists = 'This Advertiser title is already taken'

function categoryValidation() {
    let inputID = 'bt_category'
    let validationID = 'validation_category'
    let btnID = 'adsProfileNextBtn'
    checkRegexMinMaxValidations(inputID, validationID, btnID)
}

function titleValidation() {
    let inputID = 'bt_title'
    let validationID = 'validation_title'
    let btnID = 'adsProfileNextBtn'
    let regex = /^[a-zA-Z-_\s]+$/;
    let inputElement = document.getElementById(inputID);
    let _data = {
        bt_title: inputElement.value,
    }
    let url = window.location.origin + '/check_title';
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
                raiseValidationError('bt_title', 'validation_title', 'adsProfileNextBtn', advertiserExists);
            } else {
                checkRegexMinMaxValidations(inputID, validationID, btnID, regex, 3, 20);
            }
        })
        .catch(err => console.log(err));
}

function descriptionValidation2() {
    let inputID = 'bt_description'
    let validationID = 'validation_description2'
    let btnID = 'adsProfileNextBtn'
    let regex = /^[a-zA-Z\s]+$/;
    checkRegexMinMaxValidations(inputID, validationID, btnID, regex, 3, 200)
}

function adsNameValidation() {
    let inputID = 'name'
    let validationID = 'validation_ads_name'
    let btnID = 'adsProfileNextBtn'
    let regex = /^[a-zA-Z\s]+$/;
    checkRegexMinMaxValidations(inputID, validationID, btnID, regex, 3, 200)
}

function categoryValidation() {
    let inputID = 'bt_category'
    let validationID = 'validation_category'
    let btnID = 'adsProfileNextBtn'
    checkRegexMinMaxValidations(inputID, validationID, btnID)
}

function validateAdsProfileForm() {
    if (
        (document.getElementById("validation_category").innerHTML == "") &&
        (document.getElementById("validation_title").innerHTML == "") &&
        (document.getElementById("validation_description").innerHTML == "")
    ) {
        document.getElementById("adsProfileNextBtn").disabled = false;
        console.log("form is valid");
    } else {
        console.log("forms is in-valid");
        document.getElementById("adsProfileNextBtn").setAttribute('disabled', true);
    }
}