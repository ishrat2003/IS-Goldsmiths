// First undefine 'circles' so we can easily reload this file.
require.undef('circles');

define('circles', ['d3'], function (d3) {

    function draw(container, data, width, height) {
        var normalizedValue = 1000;
        var margin = { 
            top: 50, 
            right: 350, 
            bottom: 50, 
            left: 50
        };
        var outerWidth = width || 600
        var outerHeight = height || 200
        var width = outerWidth - margin.left - margin.right;
        var height = outerHeight - margin.top - margin.bottom;
        var xCat = "x";
        var yCat = "y";

        var xMax = d3.max(data, function(d) { return d[xCat]; }) * normalizedValue;
        var xMin = d3.min(data, function(d) { return d[xCat]; }) * normalizedValue;
        var yMax = d3.max(data, function(d) { return d[yCat]; }) * normalizedValue;
        var yMin = d3.min(data, function(d) { return d[yCat]; }) * normalizedValue;

        var x = d3.scaleLinear()
            .domain([xMin, xMax])
            .range([0, width]);

        var y = d3.scaleLinear()
            .domain([yMin, yMax])
            .range([0, height]);

        var svg = d3.select(container)
            .append("svg")
            .attr("width",  width)
            .attr("height",  height)
            .call(d3.zoom().on("zoom", function () {
                svg.attr("transform", d3.event.transform)
            }))
            .append("g");


        var circles = svg.selectAll('circle').data(data);

        circles.enter()
            .append("circle")
            .attr("cx", function (d, i) {
                return x(d['x']);
            })
            .attr("cy", function (d, i) {
                return y(d['y']);
            })
            .attr("r", function (d) {
                return 50;
            })
            .style("fill", "#1f77b4")
            .style("opacity", 0.7)
            .attr("cx", 300)
            .attr("cy", 300)
            .attr("r", 40)
            .style("fill", "#68b2a1");
    }

    return draw;
});

element.append('test1.js');