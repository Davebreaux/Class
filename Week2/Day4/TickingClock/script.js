var time
var hours
var minute
var seconds

function getSecondsSinceStartOfDay() {
    return new Date().getSeconds() 
    + 
    new Date().getMinutes() * 60 
    + 
       new Date().getHours() * 3600;
}

function convert12() {
    if (hours > 12) {
        return hours-12
    } else if(hours <=12){
        return hours;
    }
}

setInterval( function() {
    time = getSecondsSinceStartOfDay();
    hours = time/3600;
    minute = (time - Math.floor(hours)*3600) / 60;
    seconds = time % 60;
    hours12 = convert12();
    console.log(`seconds ${seconds}`);
    console.log(`minutes ${minute}`)
    console.log(`hours ${hours}`);
    document.getElementById("seconds").style.transform = `rotate(${seconds*6 - 180}deg)`;
    document.getElementById("minutes").style.transform = `rotate(${minute*6 - 180}deg)`;
    document.getElementById("hour").style.transform = `rotate(${convert12()*30 - 180}deg)`;
}, 1000);

