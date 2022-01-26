function addressStreetValidationAds() {
    let inputID = 'street_ads'
    let validationID = 'validation_street_ads'
    let btnID = 'adsProfileBtn'
    let regex = /^[a-zA-Z0-9-_\s]+$/;
    checkRegexMinMaxValidations(inputID, validationID, btnID, regex, 2, 12);
}

function addressStreet2ValidationAds() {
    let inputID = 'street2_ads'
    let validationID = 'validation_street2_ads'
    let btnID = 'adsProfileBtn'
    let regex = /^[a-zA-Z0-9-_\s]+$/;
    checkRegexMinMaxValidations(inputID, validationID, btnID, regex, 2, 12);
}

function addressCityValidationAds() {
    let inputID = 'city_ads'
    let validationID = 'validation_city_ads'
    let btnID = 'adsProfileBtn'
    let regex = /^[a-zA-Z\s]+$/;
    checkRegexMinMaxValidations(inputID, validationID, btnID, regex, 3, 20);
}

function addressZipValidationAds() {
    let inputID = 'code_ads'
    let validationID = 'validation_zip_ads'
    let btnID = 'adsProfileBtn'
    let regex = /^[a-zA-Z0-9-_\s]+$/;
    checkRegexMinMaxValidations(inputID, validationID, btnID, regex, 3, 12);
}

function addressPhoneValidationAds() {
    let inputID = 'phone_ads'
    let validationID = 'validation_tp1_ads'
    let btnID = 'adsProfileBtn'
    let regex = /[0-9+]+$/;
    checkRegexMinMaxValidations(inputID, validationID, btnID, regex, 3, 12);
}

function addressMobileValidationAds() {
    let inputID = 'mobile_ads'
    let validationID = 'validation_tp2_ads'
    let btnID = 'adsProfileBtn'
    let regex = /[0-9+]+$/;
    checkRegexMinMaxValidations(inputID, validationID, btnID, regex, 3, 12);
}

function addressEmailValidationAds() {
    let inputID = 'email_ads'
    let validationID = 'validation_email_ads'
    let btnID = 'adsProfileBtn'
    let regex = /[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*@(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?/
    checkRegexMinMaxValidations(inputID, validationID, btnID, regex, 3, 50);
}


function validateAddressFormAds() {
    if (
        (document.getElementById("validation_tp1_ads").innerHTML == "") &&
        (document.getElementById("validation_tp2_ads").innerHTML == "") &&
        (document.getElementById("validation_email_ads").innerHTML == "") &&
        (document.getElementById("validation_no_ads").innerHTML == "") &&
        (document.getElementById("validation_address1_ads").innerHTML == "") &&
        (document.getElementById("validation_address2_ads").innerHTML == "") &&
        (document.getElementById("validation_zip_ads").innerHTML == "")
    ) {
        document.getElementById("adsProfileBtn").disabled = false;
        console.log("form is valid");
    } else {
        console.log("forms is in-valid");
        document.getElementById("adsProfileBtn").setAttribute('disabled', true);
    }
}