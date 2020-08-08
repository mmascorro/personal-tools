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

function debounce(delay, fn) {
    let timeoutId;

    return function (...args) {
        if (timeoutId) {
            clearTimeout(timeoutId);
        }
        timeoutId = setTimeout(() => {
            fn(...args);
            timeoutId = null;
        }, delay);
    }
}

document.getElementById('amount').addEventListener('input', debounce(500, (e) => { 
    let amount = e.target.value;
    amount = amount.replace(/[^\d\.-]/g, '');
    e.target.value = amount;
}));