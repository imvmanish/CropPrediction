function validateForm(rainfall,ph) {
    let messages = [];
	if(rainfall == null || rainfall === '') {
		messages.push('Rainfall Value is Required');
	}
    if(ph == null || ph === '') {
		messages.push('pH Value is Required');
	}
    if(ph <0 || ph > 14) {
		messages.push('pH Value should be in range 0 to 14');
	}
    if(rainfall < 0) {
		messages.push('Rainfall Value cannot be negative');
	}
	return messages;
}

module.exports = validateForm