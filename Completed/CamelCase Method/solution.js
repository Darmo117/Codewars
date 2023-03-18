String.prototype.camelCase = function () {
  return this.split(" ").reduce((acc, v) => acc + v.charAt(0).toUpperCase() + v.substr(1).toLowerCase(), "")
}
