// Task 0 test cases

const assert = require('assert');
const calculateNumber = require('./1-calcul.js');

describe('calculateNumber', () => {
  it('adding 1 and 3, return 4', () => {
    assert.strictEqual(calculateNumber('SUM', 1, 3), 4);
  });
  it('adding 1 and 3.7, return 5', () => {
    assert.strictEqual(calculateNumber('SUBTRACT', 4.2, 3.7), 0);
  });
  it('adding 1.2 and 3.7, return 5', () => {
    assert.strictEqual(calculateNumber('DIVIDE', 8, 1), 8);
  });
  it('adding 1.2 and 3.7, return 5', () => {
    assert.strictEqual(calculateNumber('DIVIDE', 1.2, 5.3), 0.2);
  });
  it('adding 1.5 and 3.7, return 6', () => {
    assert.strictEqual(calculateNumber('DIVIDE', 1.5, 0), 'Error');
  });
})
