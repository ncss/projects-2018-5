function getSongs() {
  let songJSONFile;
  let songJSON = fetch('/songdb').then(function(response){
    return response.json()
  }).then(function(songJSON) {
    songJSONFile = songJSON;
  });
  return songJSONFile
}
