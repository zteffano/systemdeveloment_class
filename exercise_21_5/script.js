/*
 * Example Rational as js
 */
class Rational {
    constructor(numerator, denominator) {
        if (denominator === undefined) {
            this.denominator = 1;
        } else {
            this.denominator = parseInt(denominator);
        }
        this.numerator = parseInt(numerator);
    }

    add(other) {
        let new_num = this.numerator * other.denominator + other.numerator * this.denominator;
        let new_den = this.denominator * other.denominator;
        return new Rational(new_num,new_den).reduce();
    }

    sub(other) {
        let new_num = this.numerator * other.denominator - other.numerator * this.denominator;
        let new_den = this.denominator * other.denominator;
        console.log(new_num, new_den);
        return new Rational(new_num, new_den).reduce();
    }

    mul(other) {
        let new_num = this.numerator * other.numerator;
        let new_den = this.denominator * other. denominator;
        return new Rational(new_num, new_den).reduce();
    }

    div(other) {
        let new_num = this.numerator * other.denominator;
        let new_den = this.denominator * other.numerator;
        return new Rational(new_num, new_den).reduce();
    }

    invert() {
        return new Rational(this.denominator, this.numerator);
    }

    negate() {
        return new Rational(-this.numerator, this.denominator);
    }

    reduce() {
        let gcd = this.gcd(this.numerator, this.denominator);
        return new Rational(this.numerator / gcd, this.denominator / gcd);
    }

    toString() {
        if (this.numerator === 0 || this.denominator === 0) {
            return "0";
        }
        return `${this.numerator}/${this.denominator}`;
    }
    gcd (a, b) {
        return (b) ? this.gcd(b, a % b) : a;
    }


    
    // todo

}

const inputField = document.querySelector("#input-field");
const addBtn = document.getElementById("add");
const subBtn = document.getElementById("sub");
const multBtn = document.getElementById("mul");
const divBtn = document.getElementById("div");
const invBtn = document.getElementById("invert");
const reduceBtn = document.getElementById("reduce");
const negBtn = document.getElementById("negate");
//const testBtn = document.getElementById("test");
const clearBtn = document.getElementById("clear");
const currentValue = document.getElementById("current-value");
// mangler EQ => equal btn + logic + element

const btnArray = [addBtn,subBtn,multBtn,divBtn,invBtn,reduceBtn,negBtn,clearBtn];
var tempRational = null;


btnArray.forEach((btn) => {
    btn.addEventListener("click", ()=> {
        if (tempRational != null || btn.id == "clear" || btn.id == "invert" || btn.id == "reduce" || btn.id == "negate") {
           // laver til en sperat funktion senere
            switch(btn.id) {

                case "add":
                    inputField.value = tempRational.add(makeRational(inputField.value)).toString();
                    updateCurrentValue(inputField.value);
                    break;
                case "sub":
                    inputField.value = tempRational.sub(makeRational(inputField.value)).toString();
                    updateCurrentValue(inputField.value);
                    break;
                case "mul":
                    inputField.value = tempRational.mul(makeRational(inputField.value)).toString();
                    updateCurrentValue(inputField.value);
                    break;
                case "div":
                    inputField.value = tempRational.div(makeRational(inputField.value)).toString();
                    updateCurrentValue(inputField.value);
                    break;
                case "invert":
                    inputField.value = makeRational(inputField.value).invert().toString();
                    tempRational = inputField.value;
                    updateCurrentValue(inputField.value);
                    break;
                case "reduce":
                    inputField.value = makeRational(inputField.value).reduce().toString();
                    tempRational = inputField.value;
                    updateCurrentValue(inputField.value);
                    break;
                case "negate":
                    inputField.value = makeRational(inputField.value).negate().toString();
                    tempRational = inputField.value;
                    updateCurrentValue(inputField.value);
                    break;
                case "clear":
                    tempRational = null;
                    inputField.value = "";
                    updateCurrentValue(inputField.value);
                    break;
                default:
                    alert("Something went wrong");
                    break;
            }
    
        }
        else {
            console.log("No tempRational! - adding this");
            tempRational = makeRational(inputField.value);
            updateCurrentValue(inputField.value);
        }
    })
});

function makeRational(inputString) {

    if (inputString.length > 5 || inputString.length < 1) {
        alert("Wrong format - use  5/5 or 5");
        return;
    }
    let splitted = inputString.split("/")
    let numerator = splitted[0];
    let denominator = splitted[1]
    return new Rational(numerator, denominator);
    //alert(`Numerator: ${numerator} Denominator: ${denominator}`);
}

function updateCurrentValue(input) {
    currentValue.innerHTML = input;
}