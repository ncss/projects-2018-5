let songs

function getSongs() {
  fetch('/songdb').then(function(response){
    return response.json()
  }).then(function(data){
    songs = data;
    console.log(songs);
    return songs
  });
}

getSongs();
