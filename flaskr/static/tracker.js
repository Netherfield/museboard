var buttons = document.querySelectorAll('.button');
var path = '';

buttons.forEach(function(button) {
  button.addEventListener('click', function(e) {
    e.preventDefault();

    // get Text from button
    var buttonContent = encodeURIComponent(this.textContent || this.innerText);

    // add to path
    path += '/' + buttonContent;

    // reloading url in local (NO reload page)
    history.pushState(null, '', window.location.origin + window.location.pathname + '?tag=' + buttonContent + '&path=' + path);
  });
});

