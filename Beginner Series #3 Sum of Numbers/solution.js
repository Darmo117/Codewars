function getSum(a, b) {
  let c = Math.min(a, b);
  let d = Math.max(a, b);
  return (d - c + 1) * (c + d) / 2;
}
