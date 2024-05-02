// Write a JavaScript script that updates the text color of the HTML tag HEADER to red (#FF0000):
// when the user clicks on the tag DIV#red_header
document.querySelector('DIV#red_header').onclick = function () {
  document.querySelector('HEADER').style.color = '#FF0000';
};
