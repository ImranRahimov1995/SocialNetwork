$('.main-container').addClass('ad');
$("#changeStatus").on('click', function(){
    $('#PublicStatus').css('display','block');
    $('#pbs').css('display','none');
} );
$("#cancelChangeStatus").on('click', function(){
    $('#PublicStatus').css('display','none');
    $('#pbs').css('display','block');
} );


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
            <div class="card" data-id="${data['id']}"> \
            <div class="card-header"> \
            ${data['created']} ago \
            <button type="button" class="btn-close float-end" id="closeButton"  aria-label="Close"></button>\

            </div> \
            <div class="card-body" style=""> \
                <p class="card-text"> ${data['body']}</p> \
            </div> \
            </div> \
            `)
        }
    });
});

$(".posts").on('click', 'button.btn-close',function(e){
    e.preventDefault();
    let post_class = $(this).parent().parent();


    $.ajax({
        url: `api/posts/get/${post_class.attr('data-id')}`,
        method: 'delete',
        dataType: 'json',
        data: { },
                
        success: function(data){
            post_class.remove()
        }
    });
});
