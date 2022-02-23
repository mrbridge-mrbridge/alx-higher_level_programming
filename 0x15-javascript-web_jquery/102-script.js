$('document').ready(function () {
  $('#btn_translate').click(function () {
    $.ajax({
      type: 'GET',
      url: 'https://fourtonfish.com/hellosalut/?mode=auto',
      success: function(data) {
        $('#language_code').val(data.code)
	$('#hello').html(data.hello);
      }
    });
  });
});
