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