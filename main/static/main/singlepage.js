var allowDrawing = true;
var titleBase = "HeyTam - "

function capitalize(string) {
    return string.charAt(0).toUpperCase() + string.slice(1);
}

function loadContent(name) {
    let request = new XMLHttpRequest();
    request.open("GET", name);
    request.onreadystatechange = function () {
        if (this.readyState == 4 && this.status == 200) {
            document.getElementById("main").innerHTML = request.responseText;
            document.title = titleBase + capitalize(name);
            if (name == "products") {
                new Products();
            }
        }
    };
    request.send();
}

document.addEventListener("DOMContentLoaded", ()=> {
    document.querySelector("body").style.opacity = 0;
    $("body").animate({opacity: 1}, 1200)
    var main = document.getElementById("main");
    loadContent('index')
    document.querySelectorAll(".spa").forEach(btn => {
        btn.onclick = function() {
            let name = this.dataset.name;
            if (name == "products" || name == "news") {
                allowDrawing = false;
            } else if (name == "index" || name == "about") {
                allowDrawing = true;
            }
            $("#main").fadeOut("slow", function() {
                loadContent(name);
                $("#main").fadeIn("slow");
            });
            return false;
        }
    });
});