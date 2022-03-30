/** 
 * Tranform data from python to form thats plottable
 * Insert data in such a form:
 * {'x_axis': [1, 2, 3], 'y_axis': [[1, 3], [2, 3], [4, 5]], 'names': ['Col 1', 'Col 2']}
 */


export function return_plot(data) {
  let plot_data = [];
  for (var i = 0; i < data.y_axis.length; i++) {
    plot_data.push({
      x: data.x_axis,
      y: data.y_axis[i],
      name: data.names[i],
      line: { width: 1.5 },
    })
  }
  return plot_data;
}


export function return_subplot(data_array) {

  let plot_data = [];
  let data
  let keys = Object.keys(data_array);
  for (var j = 0; j < keys.length; j++) {
    data = data_array[keys[j]]
    for (var i = 0; i < data.y_axis.length; i++) {
      plot_data.push({
        x: data.x_axis,
        y: data.y_axis[i],
        name: data.names[i],
        line: { width: 1.5 },
        yaxis: `y${j + 1}`,
        // xaxis: j == keys.length - 1 ? 'x0' : null
      })
    }
  }

  return plot_data;

}


export function reload_page() {
  window.location.reload()
}
