function bookIndex(input) {
    var output = []
    for (var i = 0; i < input.length; i++) {
        var chainStart = input[i]
        var chainEnd = 0
        
        while (input[i+1] == input[i] +1) {
            i++
            chainEnd = input[i]
        }
        if (input[i+1] > input[i] + 1) {
            if (chainEnd == 0) {
                output.push(chainStart)
            } else {

                output.push(chainStart + '-' + chainEnd)
            }
            }
            console.log(chainStart)
            console.log(chainEnd)
        }
        
    return output
}



console.log(bookIndex([58, 104, 105, 106, 192, 194, 195, 196]));


// bookIndex(input)
// input is an array of integers (in order) representing pages in a book
// where a given term is found, and the output is a string suitable
// for printing in a book's index
// if the input is [58, 104, 105, 106, 192, 194, 195, 196]
// the output is: "58, 104-106, 192, 194-196"
// if the input is [1, 2, 3, 4, 5, 8, 9, 10, 11, 12, 15, 17, 18]
// the output is: "1-5, 8-12, 15, 17-18"

// suggestion: break this into two parts, or maybe even two
// functions - get your array of integers and turn it into an array
// of strings, then turn that array of strings into a single string
// [58, 104, 105, 106, 192, 194, 195, 196]
// ["58", "104-106", "192", "194-196"]
// "58, 104-106, 192, 194-196"

// also a suggestion: remember that you can modify your for loop iterator
// during your loop! you can add to or subtract from i at any point

