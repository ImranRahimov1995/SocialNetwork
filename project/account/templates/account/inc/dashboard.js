$('.main-container').addClass('ad');
$("#changeStatus").on('click', function(){
    $('#PublicStatus').css('display','block');
    $('#pbs').css('display','none');
} );
$("#cancelChangeStatus").on('click', function(){
    $('#PublicStatus').css('display','none');
    $('#pbs').css('display','block');
} );

$(document).ready(function(){

    $("#sendStatus").on('click', function(e){
        e.preventDefault();

        let text_data = $('#exampleFormControlTextarea1').val()
        let profile_pk = {{profile.pk}}

        $.ajax({
            url: `/api/profile/status/get/${profile_pk}/`,
            method: 'put',
            dataType: 'json',
            data: {status_text: text_data ,
                    owner: profile_pk},
            success: function(data){
                $('#PublicStatus').css('display','none');
                $('#pbs').css('display','block');
                $('#pbsText').text(text_data);

            }
        });
    });
});