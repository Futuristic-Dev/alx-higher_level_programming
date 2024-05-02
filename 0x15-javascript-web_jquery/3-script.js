// Write a JavaScript script that adds the class red to the <header> element when the user clicks on the tag DIV#red_header:
document.querySelector('DIV#red_header').onclick = function () {
  document.querySelector('HEADER').classList.add('red');
};