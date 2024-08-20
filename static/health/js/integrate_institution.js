const forms = [
    '#div-form-institutional-information',
    '#div-form-administrative-information',
    '#div-form-certification',
    '#div-form-certification-document',
    '#div-form-license',
    '#div-form-license-document',
    '#div-form-address',
    '#div-form-phone',
    '#div-form-contact-information',
    '#div-form-services-offered',
    '#div-form-operating-hour',
    '#div-form-operating-shifts',
    '#div-form-duty-shifts',
    '#div-form-policy-information',
]


let current_form = 0
function next_form(){
    $(forms[current_form]).hide()
    if (current_form < 13){
        current_form += 1
    }
    $(forms[current_form]).show() 
}
function previous_form(){
    $(forms[current_form]).hide()
    if (current_form > 0){
        current_form -= 1
    }
    $(forms[current_form]).show() 
}