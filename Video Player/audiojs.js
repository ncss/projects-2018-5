playMusic = function() {
  window.onload = function(){

    var audio = document.getElementById('my-audio');

    audio.addEventListener('seeked', function() {
      for (i = 0; i < myAudio.buffered.length; i++) {

        var startX = myAudio.buffered.start(i) * inc;
        var endX = myAudio.buffered.end(i) * inc;
        var width = endX - startX;

        context.fillRect(startX, 0, width, myCanvas.height);
        context.rect(startX, 0, width, myCanvas.height);
        context.stroke();
      }
    });
  }
}
