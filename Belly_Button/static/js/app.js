console.log("app.js accessed")

var url = "/names"
var selected_sample = "BB_940"
Plotly.d3.json(url, function(error, response) {
    console.log("in dropdown function")
    console.log(response)
    var select = Plotly.d3.select('.col-md-3')
      .append('select')
        .attr('id','selDataset')
        .on('change',optionChanged)

    Plotly.d3.select("#selDataset")
        .selectAll('option')
        .data(response)
        .enter()
        .append('option')
        .text(function (d) { return d; });

    function optionChanged() {
        selectValue = Plotly.d3.select('select').property('value')
        selected_sample = selectValue
        console.log(selected_sample)
        newPie()
    };    
})

//var url_metadata = "/metadata/<sample>"
//Plotly.d3.json(url, )


var url_pie = `/samples/${selected_sample}`
newPie()
function newPie(){
    Plotly.d3.json(url_pie, function(error, response1){
        var url_otu = ""
        console.log("in piechart function")
        console.log(url_pie)
        var data = [{
            values: response1[0]["sample_values"].slice(0,10),
            labels: response1[0]["otu_ids"].slice(0.10),
            type: "pie"
        }]
        console.log(response1[0]["sample_values"].slice(0,10))
        var layout = {
            height: 600,
            width: 700
        }
        Plotly.newPlot('pie', data, layout)
    })
}


//function init() {
//  var data = [{
//    values: [19, 26, 55, 88],
//    labels: ["Spotify", "Soundcloud", "Pandora", "Itunes"],
//    type: "pie"
//  }];
//
//  var layout = {
//    height: 600,
//    width: 800
//  };
//
//  Plotly.plot("pie", data, layout);
//}
//
//function updatePlotly(newdata) {
//  var PIE = document.getElementById("pie");
//  Plotly.restyle(PIE, "values", [newdata]);
//}
//
//function getData(dataset) {
//  var data = [];
//  switch (dataset) {
//  case "dataset1":
//    data = [1, 2, 3, 39];
//    break;
//  case "dataset2":
//    data = [10, 20, 30, 37];
//    break;
//  case "dataset3":
//    data = [100, 200, 300, 23];
//    break;
//  default:
//    data = [30, 30, 30, 11];
//  }
//  updatePlotly(data);
//}
//
//init();
