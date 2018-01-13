let startX;



albumCover.addEventListener("pointerdown", pointerdown);
function pointerdown(event){
  event.preventDefault();
  startX = event.screenX;
  albumCover.setPointerCapture(event.pointerId);
}

albumCover.addEventListener("pointermove", pointermove);
function pointermove(event){
  let difference = (startX - event.screenX) * -1;
  albumCover.style.transform = `translate(${difference}px)`;
}

albumCover.addEventListener("pointerup", pointerout);
function pointerout(event){

  let difference = (startX - event.screenX) * -1;
  startX = undefined;
  if (difference > 150) {
    voteUp.click()
  }
  else if (difference < -150) {
    voteDown.click()
  }
  albumCover.style.transform = null;
}
