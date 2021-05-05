// parensValid(input)
// input is a string
// return true if the input has a valid configuration of parentheses and false
// otherwise. by "return true/false" I mean the boolean value, not a string
// what's valid?
// - no more open parens than close parens or vice versa
// - no close parens that appear before a valid open paren
// - ignore all other characters that are not ( and )
// - () -> true
// - )( -> false
// - hello! -> true (???)
// - (()) -> true
// - (q(a)(x)(!(7(xx)(34)(2, 7, 11)))) -> true
// - (() -> false
// - hello!() -> true
// suggestion - don't bother trying to split the string...
// it won't do us any good and just makes things more complicated
// suggestion again - do we have to check every single character in the input?
// hypothetical input: ) followed by one billion characters
// or: a) followed by one billion characters
// or: a37()) followed by one billion characters

function parensValid(input, left_char, right_char) {
    var open = 0;
    var closed = 0;
    for( var i = 0; i < input.length; i++) {
        if (input[i] == left_char) {
            open += 1;
        }
        else if (input[i] == right_char) {
            closed += 1;

            if (closed > open) {
                return false;
            }
        }
    }

    // return closed == open;
    if (closed == open) {
        return true;
    }
    else {
        return false;
    }
}

console.log(parensValid('()'));
console.log(parensValid('(())'));
console.log(parensValid('(q(a)(x)(!(7(xx)(34)(2, 7, 11))))', '(', ')'));
console.log(parensValid(')('));
console.log(parensValid('(()'));
console.log(parensValid('hello!'));
// make your own test cases too

// bracesValid(input)
// as above, but for parentheses, curly brackets (or curly braces) and square
// brackets -for- -now-: don't worry if there's some weirdness where brackets
// and parentheses are interlinked with each other - we'll handle that later
// ([)] -> true (?????)
// ()[]{} -> true
// (] -> false
// x(37[q{3, 7, 9}{22, 6, 91}])(32q) -> true
// ()]... -> false
// a gentle suggestion - look at what you did for the previous function and
// see if anything can be reused

// input - a string
// brackets - an array of brackets, i.e. [['(', ')'], ['[' , ']'], ['<', '>']]

function bracesValid(input, brackets){
    if (parensValid(input, '(', ')') == false) {
        return false;
    }
    if (parensValid(input, '[', ']') == false) {
        return false;
    }
    if (parensValid(input, '{', '}') == false) {
        return false;
    }
    return true;
}

console.log(bracesValid('[(uie])(){}'));

function bracesValid2(input, brackets){
    for (var i = 0; i < brackets.length; i++) {
        if (parensValid(input, brackets[i][0], brackets[i][1]) == false) {
            return false;
        }
    }
    return true;
}

console.log(bracesValid2('[(uie])()<>', [['(', ')']]));
console.log(bracesValid2('[(uie])()><', [['(', ')'], ['[' , ']'], ['<', '>']]));

// bonus: what if we also want to check angle brackets (< and >)? what if
// sometimes we care about curly braces but sometimes we don't?
// suggestion - go back to parensValid/bracesValid and see if they can be
// improved in some way