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
        }
    };
    request.send();
}

document.addEventListener("DOMContentLoaded", ()=> {
    loadContent('index')
    document.querySelectorAll(".nav_button").forEach(btn => {
        btn.onclick = function() {
            let name = this.dataset.name;
            if (name == "products") {
                allowDrawing = false;
            } else if (name == "index" || name == "about") {
                allowDrawing = true;
            }
            loadContent(name);
            return false;
        }
    });
});