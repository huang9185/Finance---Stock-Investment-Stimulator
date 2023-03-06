document.addEventListener('DOMContentLoaded', () => {
    // Input does not exist
    try {
        document.querySelector('#input').onchange = () => load_dropdown(
            document.querySelector('#input').value
        );
    } catch {}
});

function load_dropdown(input) {
    if (input != ""){
        api = document.querySelector('form').dataset.api;
        url = "https://www.alphavantage.co/query?function=SYMBOL_SEARCH&keywords="+input+"&apikey="+api;
        fetch(url)
        .then(response => response.json())
        .then(data => {
            console.log(data['bestMatches']);
            if (data['bestMatches'].length != 0){
                length = Math.min(5, data['bestMatches'].length);
                list = document.querySelector('#search-list');
                itemain = document.createElement("button");
                itemain.classList.add("list-group-item");

                for (i = 0; i <length; i++){
                    item = itemain.cloneNode(true);
                    symbol = data['bestMatches'][i]["1. symbol"];
                    name = data['bestMatches'][i]["2. name"];
                    item.dataset.symbol = symbol;
                    item.innerHTML = `${symbol}`+`(${name})`;
                    item.value = `${symbol}`;
                    document.querySelector('.list-group').appendChild(item);
                }
                sub_search_result();
            } else {
                alert("There are no good matches yet. Type something else . . .");

            }
        })
    }
    
}

function sub_search_result(){
    children = document.querySelector('#search-list').children;
    for (let child of children){
        child.onclick = () => {
            document.querySelector('#input').value = child.dataset.symbol;
        }
    }
}