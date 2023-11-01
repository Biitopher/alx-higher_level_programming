$.ajax({
    url: "https://hellosalut.stefanbohacek.dev/?lang=fr",
    dataType: "json",
    success: function(data) {
        var helloTranslation = data.hello;
       $("#hello").text(helloTranslation);
    },
    error: function() {
        $("#hello").text("Error fetching translation");
    }
});