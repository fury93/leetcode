    return this;
  }
  multiply(value) {
    this.result *= value;
    return this;
  }
  divide(value) {
    if(value === 0) throw "Division by zero is not allowed";
    this.result /= value;
    return this;
  subtract(value){
    this.result -= value;
  add(value){
    this.result += value;
    return this;
  }
class Calculator {
  constructor(value) {
    this.result = value;
  }
["Calculator", "add", "subtract", "getResult"]
[10, 5, 7]
["Calculator", "multiply", "power", "getResult"]
