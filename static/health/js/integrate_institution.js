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



function duplicate_form(){
    form = document.querySelector(forms[current_form])
    const inputs = form.querySelectorAll('input')
    const selects = form.querySelectorAll('select')

    for (let i = 0; i < inputs.length; i++){
        if (inputs[i].type == 'file'){
            let new_input_file = document.createElement('input')

            // clone input's file 
            data_transfer = new DataTransfer()
            data_transfer.items.add(inputs[i].files[0])

            new_input_file.style.display = 'none'
            new_input_file.type = inputs[i].type
            new_input_file.name = inputs[i].name
            new_input_file.files = data_transfer.files
            
            form.appendChild(new_input_file)
        }else{
            let new_input = document.createElement('input')

            new_input.style.display = 'none'
            new_input.value = inputs[i].value
            new_input.type = inputs[i].type
            new_input.name = inputs[i].name
            
            form.appendChild(new_input)
        }
        
        inputs[i].value = ''
    }

    for (let i = 0; i < selects.length; i++){
        select = document.createElement('select')
        select.style.display = 'none'
        select.name = selects[i].name

        select.innerHTML = `
            <option value='${selects[i].value}' seletced></option>
        `
    }
    
}


