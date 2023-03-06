document.addEventListener("DOMContentLoaded", function() {
    document.querySelector('select').onchange = () => load_graph(
        document.querySelector('select').value
    );
    document.querySelector('.tool').onclick = () => watch_stock(
        (document.querySelector('.tool').dataset.watch == 'false')
    )
    load_graph("1D");
    if (document.querySelector('.tool').dataset.watch == 'false') document.querySelector('.tool').innerHTML = "Watch";
    else document.querySelector('.tool').innerHTML = "Is Watched";
});

function watch_stock(watch) {
    quote = document.querySelector('h1').innerHTML;

    if (watch == false) {
        num = 1;
        document.querySelector('.tool').innerHTML = "Watch";
        document.querySelector('.tool').dataset.watch = "false";
    } else {
        // Stock is not watched yet
        // Watch button is clicked
        num = 0;
        document.querySelector('.tool').innerHTML = "Is Watched";
        document.querySelector('.tool').dataset.watch = "true";
    }
    fetch(`/mystocks/stock/${quote}/watch/${num}`)
        .then(response => response.json())
        .then(data => {
            console.log(data);
        });
}
chart_initialized = false;
// functions not actually applied to elements
function load_graph(time) {
    quote = document.querySelector('h1').innerHTML;
    api = document.querySelector('h2').innerHTML;
    canvas = document.querySelector('canvas');
    if (chart_initialized == false){
        
        const datatmp = {
            labels: [],
            datasets: [
                {
                    label: 'Empty',
                    data: [],
                },
            ]
        };
        const config = {
            type: 'bar',
            data: datatmp,
        };
        barchart = new Chart(canvas, config);
        chart_initialized = true;
    } else
    barchart.destroy();

    if (time == "1D"){
        url = "https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol="+quote+"&interval=5min&apikey="+api;
        count = 100;
        category = "Time Series (5min)";
        label = "Low & High per 5 Min";
    }
    else if (time == "15D"){
        url = "https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol="+quote+"&outputsize=compact&apikey="+api;
        count = 15;
        category = "Time Series (Daily)";
        label = "Daily Low & High";
    }
    else if (time == "1M"){
        url = "https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol="+quote+"&outputsize=compact&apikey="+api;
        count = 30;
        category = "Time Series (Daily)";
        label = "Daily Low & High";
    }
    else if (time == "5M"){
        url = "https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol="+quote+"&outputsize=compact&apikey="+api;
        count = 100;
        category = "Time Series (Daily)";
        label = "Daily Low & High";
    }
    else if (time == "1Y"){
        url = "https://www.alphavantage.co/query?function=TIME_SERIES_MONTHLY&symbol="+quote+"&apikey="+api;
        count = 12;
        category = "Monthly Time Series";
        label = "Monthly Low & High";
    }
    else if (time == "5Y"){
        url = "https://www.alphavantage.co/query?function=TIME_SERIES_MONTHLY&symbol="+quote+"&apikey="+api;
        count = 60;
        category = "Monthly Time Series";
        label = "Monthly Low & High";
    }
    
    fetch(url)
    .then(response => response.json())
    .then(data => {
        console.log(data);
        const labels = Object.keys(data[category]).slice(0, 1+count).reverse();
        data_nums = [];
        low = "3. low";
        high = "2. high";
        let axis_low = 10000;
        let axis_high = 0;
        for (let i = 0; i < count; i++) {
            let lower_bound = parseFloat(data[category][labels[i]][high]);
            let higher_bound = parseFloat(data[category][labels[i]][low]);
            data_nums.push([lower_bound, higher_bound]);
            axis_low = Math.min(axis_low, lower_bound);
            axis_high = Math.max(axis_high, higher_bound);
        }
        difference = axis_high-axis_low;
        const datanew = {
            labels: labels,
            datasets: [
                {
                    label: label,
                    data: data_nums,
                },
            ]
        };
        const config = {
            type: 'bar',
            data: datanew,
            options: {
                responseive: true,
                plugins: {
                    title: {
                        display: false,
                    }
                },
                scales: {
                    y: {
                        min: axis_low-difference,
                        max: axis_high+difference
                    }
                }
            }
        };
        barchart = new Chart(canvas, config);
    });
    
    }