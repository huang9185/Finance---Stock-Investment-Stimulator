document.addEventListener('DOMContentLoaded', () => {
    document.querySelector('#submit').disabled = true;
    document.querySelector('#sharenumber').onchange = () => calculate_total(
        document.querySelector('#sharenumber').value
    );
});

function calculate_total(input) {
    if (input == '' || input == '0') {
        alert("Number of shares to sell cannot be zero or empty.");
        document.querySelector('#submit').disabled = true;
    } else {
        input = +input;
        numberTotal = +document.querySelector('.card-subtitle').dataset.total;
        if (input < 0 || input > numberTotal) {
            alert("Number of shares to sell must be smaller than the amount you owned.");
            document.querySelector('#submit').disabled = true;
        } else if (Number.isInteger(input) == false) {
            document.querySelector('#submit').disabled = true;
            alert("Number of shares to sell must be an integer.");
        } else {
            price = +document.querySelector('#price').value;
            document.querySelector('#submit').disabled = false;
            document.querySelector('.form-text').innerHTML = `${input} shares X $${price} = $${ new Intl.NumberFormat().format(input*price)}`;
        }
    }
}