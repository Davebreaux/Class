/*function reversearr(arr) {
    var temp = ''
    for (var i = 0; i < arr.length/2; i++) {
        temp = arr[i];
        arr[i] = arr[arr.length-1 - i];
        arr[arr.length -1 - i] = temp;
    }
    return arr
}

console.log(reversearr(["a", "b", "c", "d", "e", "f", 'g', 'h']))


function reversearr2(arr) {
    var temp2 = [];
    for (var j = arr.length-1; j >=0; j--) {
        temp2.push(arr[j])
    }
    return temp2
}
console.log(reversearr2(["a", "b", "c", "d", "e", "f", 'g', 'h'])) */

function reversarr3(arr) {
    var i = 0;
    while (i < arr.length/2) {
        temp = arr[i];
        arr[i] = arr[arr.length-1 - i];
        arr[arr.length -1 - i] = temp;
        i++;
    }
    return arr
}
console.log(reversarr3(["a", "b", "c", "d", "e", "f", 'g', 'h']))