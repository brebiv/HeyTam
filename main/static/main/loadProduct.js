// Using jquery


function loadData(id) {
    // Same function as in singlepage.js, but using jquery.
    // It's kinda bad to have two functions like that, but for let it be.
    var response = ''
    $.ajax({
        type: "GET",
        url: id,
        async: true,
        success: function(text) {
            response = text;
        }
    }).done(function() {
        $("#main").html(response)
    });
}

class Products {
    constructor () {
        // Add click listeners to buttons in cards.
        $(".product-link").on('click', function() {
            var id = this.dataset.id;
            $("#main").fadeOut("slow", function() {
                loadData(id);
                $("#main").fadeIn("slow");
            });
            return false;
        });
    }
}
