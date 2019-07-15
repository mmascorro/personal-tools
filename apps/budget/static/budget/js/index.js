document.getElementById('sign-change').addEventListener('click', (e) => {
    e.preventDefault();
    let amountInput = document.getElementById('amount');

    let current = amountInput.value;

    let newValue = '';
    if (current.includes('-')) {
        newValue = current.replace('-','');
    } else {
        newValue = `-${current}`;
    }

    amountInput.value = newValue;

});

