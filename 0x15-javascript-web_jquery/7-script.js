$.ajax({
    url: "https://swapi-api.alx-tools.com/api/people/5/?format=json",
    dataType: "json",
    success: function(data) {
        var characterName = data.name;
        $("#character").text(characterName);
    },
    error: function() {
        $("#character").text("Error fetching character name");
    }
});