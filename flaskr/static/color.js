$(document).ready(function() {
  $('.button').click(function() {
    var currentColor = this.style.borderColor;  // get current color
    $.ajax({
      url: 'http://127.0.0.1:5000/api/get_color',  // endpoint api for get data of boards
      type: 'GET',
      data: {
        'color': currentColor  // we can send url with get request
      },
      success: function(data) {
        var buttons = $('.button');
        for (var i = 0; i < buttons.length; i++) {
          $(buttons[i]).css('border-color', data);  // change border color based on data from API
        }
      }
    });
  });
});