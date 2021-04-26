var likes = 0
function addLike() {
    likes++
    document.getElementById("numLikes").innerText = `${likes} likes(s)`;
}