const validateForm = require('./validt')

test('Validate The Input Form',() => {
    expect(validateForm(200,14)).toStrictEqual([]);
});

test('Validate The Input Form',() => {
    expect(validateForm(200,15)).toStrictEqual(['pH Value should be in range 0 to 14']);
});

test('Validate The Input Form',() => {
    expect(validateForm()).toStrictEqual(["Rainfall Value is Required","pH Value is Required"]);
});
