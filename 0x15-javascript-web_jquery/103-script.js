$(document).ready(function() {
    $("#language_code").on("keydown", function(e) {
        if (e.key === "Enter") {
            translateHello();
        }
    });

    $("#btn_translate").click(translateHello);

    function translateHello() {
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
    }
});