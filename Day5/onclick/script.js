var number = 0;

function addTo() {
    number++;
    console.log(number)
    updateNum();
}

function subtractFrom() {
    number--;
    console.log(number)
    updateNum()
}

function updateNum()
    var content = "<h1>"+number+"</h1>";
    document.getElementById("counter").innerHTML = content;
