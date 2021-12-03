var chat_id;
var recipient_name;


$(".my-chats").on('click', 'a.select-chat',function(e){
  let id = $(this).attr('data-id');
  let me = '{{request.user}}'
  chat_id = $(this).attr('data-id');

  $('.welcome-text').css("display",'none');
  $('.selected-chat').css("display",'flex');
  $(".darker").remove();
  $(".asd").remove();

    $.ajax({
      url: `/api/messages/chats/${id}/`,
      method: 'get',
      dataType: 'json',
      data: {

      },

      success: function(data){
         for (const item of data){

            if(me==item['author']){
              recipient_name = item['recipient']

              $('.chat-messages').prepend(` \
              <div class="asd darker"> \
                <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/a/ac/No_image_available.svg/1024px-No_image_available.svg.png" alt="Avatar" class="right" style="width:100%;"> \
                <p style="font-weight:bold;color:orange">${item['author']}</p> \
                <p>${item['body']}</p> \
                <span class="time-left">${item['created_at']}</span> \
              </div> \
              `)
            }else(
                 $('.chat-messages').prepend(` \
                  <div class="asd"> \
                    <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/a/ac/No_image_available.svg/1024px-No_image_available.svg.png" alt="Avatar" style="width:100%;"> \
                <p style="font-weight:bold;color:orange">${item['author']}</p> \
                    <p>${item['body']}</p> \
                    <span class="time-right">${item['created_at']}</span> \
                  </div> \
                 `)
            )
        }
      }
    });
});

$("#btn").on('click', function(e){
  let text_data = $('#floatingTextarea2').val()
  let author_id = {{request.user.pk}}



  console.log(recipient_name)

      $.ajax({
        url: '/api/messages/create/',
        method: 'post',
        dataType: 'json',
        data: {
                author: author_id,
                recipient: recipient_name,
                chat: chat_id,
                body: text_data,
                },
        success: function(data){
          $('#floatingTextarea2').val('')
           }
    });
});


