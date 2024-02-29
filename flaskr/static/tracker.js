document.addEventListener('DOMContentLoaded', function() {
  var buttons = document.querySelectorAll('.button');
  var path = '';

  buttons.forEach(function(button) {
    button.addEventListener('click', function(e) {
      e.preventDefault();

      // get ID from button
      var buttonId = this.getAttribute('data-id');
      var divTag = this.parentElement.previousElementSibling;
      console.log(divTag);
      var buttonTag = divTag.innerHTML;
      console.log(buttonTag);
      // get Text from button
      var buttonText = encodeURIComponent(this.textContent || this.innerText);

      // add to path
      path += '/' + buttonTag;

      // reloading url in local (NO reload page)
      history.pushState(null, '', window.location.origin + window.location.pathname + '?item=' + buttonText + '&id=' + buttonId + '&path=' + path);
    });
  });
});

