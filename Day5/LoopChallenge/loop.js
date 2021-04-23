// Prints odds 1-20
for (var i = 1; i <= 20; i++) {
    if (i % 2 != 0) {
        console.log(i);
    }
}

// Prints the desired sequence

for (var i = 4; i > -4; i-=1.5) {
    console.log(i);
}

// Sigma
var sigma = 0;
for (var i = 1; i<=100; i++) {
    sigma += i;
}
console.log(sigma)

var product = 1;
for (var n = 1; product < 1e8; n++) {
    product = product * n;
    if (product > 1e8) {
        console.log(n)
    }
} 