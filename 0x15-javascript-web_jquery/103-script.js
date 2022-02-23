$('document').ready(function () {
  $('#btn_translate').click(lingua);
  $('#language_code').focus(function() {
    $(this).keydown(function(e) {
      if (e.keyCode === 13) {
        lingua();
      }
    })
  });
});

function lingua () {
  $.ajax({
    type: 'GET',
    url: 'https://fourtonfish.com/hellosalut/?mode=auto',
    success: function(data) {
      $('#language_code').val(data.code)
      $('#hello').html(data.hello);
    }
  });
}
