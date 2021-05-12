function longestPalindrome(word) {
        for (var j = 0; j < word.length; j++) {
            for (var k = word.length -1; k >= 0; k--) {
                temp = word.substring(j, (word.length -1 )-k)
                if (temp[j] == temp[k]) {
                    console.log(temp)
                }
    }
}

longestPalindrome("abacaed")