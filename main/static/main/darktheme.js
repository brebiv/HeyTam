function makeItDark() {
    $("html").fadeOut("slow", function() {
        $("#theme_css").attr('href', STATIC_PATH+"darktheme.css");
        $("html").fadeIn("slow", function() {
            $("#logo").attr('src', STATIC_PATH+"logo_heytam_red.png");
            $("#welcome-text").html("Welcome to Dark HeyTam!")
        });
    });
}


$(document).ready(function() {
    $("#change-theme").click(function() {
        makeItDark();
        return false;
    });
})
