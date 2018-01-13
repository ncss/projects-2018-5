// let testJson = {
//   filePath:'../mp3/',
//   songs:{
//   'Paradise':{file:'Paradise.mp3'},
//   'Havana':{file:'Paradise.mp3'},
//   'Never':{file:'Paradise.mp3'},
//   'BlankSpace':{file:'Paradise.mp3'}
//   }
// };
//
// let songList = [{'Paradise':{file:'Paradise.mp3'}},
// {'Havana':{file:'Paradise.mp3'}},
// {'Never':{file:'Paradise.mp3'}},
// {'BlankSpace':{file:'Paradise.mp3'}}];

function playNextSnippet() {
  console.log("")
  let audio = document.getElementById('audioPlayer');
  audio.currentTime = (audio.duration/2) - 5;
  audio.play();
  setTimeout(function(){
    audio.pause();
    // Audio();
  },10000);
}

let audio = document.getElementById('audioPlayer');
if (audio.readyState >= 1) {
  playNextSnippet();
} else {
  audio.addEventListener("loadeddata", playNextSnippet);
}
