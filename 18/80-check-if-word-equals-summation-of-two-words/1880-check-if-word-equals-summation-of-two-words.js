/**
 * @param {string} firstWord
 * @param {string} secondWord
 * @param {string} targetWord
 * @return {boolean}
 */
var isSumEqual = function (firstWord, secondWord, targetWord) {
  let letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j'];
  let firstValue = '';
  let secondValue = '';
  let targetValue = '';

  for (let char of firstWord) {
    firstValue += letters.indexOf(char);
  }
  for (let char of secondWord) {
    secondValue += letters.indexOf(char);
  }
  for (let char of targetWord) {
    targetValue += letters.indexOf(char);
  }

  let sum = parseInt(firstValue) + parseInt(secondValue);
  if (sum === parseInt(targetValue)) {
    return true;
  } else {
    return false;
  }
};

console.log(
  isSumEqual((firstWord = 'acb'), (secondWord = 'cba'), (targetWord = 'cdb'))
);
