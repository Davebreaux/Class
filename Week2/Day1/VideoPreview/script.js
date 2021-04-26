function playvid(element) {
    element.play();
    element.muted = false;
    element.controls = true;
    element.loop = true;
}

function pausevid(element) {
    element.pause()
    element.muted = true;
    element.controls = false;
    element.loop = false;
}