#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  const count = list.reduce((accumulator, currentElement) => {
    if (currentElement === searchElement) {
      return accumulator + 1;
    }
    return accumulator;
  }, 0);

  return count;
};
