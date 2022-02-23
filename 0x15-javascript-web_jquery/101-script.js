$(document).ready(function() {
  $('#add_item').click(function() {
    $('.my_list').append('<li>Item</li>');
    });
  $('#clear_list').click(function() {
    $('.my_list').empty();
    });
  $('#remove_item').click(function(e) {
    $('.my_list li:last').remove();		  
    });
});
