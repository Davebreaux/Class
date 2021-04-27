function acceptCookies() {
    var content = document.querySelector("#cookies")
    console.log(content)
    content.remove();
}

var unitType = "C"

function farenheight(c) {
    var f = (c*(9/5)) + 32;
    return f;
}

function celsius(f) {
    var c = (f-32) * (5/9)
    return c;
}

function convert(element) {
    if (element.value == "F") {
        for (var i = 0; i < 8; i++) {
            temp = document.querySelector("#t"+i);
            temp.innerText = celsius(parseFloat(temp.innerText)).toFixed(2);
        }
    } else if (element.value == "C") {
        for (var i = 0; i < 8; i++) {
            temp = document.querySelector("#t"+i);
            temp.innerText = farenheight(parseFloat(temp.innerText)).toFixed(2);
        }
    } 
}

