function pizzaOven(crustType, sauceType, cheeses, toppings) {
    var pizza = {}
    pizza.crustType = crustType;
    pizza.sauceType = sauceType;
    pizza.cheeses = cheeses;
    pizza.toppings = toppings;
    return pizza
}

var pizza1 = pizzaOven("deep dish", "traditional", "mozzarella", ["pepperoni", "sausage"])
console.log(pizza1)

var pizza2 = pizzaOven("hand tossed", "marinara", ["mozzarella", "feta"], ["mushrooms", "olives", "onions"])
console.log(pizza2)

var pizza3 = pizzaOven("thin crust", "BBQ sauce", "provolone", ["chicken", "bacon"])
console.log(pizza3)

var pizza4 = pizzaOven("deep dish", "traditional", ["provolone", "feta"], ["pepperoni", "sausage", "mushrooms"])
console.log(pizza4)

var randompPizza = {
    crustType: ["deep dish", "hand tossed", "thin crust"],
    sauceType: ["traditional", "marinara", "BBQ sauce"],
    cheeses: ["mozzarella", "feta", "provolone", "cheddar"],
    toppings: ["pepperoni", "sausage", "mushrooms", "olives", "onions","chicken", "bacon"],
    createPizza: function() {
        var rPizza = {};
        rPizza.crustType = this.crustType[random(this.crustType.length)];
        rPizza.sauceType = this.sauceType[random(this.sauceType.length)];
        var toAdd = []
        for (i=0; i < this.cheeses.length; i++) {
            var toAddNum = random(2);
            if (toAddNum == 1) {
                toAdd.push(this.cheeses[i])
            }
        }
        rPizza.cheeses = toAdd;
        var toAdd = []
        for (i=0; i < this.toppings.length; i++) {
            var toAddNum = random(2);
            if (toAddNum == 1) {
                toAdd.push(this.toppings[i])
            }
        }
        rPizza.toppings = toAdd;
        
        return rPizza
    }
}

function random(n) {
    return Math.floor(Math.random() * n)
}

console.log(randompPizza.createPizza())