/*
 * Example Rational as js
 */
export class Rational {
    constructor(numerator, denominator) {
        numerator = parseInt(numerator);
        denominator = parseInt(denominator);
        

        if (isNaN(numerator)) {
            throw new Error("Invalid numerator");
        }

        if (isNaN(denominator)) {
            denominator = 1;
        }

        if (denominator === 0) {
            throw new Error("Denominator cannot be zero");
        }

        if (denominator < 0) {
            // normalisere udtrykket, så minus(-) altid er foran numeratoren
            numerator = -numerator;
            denominator = -denominator;
        }

        this.numerator = numerator;
        this.denominator = denominator;
    }

    static fromString(str) {

        let [numerator, denominator] = str.split("/");

        return new Rational(numerator, denominator);
    }


    add(other) {
        let new_num = this.numerator * other.denominator + other.numerator * this.denominator;
        let new_den = this.denominator * other.denominator;
        return new Rational(new_num, new_den).reduce();
    }

    sub(other) {
        let new_num = this.numerator * other.denominator - other.numerator * this.denominator;
        let new_den = this.denominator * other.denominator;
        console.log(new_num, new_den);
        return new Rational(new_num, new_den).reduce();
    }

    mul(other) {
        let new_num = this.numerator * other.numerator;
        let new_den = this.denominator * other.denominator;
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

    gcd(a, b) {
        return b ? this.gcd(b, a % b) : a;
    }
}