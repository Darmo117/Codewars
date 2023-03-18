class FiveCommands {
  constructor() {
  }

  /**
   * @param input {string}
   * @param debug {boolean}
   */
  read(input, debug) {
    let data = [0];
    let dp = 0;
    let out = "";
    for (const c of input) {
      switch (c) {
        case "+":
          dp++;
          if (dp === data.length) {
            data.push(0);
          }
          break;
        case "-":
          dp--;
          if (dp === -1) {
            data.splice(0, 0, 0);
            dp = 0;
          }
          break;
        case "^":
          data[dp]++;
          break;
        case "v":
          data[dp]--;
          break;
        case "*":
          out += "" + data[dp];
          break;
      }
    }
    // noinspection JSUnresolvedFunction
    return new Output(out, debug ? data.map((value, i) => `${i}->${value}`) : []);
  }
}
