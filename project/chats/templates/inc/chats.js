var chat_id;
var recipient_name;
var messagesSocket;


//On select chat
$(".my-chats").on('click', 'a.select-chat',function(e){
  //  check socket if opened we need to close
  if (messagesSocket!=null){
    messagesSocket.close()
  };

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
        messagesSocket = new WebSocket(
        'ws://'
        + window.location.host
        + '/chat/'
        + chat_id
        + '/'
      );
        messagesSocket.onmessage = function(e) {
        const data = JSON.parse(e.data)

        let author_mes = data['message']['author'];
        console.log(data['message'])
        if(author_mes==me){
          $('.chat-messages').append(` \
              <div class="asd darker"> \
                <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/a/ac/No_image_available.svg/1024px-No_image_available.svg.png" alt="Avatar" class="right" style="width:100%;"> \
                <p style="font-weight:bold;color:orange">${data['message']['author']}</p> \
                <p>${data['message']['body']}</p> \
                <span class="time-left">${data['message']['created_at']}</span> \
              </div> \
              `)
        }else{
           $('.chat-messages').append(` \
                  <div class="asd"> \
                    <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/a/ac/No_image_available.svg/1024px-No_image_available.svg.png" alt="Avatar" style="width:100%;"> \
                <p style="font-weight:bold;color:orange">${data['message']['author']}</p> \
                    <p>${data['message']['body']}</p> \
                    <span class="time-right">${data['message']['created_at']}</span> \
                  </div> \
                 `)
        }

        };
      }
    });
});

$("#btn").on('click', function(e){
  let text_data = $('#floatingTextarea2').val()
  let author_id = {{request.user.pk}}

  e.preventDefault()
  messagesSocket.send(JSON.stringify({
                'text':text_data
        }));
 $('#floatingTextarea2').val('')



//      $.ajax({
//        url: '/api/messages/create/',
//        method: 'post',
//        dataType: 'json',
//        data: {
//                author: author_id,
//                recipient: recipient_name,
//                chat: chat_id,
//                body: text_data,
//                },
//        success: function(data){
//          $('#floatingTextarea2').val('')
//           }
//    });
});

