$.ajax({
  type: 'GET',
  url: 'https://swapi-api.hbtn.io/api/films/?format=json',
  success: function(data) {
    $results = data.results
    $.each($results, function(i, movie) {
      $('#list_movies').append('<li>'+ movie.title +'</li>')
    });
  }
});
