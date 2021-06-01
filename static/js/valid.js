//Handle Rainfall and pH
let rainfall = document.getElementById('rainfall');
const ph = document.getElementById('ph');

const errorBox = document.getElementById('err');
const form = document.getElementById('main-form');

form.addEventListener('submit',(e) => {
	let messages = [];
	if(rainfall.value == null || rainfall.value === '') {
		messages.push('Rainfall Value is Required');
	}
    if(ph.value == null || ph.value === '') {
		messages.push('pH Value is Required');
	}
    if(ph.value <0 || ph.value > 14) {
		messages.push('pH Value should be in range 0 to 14');
	}
    if(rainfall.value < 0) {
		messages.push('Rainfall Value cannot be negative');
	}
	if(messages.length > 0) {
		e.preventDefault();
		errorBox.innerText = messages.join('\n');
		errorBox.classList.add('visible');
	}
});