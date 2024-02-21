// Task 0 test cases

const assert = require('assert');
const calculateNumber = require('./0-calcul.js');

describe('calculateNumber', () => {
  it('adding 1 and 3, return 4', () => {
    assert.strictEqual(calculateNumber(1, 3), 4);
  });
  it('adding 1 and 3.7, return 5', () => {
    assert.strictEqual(calculateNumber(1, 3.7), 5);
  });
  it('adding 1.2 and 3.7, return 5', () => {
    assert.strictEqual(calculateNumber(1.2, 3), 4);
  });
  it('adding 1.5 and 3.7, return 6', () => {
    assert.strictEqual(calculateNumber(1.5, 3.7), 6);
  });
  it('adding 1 and 3.2, return 4', () => {
    assert.strictEqual(calculateNumber(1, 3.2), 4);
  });
})
