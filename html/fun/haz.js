var box = document.getElementById("box");
var isBoxRight = false;

function togglePosition() {
    box.classList.toggle("right");
    isBoxRight = !isBoxRight;
}