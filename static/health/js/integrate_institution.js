const forms = {
    1: '#div-form-institutional-information',
    2: '#div-form-administrative-information',
    3: '#div-form-certification',
    4: '#div-form-certification-document',
    5: '#div-form-license',
    6: '#div-form-license-document',
    7: '#div-form-address',
    8: '#div-form-phone',
    9: '#div-form-contact-information',
    10: '#div-form-services-offered',
    11: '#div-form-operating-hour',
    12: '#div-form-operating-shifts',
    13: '#div-form-duty-shifts',
    14: '#div-form-policy-information',
}


let current_form = 1
function next_form(){
    $(forms[current_form]).hide()
    if (current_form < 14){
        current_form += 1
    }
    $(forms[current_form]).show() 
}
function previous_form(){
    $(forms[current_form]).hide()
    if (current_form > 1){
        current_form -= 1
    }
    $(forms[current_form]).show() 
}