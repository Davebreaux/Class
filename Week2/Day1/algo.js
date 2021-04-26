// function d6(a) {
//     var roll = Math.ceil(Math.random() * a);
    
//     return roll;
// }
    
// var playerRoll = d6(3);
// console.log("The player rolled: " + playerRoll);







var lifesAnswers = [
    "It is certain.",
    "It is decidedly so.",
    "Without a doubt.",
    "Yes – definitely.",
    "You may rely on it.",
    "As I see it, yes.",
    "Most likely.",
    "Outlook good.",
    "Yes.",
    "Signs point to yes.",
    "Reply hazy, try again.",
    "Ask again later.",
    "Better not tell you now.",
    "Cannot predict now.",
    "Concentrate and ask again.",
    "Don't count on it.",
    "My reply is no.",
    "My sources say no.",
    "Outlook not so good.",
    "Very doubtful."
];

function magicEightBall() {
    var n = Math.floor(Math.random() * lifesAnswers.length)
    var answer = lifesAnswers[n];
    return answer
}

console.log(magicEightBall())
