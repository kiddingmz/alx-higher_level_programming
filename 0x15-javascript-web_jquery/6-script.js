$('DIV#update_header').click(function (e) {
  e.preventDefault();
  $('UL.my_list').append('<li>Item</li>');
  $('header').text('New Header!!!');
});
