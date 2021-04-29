var displayDiv = document.querySelector("#display");

displayDiv.innerText = `0`;

var inputNum = "";

var operator = "";

var number1 = 0

var number2 = 0

var answer = ""

function press(n) {
    inputNum += n;
    console.log(inputNum)
    displayDiv.innerText = `${inputNum}`;
}

function setOP(op) {
    number1 = parseFloat(inputNum);
    operator = op;
    inputNum = ""
}

function calculate() {
    number2 = parseFloat(inputNum);
    switch (operator) {
        case "+":
            answer = `${number1 + number2}`
            break;
        case "-":
            answer = `${number1 - number2}`
            break;
        case "*":
            answer = `${number1 * number2}`
            break;
        case "/":
            answer = `${number1 / number2}`
            break;
        default:
            break;
    }
    displayDiv.innerText = answer;
}

function clr() {
    displayDiv.innerText = `0`;
    inputNum = ``
    operator = ``
    number1 = 0
    number2 = 0
}