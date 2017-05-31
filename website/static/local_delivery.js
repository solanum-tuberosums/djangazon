$("#id_local_delivery").click((event)=>{
    $("#id_location").prop('disabled', function () {
    return ! $(this).prop('disabled')
   ;})
    $("#id_location").val('');
    if ($("#id_location").prop('disabled')) {
        $("#id_location").attr('placeholder', 'Select "Local delivery" to ' + 
            'input a city...')
    } else {
        $("#id_location").attr('placeholder', 'Please input a city...')
    }
});
