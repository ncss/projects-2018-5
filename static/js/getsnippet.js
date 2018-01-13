let filePath = '/static/mp3/'
let songs;
let songCount = 0
let audio = document.getElementById('audioPlayer');

function playNextSnippet() {
  audio.currentTime = (audio.duration/2) - 5;
  audio.play();
  setTimeout(function(){
    seekNextSong();
  },10000);
}

function seekNextSong() {
  audio.pause();
  songCount += 1;
  let nextSong = songs[songCount];
  changeAudioPath(nextSong.title);
  if (audio.readyState >= 1) {
    playNextSnippet();
  } else {
    audio.addEventListener("loadeddata", playNextSnippet);
  }
}

function changeAudioPath(songName) {
  audio.src = filePath + songName + '.mp3';
}

function getSongs() {
  fetch('/songdb').then(function(response){
    return response.json()
  }).then(function(data){
    songs = data;
  }).then(function() {
    let nextSong = songs[songCount];
    changeAudioPath(nextSong.title);
    let audio = document.getElementById('audioPlayer');
    if (audio.readyState >= 1) {
      playNextSnippet();
    } else {
      audio.addEventListener("loadeddata", playNextSnippet);
    }
  });
}

getSongs();
