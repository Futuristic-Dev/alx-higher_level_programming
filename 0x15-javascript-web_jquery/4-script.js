// Write a JavaScript script that toggles the class of the <header> element when the user clicks on the tag DIV#toggle_header
document.querySelector('DIV#toggle_header').onclick = function () {
  document.querySelector('HEADER').classList.toggle('red');
};