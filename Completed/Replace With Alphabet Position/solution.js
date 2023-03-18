function alphabetPosition(text) {
  return text.toLowerCase().split("")
    .filter(c => /[a-zA-Z]/.test(c))
    .map(c => c.codePointAt(0) - 96)
    .join(" ");
}
