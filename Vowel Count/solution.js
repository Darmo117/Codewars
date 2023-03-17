function getCount(str) {
  return str.split("").reduce((acc, c) => acc + "aeiou".includes(c), 0);
}
