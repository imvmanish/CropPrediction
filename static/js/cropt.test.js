const crop = require('./cropt');
const print_city = crop.print_city
const print_state = crop.print_state
const state_arr = crop.state_arr
const s_a = crop.s_a

test('State Function',() => {
    expect(print_state(0)).toBe("Andaman & Nicobar");
});

test('State Function',() => {
    expect(print_state(1)).toBe("Andhra Pradesh");
});

test('State Function',() => {
    expect(print_state(4)).toBe("Bihar");
});

test('State Function',() => {
    expect(print_state(16)).toBe("Karnataka");
});

test('State Function',() => {
    expect(print_state(1)).toBe("Andhra Pradesh");
});

test('State Function',() => {
    expect(print_state(34)).toBe("West Bengal");
});

//Testing City Functions

test('City Function',() => {
    expect(print_city(1,0)).toBe("Alipur");
});

test('City Function',() => {
    expect(print_city(2,2)).toBe("Adoni");
});

test('City Function',() => {
    expect(print_city(10,0)).toBe("Central Delhi");
});

test('City Function',() => {
    expect(print_city(0,0)).toBe("");
});

test('City Function',() => {
    expect(print_city(17,6)).toBe("Arsikere");
});

test('City Function',() => {
    expect(print_city(34,0)).toBe("Almora");
});
