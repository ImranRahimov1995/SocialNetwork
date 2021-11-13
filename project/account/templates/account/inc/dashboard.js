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
    $("#createPost").on('click', function(e){
        e.preventDefault();

        let text_data = $('#createPostBody').val()
        let profile_pk = {{profile.pk}}

        $.ajax({
            url: 'api/posts/create/',
            method: 'post',
            dataType: 'json',
            data: { body: text_data ,
                    profile: profile_pk,
                    active: true },
                    
            success: function(data){
                $('#createPostBody').val('')
                $('.posts').prepend(` \
                <div class="card"> \
                <div class="card-header"> \
                ${data['created']} ago \
                </div> \
                <div class="card-body" style=""> \
                  <p class="card-text"> ${data['body']}</p> \
                  {% comment %} <a href="#" class="btn btn-warning">Go somewhere</a> {% endcomment %} \
                </div> \
              </div> \
              `)
            }
        });
    });
});