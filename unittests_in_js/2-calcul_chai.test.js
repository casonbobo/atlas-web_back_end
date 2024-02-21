// Task 0 test cases

const expect = require('chai').expect;
const calculateNumber = require('./2-calcul_chai.js');

describe('calculateNumber', () => {
    it('adding 1 and 3, return 4', () => {
        expect(calculateNumber('SUM', 1, 3)).to.equal(4);
    });
    it('SUBTRACT 4 and 4, return 0', () => {
        expect(calculateNumber('SUBTRACT', 4.2, 3.7)).to.equal(0);
    });
    it('DIVIDE 8 and 1, return 8', () => {
        expect(calculateNumber('DIVIDE', 8, 1)).to.equal(8);
    });
    it('DIVIDE 1 and 5, return 0.2', () => {
        expect(calculateNumber('DIVIDE', 1.2, 5.3)).to.equal(0.2);
    });
    it('DIVIDE 1.5 and 0, return ERROR', () => {
        expect(calculateNumber('DIVIDE', 1.5, 0)).to.equal('Error');
    });
})
