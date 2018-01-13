var possibleEmoji = [
     "🎵",
     "🎶",
     "🎤",
     "🎧",
     "🎷",
     "🎸",

];


document.body.addEventListener("pointermove", (event) => {
    if (Math.random() < 0.8) {
        return;
    }

    const index = Math.round(Math.random() * possibleEmoji.length);
    const emoji = possibleEmoji[index];
    console.log(emoji)

    const el = document.createElement("span");
    document.body.appendChild(el);
    el.textContent = emoji;
    el.classList.add('emoji');
    el.offsetLeft;  // forces layout

    el.style.left = event.clientX + 'px';
    el.style.top = event.clientY + 'px';
    el.style.transform = 'translate(' + (Math.random() * -1000 + 500) + 'px, 1200px) scale(0)';

    el.addEventListener('transitionend', () => {
        el.remove()
    })

    }
    );  