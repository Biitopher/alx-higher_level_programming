$(document).ready(function() {
    $("#btn_translate").click(function() {
        var languageCode = $("#language_code").val();

        $.ajax({
            url: 'https://www.fourtonfish.com/hellosalut/hello/',
            data: { lang: languageCode },
            dataType: 'json',
            success: function(data) {
                $("#hello").text(data.hello);
            },
            error: function() {
                $("#hello").text("Translation not found");
            }
        });
    });
});