let filePath = '/static/mp3/'
let songs;
let songCount = 0;
let audio = document.getElementById('audioPlayer');
let albumCover = document.getElementById('albumCover');
let timeouts = []
let currentSongId = 0;

function playNextSnippet() {
  for (var i = 0; i < timeouts.length; i++) {
    clearTimeout(timeouts[i]);
  }
  timeouts = [];
  let audio = document.getElementById('audioPlayer');
  if (isFinite(audio.duration)) {
    audio.currentTime = (audio.duration/2) - 5;
  }
  audio.play();
  seconds = 0;
  timeouts.push(setTimeout(function() {
    playNextSnippet();
  }, 10000));
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

function updateAlbumCoverPath(filePath) {
  albumCover.src = filePath;
}

function updateValues(songJSON){
  try {
    document.getElementById("musicTitle").innerHTML = songJSON.title;
    document.getElementById("musicArtist").innerHTML = songJSON.artist;
    updateAudioPath(songJSON.location);
    updateAlbumCoverPath(songJSON.coverlocation);
  } catch(err) {
    console.log('No more songs!!!');
    noMoreSongs();
  }
}

function noMoreSongs() {

}

function getSongs() {
  fetch('/songdb').then(function(response) {
    return response.json();
  }).then(function(data) {
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
