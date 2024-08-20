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

// forms can be filled out more than once
const forms_than_once = [
    forms[2],
    forms[3],
    forms[4],
    forms[5],
    forms[7],
    forms[9],
    forms[10],
    forms[11],
    forms[12],
    forms[13],
]


let current_form = 0
function next_form(){
    $(forms[current_form]).hide()
    if (current_form < 13){
        current_form += 1
    }
    $(forms[current_form]).show() 

    if(forms_than_once.includes(forms[current_form])){
        $('#btn-duplicate-form').show()
    }else{
        $('#btn-duplicate-form').hide()
    }
}
function previous_form(){
    $(forms[current_form]).hide()
    if (current_form > 0){
        current_form -= 1
    }
    $(forms[current_form]).show() 
    if(forms_than_once.includes(forms[current_form])){
        $('#btn-duplicate-form').show()
    }else{
        $('#btn-duplicate-form').hide()
    }
}