/**
 * 
 * @param {DOMElement} elm HTML element to monitor 
 * @param {function} callback a callback function that is called every time there is a new  receives newHeight as argument
 */
function onElementHeightChange(elm, callback) {
  var lastHeight = elm.scrollHeight;
  var newHeight = 0;
  
  (function run() {
    newHeight = elm.scrollHeight;
    if (lastHeight != newHeight)
      callback(newHeight)
    lastHeight = newHeight

    if (elm.onElementHeightChangeTimer)
      clearTimeout(elm.onElementHeightChangeTimer)
    elm.onElementHeightChangeTimer = setTimeout(run, 200)
  })()
}

onElementHeightChange(document.documentElement, function(newHeight) {
    console.log('iframed: onElementHeightChanged: newheight: ', newHeight)
    window.parent.postMessage( newHeight, "*")
  })
  
