var data = [];
var topics = [];

rawData.forEach(function(d) {
    if(!topics[d[colorCat]]){
        topics[d[colorCat]] = [];
    }
    topics[d[colorCat]].push(d[labelCat]);
    if(!excludedLabels.includes(d[labelCat])){
        data.push(d);
    }
  });
  
delete rawData;

var xMax = d3.max(data, function(d) { return d[xCat]; }) * normalizedValue;
var xMin = d3.min(data, function(d) { return d[xCat]; }) * normalizedValue;
var yMax = d3.max(data, function(d) { return d[yCat]; }) * normalizedValue;
var yMin = d3.min(data, function(d) { return d[yCat]; }) * normalizedValue;

var color = d3.scaleOrdinal(d3.schemeCategory10);

// set the dimensions and margins of the graph
var margin = {top: 10, right: 30, bottom: 30, left: 60},
    width = givenWidth,
    height = givenHeight;

// append the SVG object to the body of the page
var SVG = d3.select("#plot")
  .append("svg")
    .attr("width", width + margin.left + margin.right)
    .attr("height", height + margin.top + margin.bottom)
  .append("g")
    .attr("transform",
          "translate(" + margin.left + "," + margin.top + ")");

// Add X axis
var x = d3.scaleLinear()
    .domain([xMin, xMax])
    .range([ 0, width ]);

var xAxis = SVG.append("g")
    .attr("transform", "translate(0," + height + ")")
    .call(d3.axisBottom(x));

// Add Y axis
var y = d3.scaleLinear()
    .domain([yMin, yMax])
    .range([ height, 0]);

var yAxis = SVG.append("g")
    .call(d3.axisLeft(y));

// Add a clipPath: everything out of this area won't be drawn.
var clip = SVG.append("defs").append("SVG:clipPath")
    .attr("id", "clip")
    .append("SVG:rect")
    .attr("width", width )
    .attr("height", height )
    .attr("x", 0)
    .attr("y", 0);

  // Create the scatter variable: where both the circles and the brush take place
var scatter = SVG.append('g')
    .attr("clip-path", "url(#clip)")

// Add circles
scatter
.selectAll("circle")
.data(data)
.enter()
.append("circle")
    .attr("cx", function (d) { 
        var xVal = d[xCat] * normalizedValue;
        return x(xVal); 
    })
    .attr("cy", function (d) { 
        var yVal = d[yCat] * normalizedValue;
        console.log('y:' + yVal);
        return y(yVal); 
    } )
    .attr("r", 3)
    .style("fill", function (d) { 
        return color(d[colorCat]); 
    })
    .style("opacity", 0.8)

scatter
    .selectAll("text")
    .data(data)
    .enter()
    .append("text")
    .text(function(d) {
        return d[labelCat];
    })
    .attr("x", function (d) { 
        var xVal = d[xCat] * normalizedValue;
        return x(xVal); 
      })
    .attr("y", function (d) { 
        var yVal = d[yCat] * normalizedValue;
        return y(yVal); 
      } )
    .attr("font_family", "sans-serif")  // Font type
    .attr("font-size", "10px")  // Font size
    .attr("fill", "black");   // Font color

  // Set the zoom and Pan features: how much you can zoom, on which part, and what to do when there is a zoom
  var zoom = d3.zoom()
      .scaleExtent([0.1, 20])  // This control how much you can unzoom (x0.5) and zoom (x20)
      .extent([[0, 0], [width, height]])
      .on("zoom", updateChart);

  // This add an invisible rect on top of the chart area. This rect can recover pointer events: necessary to understand when the user zoom
  SVG.append("rect")
      .attr("width", width)
      .attr("height", height)
      .style("fill", "none")
      .style("pointer-events", "all")
      .attr('transform', 'translate(' + margin.left + ',' + margin.top + ')')
      .call(zoom);
  // now the user can zoom and it will trigger the function called updateChart

// A function that updates the chart when the user zoom and thus new boundaries are available
function updateChart() {
    // recover the new scale
    var newX = d3.event.transform.rescaleX(x);
    var newY = d3.event.transform.rescaleY(y);

    // update axes with these new boundaries
    xAxis.call(d3.axisBottom(newX))
    yAxis.call(d3.axisLeft(newY))

    // update circle position
    scatter
        .selectAll("circle")
        .attr('cx', function(d) {
            var xVal = d[xCat] * normalizedValue;
            return newX(xVal)
            })
        .attr('cy', function(d) {
            var yVal = d[yCat] * normalizedValue;
            return newY(yVal)
        });

    scatter
        .selectAll("text")
        .attr('x', function(d) {
            var xVal = d[xCat] * normalizedValue;
            return newX(xVal)
            })
        .attr('y', function(d) {
            var yVal = d[yCat] * normalizedValue;
            return newY(yVal)
        });
}

// Add legends

var legend = d3.select('#legend')
            .append('svg')
                .attr('width', width)
                .attr('height', height);

legend.selectAll(".legend")
    .data(color.domain())
    .enter()
        .append("g")
        .classed("legend", true)
        .attr("transform", function(d, i) {
            return "translate(0," + (10 + i * 10) + ")"; 
        })
        .append("circle")
            .attr("r", 3)
            .attr("cx",  function(d, i) { 
                return width / 2;
            })
            .attr("fill", color);

legend.selectAll(".legend")
    .append("text")
    .attr("x",  function(d, i) { 
        return 10 + width / 2;
    })
    .attr("y",  function(d, i) { 
        return 5;
    })
    .text(function(d, i) {
        console.log(d);
        if (topics[d]){
            return "Topic " + (i+1) + ": " + topics[d].join(", ");
        }
        
        return i; 
    })
    .attr("font_family", "sans-serif")  // Font type
    .attr("font-size", "10px")  // Font size
    .attr("fill", "black");   // Font color


