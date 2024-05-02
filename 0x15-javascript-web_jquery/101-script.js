// Write a JavaScript script that adds, removes and clears LI elements from a list when the user clicks:
// The new element must be: <li>Item</li>
// The new element must be added to UL.my_list


$(document).ready(function () {
  $('DIV#add_item').click(function () {
    $('UL.my_list').append('<li>Item</li>');
  });
  $('DIV#remove_item').click(function () {
    $('UL.my_list li').last().remove();
  });
  $('DIV#clear_list').click(function () {
    $('UL.my_list').empty();
  });
});