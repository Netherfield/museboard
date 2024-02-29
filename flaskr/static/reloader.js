$(document).ready(function() {
  $('.button').click(function() {
    var currentUrl = window.location.href;  // get current url
    $.ajax({
      url: 'http://127.0.0.1:5000/api/get_board',  // endpoint api for get data of boards
      type: 'GET',
      data: {
        'url': currentUrl  // we can send url with get request
      },
      success: function(data) {
        var buttons = $('.button');
        var texts = $('.text');
        var i = 0;
        for (var key in data) {
          $(texts[i]).text(data[key]['tag']);
          i++;
          for (var j=0; j < data[key]['items'].length; j++) {
            var content = data[key]['items'][j][0];
            var link = data[key]['items'][j][1];
            $('p', buttons[j + (i-1)*data[key]['items'].length]).text(content);
            $(buttons[j + (i-1)*data[key]['items'].length]).attr('data-id', key);
            $('img', buttons[j + (i-1)*data[key]['items'].length]).attr('src', link);
          }
        }
      }
    });
  });
});