function addUsername(list) {
  let res = [];
  const now = new Date().getFullYear();
  for (let user of list) {
    res.push({
      ...user,
      username: user["firstName"].toLowerCase() + user["lastName"].charAt(0).toLowerCase() + (now - user["age"]),
    });
  }
  return res;
}
