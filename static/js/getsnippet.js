let filePath = '/static/mp3/'
let songs;
let songCount = 0;
let audio = document.getElementById('audioPlayer');
let timeouts = []
let currentSongId = 0;

function playNextSnippet() {
  for (var i = 0; i < timeouts.length; i++) {
    clearTimeout(timeouts[i]);
  }
  timeouts = []
  let audio = document.getElementById('audioPlayer');
  if (isFinite(audio.duration)){
    audio.currentTime = (audio.duration/2) - 5;
  }
  audio.play();
  timeouts.push(setTimeout(function(){
    audio.pause();
  },10000));
  timeouts.push(setTimeout(function(){
    nextSong();
  },20000));
}

function nextSong() {
  audio.pause();
  songCount += 1;
  let nextSong = songs[songCount];
  updateValues(nextSong);
  if (audio.readyState >= 1) {
    playNextSnippet();
  } else {
    audio.addEventListener("loadeddata", playNextSnippet);
  }
}

function updateAudioPath(filePath) {
  audio.src = filePath;
}

function updateValues(songJSON){
  document.getElementById("musicTitle").innerHTML = songJSON.title;
  document.getElementById("musicArtist").innerHTML = songJSON.artist;
  updateAudioPath(songJSON.location);
  currentSongId = songJSON.id;
}

function getSongs() {
  fetch('/songdb').then(function(response){
    return response.json()
  }).then(function(data){
    songs = data;
  }).then(function() {
    let nextSong = songs[songCount];
    updateValues(nextSong)
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
