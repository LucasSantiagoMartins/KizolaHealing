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
const formsThanOnce = [
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

let operatingShiftsArray = []
let currentForm = 0


function nextForm(){
    $(forms[currentForm]).hide()
    if (currentForm < 13){
        currentForm += 1
    }
    $(forms[currentForm]).show() 

    if(formsThanOnce.includes(forms[currentForm])){
        $('#btn-duplicate-form').show()
    }else{
        $('#btn-duplicate-form').hide()
    }

    // 11 => div-form-operating-shifts and 1 is the next div-form
    if(currentForm == 11 + 1){
        let shiftTypeSelect = document.querySelector('#id_OperatingShiftForm_shift_type')
        let beginHourInput = document.querySelector('#id_OperatingShiftForm_begin_hour')
        let endHourInput = document.querySelector('#id_OperatingShiftForm_end_hour')
        
        if(shiftTypeSelect.value != '' && beginHourInput.value != '' && endHourInput.value != ''){
            operatingShiftsArray.push(shiftTypeSelect.value)
            let dutyShiftOperatingShiftSelect = document.querySelector('#id_DutyShiftForm_operating_shift')

            shiftTypeSelectOptions = shiftTypeSelect.options
            optionsText = {}
            for(let i = 0; i < shiftTypeSelectOptions.length; i++){
                optionsText[shiftTypeSelectOptions[i].value] = shiftTypeSelectOptions[i].innerHTML
            }
            for(let i = 0; i < operatingShiftsArray.length; i++){
                option = document.createElement('option')
                option.value = operatingShiftsArray[i]
                console.log(option.value)
                option.innerHTML = optionsText[operatingShiftsArray[i]]
                dutyShiftOperatingShiftSelect.appendChild(option) 
            }
           
        }
    }
}
function previousForm(){
    $(forms[currentForm]).hide()
    if (currentForm > 0){
        currentForm -= 1
    }
    $(forms[currentForm]).show() 
    if(formsThanOnce.includes(forms[currentForm])){
        $('#btn-duplicate-form').show()
    }else{
        $('#btn-duplicate-form').hide()
    }
}



function duplicateForm(){
    formId = forms[currentForm]
    form = document.querySelector(formId)

    if(validateForm(form)){
        const inputs = form.querySelectorAll('input')
        const selects = form.querySelectorAll('select')

        for (let i = 0; i < inputs.length; i++){
            if (inputs[i].type == 'file'){
                let newInputFile = document.createElement('input')

                // clone input's file 
                dataTransfer = new DataTransfer()
                dataTransfer.items.add(inputs[i].files[0])

                newInputFile.style.display = 'none'
                newInputFile.type = inputs[i].type
                newInputFile.name = inputs[i].name
                newInputFile.files = dataTransfer.files
                
                form.appendChild(newInputFile)
            }else{
                let newInput = document.createElement('input')

                newInput.style.display = 'none'
                newInput.value = inputs[i].value
                newInput.type = inputs[i].type
                newInput.name = inputs[i].name
                form.appendChild(newInput)
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
            if(selects[i].name == 'shift_type'){
                operatingShiftsArray.push(selects[i].value)
            }
            selects[i].value = ''
        }
    }
}

function renewalDateInputDisabler(renewalCheckbox, renewalDateInput){
    if(renewalCheckbox.checked == false){
        renewalDateInput.classList.remove('is-invalid')
        renewalDateInput.classList.remove('is-valid')
        renewalDateInput.value = ''
        renewalDateInput.disabled = true
    }else{
        renewalDateInput.disabled = false
    }
}

renewalCheckboxCertification = document.querySelector('#id_CertificationForm_renewal_required')
renewalCheckBoxLicense = document.querySelector('#id_LicenseForm_renewal_required')

renewalCheckboxCertification.addEventListener('change', ()=>{
    let renewalDateInput = document.querySelector('#id_CertificationForm_renewal_date')
    renewalDateInputDisabler(renewalCheckboxCertification, renewalDateInput)
})
renewalCheckBoxLicense.addEventListener('change', ()=>{
    let renewalDateInput = document.querySelector('#id_LicenseForm_renewal_date')
    renewalDateInputDisabler(renewalCheckBoxLicense, renewalDateInput)
})

function validateForm(form){
    const inputs = form.querySelectorAll('input')
    const selects = form.querySelectorAll('select')
    let invalidFields = []

    if(form.id == 'div-form-certification'){
        renewalRequiredChecked = document.querySelector('#id_CertificationForm_renewal_required').checked
    }else if(form.id == 'div-form-license'){
        renewalRequiredChecked = document.querySelector('#id_LicenseForm_renewal_required').checked
    }

    inputs.forEach((input)=>{
        if(input.type == 'file'){
            if(!input.files[0]){
                input.classList.add('is-invalid')
                invalidFields.push(input)
            }else{
                input.classList.remove('is-invalid')
                input.classList.add('is-valid')
            }
        }else{
            if(!input.value){
                if(input.name == 'renewal_date'){
                    if(renewalRequiredChecked){
                        input.classList.add('is-invalid')
                        invalidFields.push(input)
                    }else{
                        input.classList.remove('is-invalid')
                    }
                }else{
                    input.classList.add('is-invalid')
                    invalidFields.push(input)
                }
                
                
            }else{
                input.classList.remove('is-invalid')
                input.classList.add('is-valid')
            }
        }
    })

    selects.forEach((select)=>{
        if(select.type == 'file'){
            if(!select.files[0]){
                select.classList.add('is-invalid')
                invalidFields.push(select)
            }else{
                select.classList.remove('is-invalid')
                select.classList.add('is-valid')
            }
        }else{
            if(!select.value){
                select.classList.add('is-invalid')
                invalidFields.push(select)
            }else{
                select.classList.remove('is-invalid')
                select.classList.add('is-valid')
            }
        }
    })

    if(invalidFields.length == 0){
        inputs.forEach((input)=>{
            input.classList.remove('is-valid')
        })
        selects.forEach((select)=>{
            select.classList.remove('is-valid')
        })
        return true
    }else{
        return false
    }

}