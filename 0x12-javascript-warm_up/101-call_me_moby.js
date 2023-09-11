#!/usr/bin/node

function callMeMoby (x, theFunction) {
  for (let a = 0; a < x; a++) {
    theFunction();
  }
}

module.exports.callMeMoby = callMeMoby;
