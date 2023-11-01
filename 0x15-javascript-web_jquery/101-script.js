$(document).ready(function() {
    $("DIV#add_item").click(function() {
        var newItem = $("<li>Item</li>");
        $(".my_list").append(newItem);
    });

    $("DIV#remove_item").click(function() {
        var list = $(".my_list");
        list.children("li:last").remove();
    });

    $("DIV#clear_list").click(function() {
        var list = $(".my_list");
        list.empty();
    });
});