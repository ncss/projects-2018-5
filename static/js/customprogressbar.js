let seconds = 0
let progressBar = document.getElementById('progressBar');

function incrementSeconds() {
  seconds += 0.01;
}

function updateProgressBar() {
  if (!audio.paused) {
    incrementSeconds();
    let percentage = Math.floor(seconds * 10);
    progressBar.style.width = percentage+'%';
    if (seconds >= 10) {
      seconds = 0;
    }
  }
}

setInterval(updateProgressBar, 10);
