function getRandomColor() {
    var letters = '0123456789ABCDEF';
    var color = '#';
    for (var i = 0; i < 6; i++) {
      color += letters[Math.floor(Math.random() * 16)];
    }
    return color;
  }

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
                .style('z-index', '10'); // Don't work
        }
    }

    const svg = d3.select("#svg");
    svg.on("mousemove", draw_point)
    document.querySelectorAll("circle").forEach(c => {
        c.style.animationPlayState = "running";
        c.addEventListener("animationend", function () {
            console.log("animationed")
            this.remove();
        });
    })
});

document.onmousedown = () => {
    document.querySelectorAll("circle").forEach(c => {
        c.style.animationPlayState = "running";
    })
};
