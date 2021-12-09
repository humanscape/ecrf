if (!$) {
    // Need this line because Django also provided jQuery and namespaced as django.jQuery
    $ = django.jQuery;
}

$(function () {
    let age = '-';
    let birthday = '';
    let calculateList = $('input.vDateField[target]')
    for (let obj of calculateList){
        if (obj.getAttribute('target') == 'age') birthday = $(`input[name=${obj.getAttribute('name')}]`).val()
        $(`input[name=${obj.getAttribute('name')}]`).on("focus blur", function() {
            if (obj.getAttribute('target') == 'age') {
                age = calculateAge($(`input[name=${obj.getAttribute('name')}]`).val(), true);
                birthday = $(`input[name=${obj.getAttribute('name')}]`).val()
            }
            else {
                age = calculateAge($(`input[name=${obj.getAttribute('name')}]`).val(), false, birthday);
            }
            $(`.form-row.field-${obj.getAttribute('target')}`).find(".readonly").text(age);
        });
    }
})

function calculateAge(target_date, is_birth, birthday) {
    // date format regex
    const regex = RegExp(/^\d{4}-(0[1-9]|1[012])-(0[1-9]|[12][0-9]|3[01])$/);
    if (! regex.test(target_date)) return '-'

    let age = '-'
    const date = is_birth ? new Date(): new Date(target_date)
    const year = date.getFullYear();
    let month = (date.getMonth() + 1);
    let day = date.getDate();
    if (month < 10) month = '0' + month;
    if (day < 10) day = '0' + day;
    
    // calculate age
    if (is_birth){
        target_date = target_date.replace('-', '').replace('-', '');
        const calculated_dayy = target_date.substr(0, 4);
        age = year - calculated_dayy;
    } else {
        if(birthday != ''){
            birthday = birthday.replace('-', '').replace('-', '');
            const birthdayy = birthday.substr(0, 4);
            age = year - birthdayy;
        }
    }
    return age;
}
