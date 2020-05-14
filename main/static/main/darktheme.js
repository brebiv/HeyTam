function makeItDark() {
    $("html").fadeOut("slow", function() {
        $("#theme_css").attr('href', STATIC_PATH+"darktheme.css");
        $("html").fadeIn("slow", function() {
            $("#logo").attr('src', STATIC_PATH+"logo_heytam_red.png");
            $("#welcome-text").html("Welcome to Dark HeyTam!");
            $("#change-theme").html("Light");
            $("#change-theme").data('theme', 'dark');
        });
    });
}

function makeItBright() {
    $("html").fadeOut("slow", function() {
        $("#theme_css").attr('href', '');
        $("html").fadeIn("slow", function() {
            $("#logo").attr('src', STATIC_PATH+"logo_heytam.png");
            $("#welcome-text").html("Welcome back!");
            $("#change-theme").html("Dark");
            $("#change-theme").data('theme', 'bright');
        });
    });
}

$(document).ready(function() {
    $("#change-theme").click(function() {
        let currentTheme = $(this).data('theme');
        if (currentTheme == 'bright') {
            makeItDark();
        } else {
            makeItBright();
        }
        return false;
    });
})
