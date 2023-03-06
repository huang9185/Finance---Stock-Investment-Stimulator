document.addEventListener('DOMContentLoaded', () => {
    document.querySelector('#sharenumber').onchange = () => calculate_share(
        document.querySelector('#sharenumber').value
    );
    document.querySelector('#submit').disabled = true;
});

function calculate_share(number) {
    if (number == '' || number == '0') {
        alert("Number of shares cannot be empty or zero");
        document.querySelector('#submit').disabled = true;
    }
    else {
        number = +number;
        if (Number.isInteger(number)){
            quote = document.querySelector('#quotename').value;
            api = document.querySelector('label').dataset.api;
            url = "https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol="+quote+"&apikey="+api;
            fetch(url)
            .then(response => response.json())
            .then(data => {
                console.log(data);
                if (data["Global Quote"].length != 0){
                    price = data["Global Quote"]["05. price"];
                    document.querySelector('#sharetotal').innerHTML = `${number} shares X $${price} = $${new Intl.NumberFormat().format(number*price)}`;
                    document.querySelector('#price').value = price;
                    document.querySelector('#submit').disabled = false;
                } else {
                    alert("The quote does not exist.");
                }
            })
        } else{
            alert("Number of shares must be an integer.");
            document.querySelector('#submit').disabled = true;
        } 
    }
}