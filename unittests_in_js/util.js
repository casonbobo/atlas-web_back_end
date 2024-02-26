const Utils = {
  calculateNumber(type, a, b) {
    const a = Math.round(a);
    const b = Math.round(b);

    switch (type) {
      case 'SUM':
        return a + b;
      case 'SUBTRACT':
        return a - b;
      case 'DIVIDE':
        return b === 0 ? 'Error' : a / b;
      default:
        throw new Error('Unknown operation');
    }
  }
};

module.exports = Utils;
