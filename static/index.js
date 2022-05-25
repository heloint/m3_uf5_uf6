var videoModal = document.getElementById("videoModal");
var videoBtn= document.getElementById("videoBtn");
var videoClose = document.getElementsByClassName("videoClose")[0];


var aboutModal = document.getElementById("aboutModal");
var aboutBtn = document.getElementById("aboutBtn");
var aboutClose = document.getElementsByClassName("aboutClose")[0];


function stopVideo(modal) {
  var currentIframe = videoModal.querySelector('.modal-content > iframe');
  currentIframe.src = currentIframe.src;
}

// When the user clicks the button, open the videoModal 
videoBtn.onclick = function() {
  videoModal.style.display = "block";
}

// When the user clicks on <span> (x), close the videoModal
videoClose.onclick = function() {
  videoModal.style.display = "none";
  stopVideo(videoModal);
}


aboutBtn.onclick = function() {
  aboutModal.style.display = "block";
}

aboutClose.onclick = function() {
  aboutModal.style.display = "none";
}


// When the user clicks anywhere outside of the modal, close it
window.onclick = function(event) {
  if (event.target == videoModal || event.target == aboutModal){
    videoModal.style.display = "none";
    stopVideo(videoModal);
    aboutModal.style.display = "none";
  }
}


