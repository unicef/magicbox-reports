/**

 * @param {string} iframeId id of the iframe element in which we want to add the report
 * @param {string} url url of the report to embed. It shall include embed=true
 */
function embed(iframeId, url) {
  console.log("Running embed...");
  // get iframe
  var iframe = document.getElementById(iframeId);
  //Set the width to 100
  iframe.style.width = "100%"
  iframe.src = url  
  //listen to resize events
  window.addEventListener("message", (event) => {
    console.log('embed: resize event sent', event.data)
    iframe.height = event.data
  }, false);
  console.log(iframe)
}

