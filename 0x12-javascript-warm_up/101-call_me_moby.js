#!/usr/bin/node

const executeUtils = {
  executeNTimes: function (x, theFunction) {
    for (let a = 0; a < x; a++) {
      theFunction();
    }
  }
};

module.exports = executeUtils;
