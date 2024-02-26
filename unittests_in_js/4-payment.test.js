// playing around with stubs

const expect = require('chai').expect;
const sinon = require('sinon');
const sendPaymentRequestToApi = require('./4-payment');
const Utils = require('./utils');

describe('sendPaymentRequestToApi', () => {
  it('should return 200 if the payment is successful', () => {
    const stub = sinon.stub(Utils, 'calculateNumber').returns(10);

    const Spy = sinon.spy(console, 'log');

    sendPaymentRequestToApi(100, 20);

    expect(stub.calledOnceWithExactly('SUM', 100, 20)).to.be.true;
    expect(Spy.calledWith('The total is: 10')).to.be.true;

    stub.restore();
    Spy.restore();
  });
});
