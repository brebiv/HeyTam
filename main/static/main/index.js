function getRandomColor() {
    var letters = '0123456789ABCDEF';
    var color = '#';
    for (var i = 0; i < 6; i++) {
      color += letters[Math.floor(Math.random() * 16)];
    }
    return color;
  }


// Dots limit for drawing optimisation
let dotsLimit = 200;
let currentDots = 0;

document.addEventListener("DOMContentLoaded", ()=>{

    function draw_point() {
        if (allowDrawing) {
            const coords = d3.mouse(this);
            const randomColor = getRandomColor();
            svg.append("circle")
                .attr("cx", coords[0])
                .attr("cy", coords[1])
                .attr('r', 20)
                .style('fill', "black")
            currentDots++;

            if (currentDots > dotsLimit) {
                // No more then dots then limit allows.
                var first_dot = document.getElementById("svg").firstChild;  // Get oldest dot.
                document.getElementById("svg").removeChild(first_dot);      // Remove oldest dot.
                currentDots--;
            }
            // Remove dots when it's done animating.
            document.querySelectorAll("circle").forEach(c => {
                c.onanimationend = function() {
                    c.remove();
                    currentDots--;
                }
            });
        }
    }

    const svg = d3.select("#svg");
    document.addEventListener("mousedown", ()=> {
        // Draw while mouse is hold
        console.log(`Currently there is - ${currentDots} on the screen`)
        svg.on("mousemove", draw_point);
    });

    document.addEventListener("mouseup", ()=> {
        // Stop drawing when mouse released
        svg.on("mousemove", ()=>{}) // Callback anonymous function that does nothing. (stop drawing)
    });
});
