function reverseString(str) {
    backStr = ""
    for (var i = str.length-1; i>=0; i--) {
        backStr += str[i]
    }
    return backStr
}
console.log(reverseString('This is a test'))


var test = "this is a test";
test[2] = "e"
console.log(test)