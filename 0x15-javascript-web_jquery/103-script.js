// Write a JavaScript script that fetches and prints how to say “Hello” depending on the language
// When the user clicks on the tag DIV#hello
// You should use this API service: https://www.fourtonfish.com/hellosalut/hello/
// The language code will be the value entered in the tag INPUT#language_code (ex: es, fr, en, etc.)
// Your script must listen on a click event
// You can’t use document.querySelector to select the HTML tag
// You must use the jQuery API

$('DIV#hello').click( function () {
  $.get('https://www.fourtonfish.com/hellosalut/?lang=' + $('INPUT#language_code').val(), function (data) {
    $('DIV#hello').text(data.hello);
  });
});