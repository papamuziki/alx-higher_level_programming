#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  let numberOfOccurences = 0;
  for (const i in list) {
    if (list[i] === searchElement) {
      numberOfOccurences++;
    }
  }
  return numberOfOccurences;
};
