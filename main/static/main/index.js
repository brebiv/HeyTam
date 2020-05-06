document.addEventListener("DOMContentLoaded", ()=>{
    const svg = d3.select("#svg");
    svg.on("mousemove", draw_point);
    function draw_point() {
        const coords = d3.mouse(this);

        svg.append("circle")
            .attr("cx", coords[0])
            .attr("cy", coords[1])
            .attr('r', 5)
            .style('fill', 'black');        
    }
});

document.onmousedown = () => {
    document.querySelectorAll("circle").forEach(c => {
        c.style.animationPlayState = "running";
        console.log("here")
    })
};
