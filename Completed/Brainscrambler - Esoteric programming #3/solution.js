class Interpreter {
  constructor() {
    this.stacks = [[0], [0], [0]];
    this.stack_i = 0;
  }

  /**
   * @param input {string}
   */
  read(input) {
    let out = "";
    let i = 0;

    while (i < input.length) {
      const stack = this.stacks[this.stack_i];

      switch (input[i]) {
        case "+":
          if (stack.length) {
            stack[stack.length - 1]++;
          } else {
            stack.push(0);
          }
          break;
        case "-":
          if (stack.length) {
            stack[stack.length - 1]--;
          } else {
            stack.push(0);
          }
          break;
        case "<":
          if (stack.length) {
            const v = stack.pop();
            if (this.stack_i === 0) {
              this.stacks[this.stacks.length - 1].push(v);
            } else {
              this.stacks[this.stack_i - 1].push(v);
            }
          }
          break;
        case ">":
          if (stack.length) {
            this.stacks[(this.stack_i + 1) % this.stacks.length].push(stack.pop());
          }
          break;
        case "*":
          stack.push(0);
          break;
        case "^":
          stack.pop();
          break;
        case "#":
          this.stack_i = (this.stack_i + 1) % this.stacks.length;
          break;
        case ",":
          i++;
          let buffer = "";
          while (0 <= input[i] && input[i] <= 9) {
            buffer += "" + input[i];
            i++;
          }
          i--;
          stack.push(parseInt(buffer));
          break;
        case ".":
          if (stack.length) {
            out += "" + stack[stack.length - 1];
          }
          break;
        case "]":
          if (stack.length && stack[stack.length - 1] > 0) {
            let n = 1;
            while (n > 0) {
              i--;
              if (input[i] === "[") {
                n--;
              } else if (input[i] === "]") {
                n++;
              }
            }
          }
          break;
      }
      i++;
    }

    return out;
  }
}
