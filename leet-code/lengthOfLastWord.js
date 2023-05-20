// 58. Length of Last Word

// const lengthOfLastWord = (s) => {
//   const strArr = s.split(' ');
//   let i = strArr.length - 1;

//   while (i >= 0) {
//     const word = strArr[i];

//     if (word) return word.length;
//     i--;
//   }

//   return 0;
// };

const lengthOfLastWord = (s) => {
  let result = '';
  let i = s.length - 1;

  while (i >= 0) {
    const letter = s[i];

    if (letter === ' ') {
      if (!result) i--;
      else break;
    } else {
      result += letter;
      i--;
    }
  }

  return result.length;
};

console.log(
  lengthOfLastWord('Hello World'),
);
