let songs;

function getSongs() {
  fetch('/songdb').then(function(response){
    return response.json()
  }).then(function(data){
    songs = data;
  });
}

getSongs();

function playNextSnippet() {
  console.log(songs);
  let audio = document.getElementById('audioPlayer');
  audio.currentTime = (audio.duration/2) - 5;
  audio.play();
  setTimeout(function(){
    audio.pause();
    //Go to next song or if like or dislike
    // Audio();
  },10000);
}

let audio = document.getElementById('audioPlayer');
if (audio.readyState >= 1) {
  playNextSnippet();
} else {
  audio.addEventListener("load", playNextSnippet);
}
