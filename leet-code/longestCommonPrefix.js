const longestCommonPrefix = (arr) => {
  let [str] = arr;

  for (let i = 1; i < arr.length; i++) {
    const word = arr[i];
    let index = 0;

    while (index <= str.length && str[index]) {
      if (str[index] !== word[index]) {
        str = str.split('').slice(0, index).join('');
        index = 0;
      } else index++;
    }
  }

  return str;
};

console.log(
  longestCommonPrefix(['aa', 'ab']),
  longestCommonPrefix(['flower', 'flow', 'flight']),
);
