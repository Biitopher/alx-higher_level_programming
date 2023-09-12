#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print (b = 'X') {
    for (let a = 0; a < this.height; a++) {
      console.log(b.repeat(this.width));
    }
  }
}

module.exports = Rectangle;
