$.ajax({
  url: "https://swapi-api.alx-tools.com/api/films/?format=json",
  dataType: "json",
  success: function(data) {
      var movies = data.results;
      var $listMovies = $("#list_movies");
      $.each(movies, function(index, movie) {
          $listMovies.append("<li>" + movie.title + "</li>");
      });
  },
  error: function() {
      $("#list_movies").append("<li>Error fetching movie titles</li>");
  }
});