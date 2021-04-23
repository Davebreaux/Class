//highpass
function highPass(arr, cutoff) {
    var filteredArr = [];
    for (var i = 0; i < arr.length; i++) {
        if (arr[i] > cutoff) {
            filteredArr.push(arr[i])
        }
    }
    return filteredArr;
}
var res = highPass([6, 8, 3, 10, -2, 5, 9], 5);
console.log(res); // we expect back [6, 8, 10, 9]




function evensOfOdds(arr) {
    var totalOdds = 0;
    var totalEvens = 0;
    for (var i = 0; i < arr.length; i++) {
        if (arr[i] % 2 == 0) {
            totalEvens+= arr[i];
        } else {
            totalOdds+= arr[i];
        }
    }
    if (totalOdds == totalEvens) {
        return 'Tied'
    } else if (totalOdds > totalEvens) {
        return 'odds are larger'
    } else if (totalOdds < totalEvens) {
        return 'evens are larger'
    }
}
    
var result2 = evensOfOdds([6, 8, 3, 10, -2, 5, 9]);
console.log(result2); // we expect back "evens are larger"



function betterThanAverage(arr) {
    var sum = 0;
    for (var i = 0; i < arr.length; i++) {
        sum+= arr[i]
    }
    var count = 0
    for (var j = 0; j < arr.length; j++) {
        if (arr[j] > (sum/arr.length)) {
            count++
        }
    }
    return count;
}
var result3 = betterThanAverage([6, 8, 3, 10, -2, 5, 9]);
console.log(result3); // we expect back 4

//fibonacci

function fibonacciArray(n) {
    // the [0, 1] are the starting values of the array to calculate the rest from
    var fibArr = [0, 1];
    for (var i = 0; i <= n; i++) {
        fibArr.push((fibArr[i] + fibArr[i+1]))
    }
    return fibArr;
}
var resultFIB = fibonacciArray(10);
console.log(resultFIB)

console.log('hello')