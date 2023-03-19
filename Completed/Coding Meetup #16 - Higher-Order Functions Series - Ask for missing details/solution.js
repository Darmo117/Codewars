function askForMissingDetails(list) {
  let missing = []
  list.map(e => {
    for (let [k, v] of Object.entries(e)) {
      if (v === null) {
        e.question = `Hi, could you please provide your ${k}.`;
        missing.push(e);
      }
    }
  });
  return missing;
}
