$("#id_local_delivery").click((event)=>{
    $("#id_location").prop('disabled', function () {
    return ! $(this).prop('disabled')
   ;})
    $("#id_location").val('')
});
