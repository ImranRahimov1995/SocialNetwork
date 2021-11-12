// $("#loginPage").on('click', function(){
//     $('.loginBlock').css('display','block');
//     $('.signUpBlock').css('display','none');
// } );

// $("#signPage").on('click', function(){
//     $('.signUpBlock').css('display','block');
//     $('.signUpBlock').css('margin-left','7%');
//     $('.loginBlock').css('display','none');
// } );

var csrftoken = Cookies.get('csrftoken');
    function csrfSafeMethod(method) {
      // these HTTP methods do not require CSRF protection
      return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
    }
    $.ajaxSetup({
      beforeSend: function(xhr, settings) {
        if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
          xhr.setRequestHeader("X-CSRFToken", csrftoken);
        }
      }
    });

