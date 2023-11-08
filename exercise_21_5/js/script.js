'use strict'
import { Rational } from "./Rational.js";

const inputField = document.querySelector("#input-field"); // vores input felt
const currentValue = document.getElementById("current-value"); // vores current value felt, som bedre viser den sum vi arbejder med
const log = document.getElementById("log");

const buttonIds = ["add", "sub", "mul", "div", "invert", "reduce", "negate", "clear"]; // ID på vores knapper
const btnArray = buttonIds.map(id => document.getElementById(id)); // laver et array med alle vores knapper, i stedet for at lave dem enkeltvis
var currentRational = null;
let calcLog = [];


btnArray.forEach((button) => {
    button.addEventListener("click", ()=> {
        doOperation(button.id)
    })
})


function doOperation(btnName) {


    if (currentRational !== null || btnName == "clear" || btnName == "invert" || btnName == "reduce" || btnName == "negate") {
        console.log(`performing a ${btnName} on ${currentRational? currentRational.toString():inputField.value}`);
        let inputRational;
        switch (btnName) {
            
            case "add":
                inputRational = Rational.fromString(inputField.value);
                currentRational = currentRational.add(Rational.fromString(inputField.value));
                calcLog.push(["+",inputRational.toString()])
                break;
            case "sub":
                inputRational = Rational.fromString(inputField.value);
                currentRational = currentRational.sub(Rational.fromString(inputField.value));
                calcLog.push(["-",inputRational.toString()])
                break;

            case "mul":
                inputRational = Rational.fromString(inputField.value);
                currentRational = currentRational.mul(Rational.fromString(inputField.value));
                calcLog.push(["*",inputRational.toString()])
                break;

            case "div":
                inputRational = Rational.fromString(inputField.value);
                currentRational = currentRational.div(Rational.fromString(inputField.value));
                calcLog.push(["/",inputRational.toString()])
                break;

            case "invert":
            case "reduce":
            case "negate":
                // Bare lidt sjovt JS lir, hvor jeg via bracket notation kan tilgå metoderne i Rational, da de er af samme navn
                //...Dette kunne også gøres ovenover
                if (inputField.value == "") {
                    currentRational = currentRational[btnName]();
                } else {
                    currentRational = Rational.fromString(inputField.value)[btnName]();
                    calcLog = [[inputField.value,""]]
    
                }
                calcLog.push([" & ",btnName]);
                break;
            case "clear":
                currentRational = null;
                calcLog = [];
                break;
            default:
                console.log("Default switch ")
                break;
        }
    }
    else {
        currentRational = Rational.fromString(inputField.value)
        calcLog.push(["",currentRational.toString()])
    }
    updateCurrentValue(); // opdaterer vores current value felt efter hver operation
}

function updateCurrentValue() {
    if (currentRational !== null) {
        currentValue.textContent = currentRational.toString();
        inputField.value = "";
    } else {
        currentValue.textContent = ""; // min default
    }
    // vi joiner vores log array hvis den har indhold, og smider den ud i vores log felt - ellers paster vi blot en tom string
    log.textContent = calcLog.length > 0? calcLog.map((item) => item.join(" ")).join(" ") + " = "+ currentRational.toString():""; 
}   
