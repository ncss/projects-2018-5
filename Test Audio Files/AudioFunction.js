playSong = function() {
  let audio = document.getElementById('audioPlayer');
  let songLength = audio.length;
  let start = songLength / 2;
  audio.currentTime = start;
  audio.play();
}

playSong();
