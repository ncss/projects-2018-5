let filePath = '/static/mp3/'
let songs;
let songCount = 0
let audio = document.getElementById('audioPlayer');

function playNextSnippet() {
  console.log("")
  let audio = document.getElementById('audioPlayer');
  audio.currentTime = (audio.duration/2) - 5;
  audio.play();
  setTimeout(function(){
    audio.pause();
  },10000);
  setTimeout(function(){
    nextSong();
  },20000);
}

function nextSong() {
  audio.pause();
  songCount += 1;
  let nextSong = songs[songCount];
  updateAudioPath(nextSong.title);
  if (audio.readyState >= 1) {
    playNextSnippet();
  } else {
    audio.addEventListener("loadeddata", playNextSnippet);
  }
}

//To do!!!

function updateAudioPath(songName) {
  audio.src = filePath + songName + '.mp3';
}

function updateArtist() {
  return
}

function updateInfo(songJSON) {
  updateAudioPath(songJSON.title);
}

//To do!!!

function getSongs() {
  fetch('/songdb').then(function(response){
    return response.json()
  }).then(function(data){
    songs = data;
  }).then(function() {
    let nextSong = songs[songCount];
    updateAudioPath(nextSong.title);
    let audio = document.getElementById('audioPlayer');
    if (audio.readyState >= 1) {
      playNextSnippet();
    } else {
      audio.addEventListener("loadeddata", playNextSnippet);
    }
  });
}


//First call gets all the songs from database into a json file
//Songs are auto updated with music and all info!
getSongs();
