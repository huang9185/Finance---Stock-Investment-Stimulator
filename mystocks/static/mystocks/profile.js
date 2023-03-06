document.addEventListener('DOMContentLoaded', () => {
    load_chart();
    load_link();
});

function load_link() {
    rows = document.querySelector('tbody').children;
    for (let row of rows) {
        row.click = () => {
            window.location = row.children[0].children[0].href;
        }
    }
}

function load_chart() {
    amtchart = document.querySelector('canvas');
    volchart = document.querySelector('#volChart');
    rows = document.querySelector('tbody').children;
    labels = [];
    vols = [];
    prices = [];
    for (let row of rows) {
        quote = row.children[0].children[0].innerHTML;
        labels.push(quote);
        vol = row.children[1].innerHTML;
        price = row.children[2].innerHTML;
        vols.push(vol);
        prices.push(price);
    }

    data = {
        labels: labels,
        datasets: [{
            label: 'Profile by Amount Paid',
            data: prices,
            hoverOffset: 6
        }],
    }
    config = {
        type: 'doughnut',
        data: data,
        options: {
            plugins: {
                title: {
                    display: true,
                    text: 'Profile by Amount Paid',
                }
            }
        }
    };
    new Chart(amtchart, config);
    data = {
        labels: labels,
        datasets: [{
            label: 'Profile by # Shares',
            data: vols,
            hoverOffset: 6
        }],
    }
    config = {
        type: 'doughnut',
        data: data,
        options: {
            plugins: {
                title: {
                    display: true,
                    text: 'Profile by # Shares',
                }
            }
        }
    };
    new Chart(volchart, config);
}