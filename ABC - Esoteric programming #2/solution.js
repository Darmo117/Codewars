class Interpreter {
  constructor() {
  }

  /**
   * @param input {string}
   */
  read(input) {
    let tape = input.split("");
    let acc = 0;
    let out = "";
    let debug_out = [];
    let ascii = false;
    let i = 0;
    while (i < tape.length) {
      switch (tape[i]) {
        case "a":
          acc++;
          break;
        case "b":
          acc--;
          break;
        case "c":
          out += (ascii ? String.fromCharCode(acc) : "" + acc);
          break;
        case "d":
          acc = -acc;
          break;
        case "r":
          acc = Math.floor(Math.random() * acc);
          break;
        case "n":
          acc = 0;
          break;
        case "$":
          ascii = !ascii;
          break;
        case "l":
          tape.splice(i, 1);
          i = 0;
          continue;
        case ";":
          debug_out.push(`${acc}->${String.fromCharCode(acc)}`);
          break;
      }
      i++;
    }
    // noinspection JSUnresolvedFunction
    return new Output(out, debug_out);
  }
}
