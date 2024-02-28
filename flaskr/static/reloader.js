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
            for (var j=0; j < data[key]['items'].length; j++) {
                var content = data[key]['items'][j][0];
                var link = data[key]['items'][j][1];
                $(buttons[i]).text(content);
                $(buttons[i]).attr('data-id', key);
                
                i++;
            }
        }
//      for (var i = 0; i < data.length; i++) {
//          var numbers = data[i][1]; // data[i] = [1, ["topic1", "topic2", "topic3", "topic5]"]
//          for (var j = 0; j < numbers.length; j++) {
//            if (i * numbers.length + j < buttons.length) { // add error
//              $(buttons[i * numbers.length + j]).text(numbers[j]);
//            }
//          }
//        }
      }
    });
  });
});