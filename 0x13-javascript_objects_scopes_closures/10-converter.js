#!/usr/bin/node

exports.converter = function (base) {
  return function convertToBase (num) {
    if (num < base) {
      return num.toString();
    }
    const remainder = num % base;
    const quotient = Math.floor(num / base);
    return convertToBase(quotient) + remainder.toString();
  };
};
