function isPalindrome(word) {
    if (word == '') {
        return 'palindrome'
    }
    for (var x = 0; x < word.length/2; x++) {
        var temp1 = word[x]
        var temp2 = word[(word.length-1) - x]
        if (word[x] != word[(word.length-1) - x]) {
            return 'not a palindrome';
        } else {
            continue;
        }
    } 
    return 'palindrome!'
}

// console.log(isPalindrome("qwerttttttreq"))



// console.log(isPalindrome("racecar"));
// console.log(isPalindrome("raceecar"));
// console.log(isPalindrome("raceeecar"));
// console.log(isPalindrome(""));
// console.log(isPalindrome("a"));
// console.log(isPalindrome("aa"));
// console.log(isPalindrome("ab"));


function longestPalindrome(word) {
        for (var j = 0; j < word.length; j++) {
            for (var k = word.length -1; k >= 0; k--) {
                temp = word.substring(j, k+1)
                console.log()
                if (isPalindrome(temp) == 'palindrome!') {
                    return temp
                }
    }
}
}

console.log(longestPalindrome("qwerttttttreqwerewy"))
// // "ehjgkkgeh" -> "gkkg"
// // "ehjg kkgeh" -> "kk"
// // "qwertttreqwerewy" -> "ertttre"
// // "qwerttttttreqwerewy" -> "erttttttre"
// // "abacabd" -> "bacab"
// // "abacaed" -> "aba" or "aca"
// // "abcde" -> "a" or "e", but probably "a"