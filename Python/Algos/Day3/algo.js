// generateCoinChange(input)
// input is an integer representing an amount of money
// output is an object representing the most optimal
// (i.e. fewest coins) way to represent that amount
// with standard U.S. coins
// if the input is 74 cents, the output would be:
// {quarters: 2, dimes: 2, nickels: 0, pennies: 4}
// if the input is 109 cents, the output would be:
// {quarters: 4, dimes: 0, nickels: 1, pennies: 4}
var coin_values = {'quarters': 25, 'dimes': 10, "nickels": 5, "pennies": 1}


function generateCoinChange(input) {
    var output = {'quarters': 0, 'dimes': 0, 'nickels': 0, 'pennies': 0};
        for (x in coin_values) {
            output[x] = Math.floor((input)/coin_values[x])
            // coin_total += coin_values[x] * output[x]
            input -= coin_values[x] * output[x]
        }
    return output;
}

console.log(generateCoinChange(109));

// generateCoinChangeWithGivenValues(input, values)
// input is an integer representing an amount of money
// values is an array of arrays - each array represents a
// denomination of currency (string) and its value (integer)
// (a denomination of 1 will always be present)
// that array is in order of denomination
// the output is an object representing the most optimal
// way to represent that amount given the denominations
// if the input is 127 cents, and the values are:
// [ ['metadime', 15],
//  ['supernickel', 6]
//  ['very regular penny', 1]]
// the output would be:
// {metadimes: 8, supernickels: 1, very regular pennys: 1}
// (note the pluralization)
// if the input was 127, but the values were:
// [ ['halfquarter', 12],
//  ['greater nickel', 8],
//  ['lesser dime', 3]
//  ['just-a-penny', 1]]
// the output would be:
// {halfquarters: 10, greater nickels: 0, lesser dimes: 2, just-a-pennys: 0}
// (these values -could- be an object, but I want to get you used to
// the concept of arrays within arrays and accessing that data)
//
// bonus: what would you do if we couldn't guarantee a denomination of 1
// being present? there are a few different answers


function generateCoinChangeWithGivenValues(input, values) {
        var output = {};
            for (var x = 0; x < values.length; x++) {
                // output[(values[x][0])] = 0;
                output[values[x][0]] = Math.floor((input)/values[x][1]);
                input -= (values[x][1] * output[values[x][0]]);
            
            }
        return output;
        }


console.log(generateCoinChangeWithGivenValues(127, [ ['halfquarter', 12], ['greater nickel', 8],['lesser dime', 3],['just-a-penny', 1]]))