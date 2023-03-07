<!-- PROJECT TITLE -->
<br />
<div align="center">
    <h3 align="center">Finance</h3>
    <p align="center">
        A Stock Investment Simulator
        <br />
    </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#authentication">Authentication</a></li>
        <li><a href="#home-page">Home Page</a></li>
        <li><a href="#profile">Profile</a></li>
        <li><a href="#watchlist">Watchlist</a></li>
        <li><a href="#history">History</a></li>
        <li><a href="#search-page">Search Page</a></li>
        <li><a href="#stock-page">Stock Page</a></li>
        <li><a href="#company-page">Company Page</a></li>
      </ul>
    </li>
    <li><a href="#file-structure">File Structure</a></li>
    <li>
      <a href="#complexity">Complexity</a>
    </li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

The idea of an investment simulator comes from my interdisciplinary study in finance course. I hope to build such a web app that is more user-friendly and can help them practice their investment skills with real time data.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



### Built With

* [![VSCode][VSCode.com]][VSCode-url]
* [![Django][Django.com]][Django-url]
* [![SQLite][SQLite.com]][SQLite-url]
* [![HTML5][HTML5.com]][HTML5-url]
* [![JavaScript][JavaScript.com]][JavaScript-url]
* [![Python][Python.com]][Python-url]
* [![Chart][Chart.js]][Chart-url]
* [![Bootstrap][Bootstrap.com]][Bootstrap-url]
* [![Alphavantage][Alphavantage.com]][Alphavantage-url]

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started

### Authentication

* If new to the site, website would take you to the login page.
    [![login-screenshot][login]](#authentication)
    * Click the link on the bottom and register yourself with all fields filled.
    [![register-screenshot][register]](#authentication)
    * Submit the form and you will be taken to the home page.

### Home Page

* This page shows the details about your account like your email and your username.
    [![home-page-screenshot][home-page]](#home-page)
    * The button in the right-bottom corner would take you to the side bar.
    [![sidebar-screenshot][sidebar]](#home-page)

### Profile

* Click on profile link in the sidebar to go to the profile page.
    [![profile-screenshot][profile]](#profile)
	* The title of quote names shown in blue would take you to the stock page.

### Watchlist

* Click the watchlist link in the sidebar to go to the watchlist page.
* Every page of watchlist would show five stocks you previously watched.
* To move to the next page, scroll to the bottom of the page and click next or the page number.
* If the button is shown in grey, there does not exist another page of such.

### History

* Click the history link in the sidebar to go to the history page.
* This page shows all transactions you have made in this account, including purchasing shares and selling shares.
* The same pagination is implemented.

### Search Page

* The search link is slightly different from watchlist and history.
* Once you click onto it, there would be two options shown.
[![search-sidebar-screenshot][search-sidebar]](#search-page)
* For each option, the page below will be displayed.
[![search-screenshot][search]](#search-page)
* Enter the quote desired, and click the search button. That will lead you to the stock or company page.
	* If the quote-related stock or company does not exist. You will be taken back to the search page.
* If you do not know the specific quote to search for, type in some related words and try the matching function.
[![search-match-screenshot][search-match]](#search-page)
	* Click on the quote you are looking for, and the input field would be filled with the quote. Click the search button.

### Stock Page

* You would be taken to the stock page through search page.
[![stock-screenshot][stock]](#stock-page)
* It displays the basic information about the stock under the chart.
* On the top-right corner is the toolbar of watch and purchase.
	* If already watched or purchased the stock, the button would be changed to *is wached* and a sell button would appear respectively.
	* Click the time period button, and change the value to see a bar graph of lows and highs per time period.
	* The company button would direct you to the company page

### Company Page

* You can navigate to this page through either search or stock page.
[![company-screenshot][company]](#company-page)
* If the company related to the stock does not exist, you would see a message on screen instead.
* To go back to the stock page, click the *stock details* button.


<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- FILE STRUCTURE -->
## File Structure

Below is a list of files and folders created by me. Click on them to see details.

<details>
  <summary>File Navigation</summary>
  <ul>
    <details>
      <summary><a href="#diet">mystocks</a></summary>
      <ul>
        <details>
          <summary><a href="#static">static</a></summary>
          <ul>
            <li><a href="#profile-js">profile.js</a></li>
            <li><a href="#search-js">search.js</a></li>
            <li><a href="#sell-js">sell.js</a></li>
            <li><a href="#share-js">share.js</a></li>
            <li><a href="#stock-js">stock.js</a></li>
          </ul>
        </details>
        <details>
          <summary><a href="#templates">templates</a></summary>
          <ul>
            <li><a href="#company-html">company.html</a></li>
            <li><a href="#history-html">history.html</a></li>
            <li><a href="#home-html">home.html</a></li>
            <li><a href="#layout-html">layout.html</a></li>
            <li><a href="#login-html">login.html</a></li>
            <li><a href="#profile-html">profile.html</a></li>
            <li><a href="#register-html">register.html</a></li>
            <li><a href="#search-html">search.html</a></li>
            <li><a href="#sell-html">sell.html</a></li>
            <li><a href="#share-html">share.html</a></li>
            <li><a href="#stock-html">stock.html</a></li>
            <li><a href="#watchlist-html">watchlist.html</a></li>
          </ul>
        </details>
        <li><a href="#models">models</a></li>
        <li><a href="#urls">urls</a></li>
        <li><a href="#views">views</a></li>
      </ul>
    </details>
  </ul>
</details>

### mystocks

The folder that contains all files of mystocks application

#### static

The folder that contains all static files for mystocks

###### [profile.js](/mystocks/static/mystocks/profile.js)
The JavaScript file attached to profile.html

```sh
document.addEventListener('DOMContentLoaded', () => {
    load_chart();
});

function load_chart()
```
This function takes the values in the table in the profile html and then turns them into two pie charts - one showing the number of shares hold and another showing the amount of money paid.

```sh
document.addEventListener('DOMContentLoaded', () => {
    load_link();
});

function load_link()
```
This function assigns each quote name a link towards its stock page.

###### [search.js](/mystocks/static/mystocks/search.js)
The JavaScript file attached to search.html

```sh
document.addEventListener('DOMContentLoaded', () => {
    try {
        document.querySelector('#input').onchange = () => load_dropdown(
            document.querySelector('#input').value
        );
    } catch {}
});

function load_dropdown(input)
```
This function is called when the form input is onchange. If the input value is not empty, a link would be fetched to alpha vantage api database to get the best five matches or less. The result would be shown as list items under the input form.

```sh
function load_dropdown(input) {
	// Something
	sub_search_result();
	// Something
}

function sub_search_result()
```
When a list item is clicked, the function is called and the input would be substituted into the value of the item.

###### [sell.js](/mystocks/static/mystocks/sell.js)
The JavaScript file attached to sell.html

```sh
document.addEventListener('DOMContentLoaded', () => {
    document.querySelector('#submit').disabled = true;
    document.querySelector('#sharenumber').onchange = () => calculate_total(
        document.querySelector('#sharenumber').value
    );
});

function calculate_total(input)
```
When the number of shares to sell in the form is changed, this function checks for the validity, calculates the amount that would be earned using the up-to-date price, and, if valid, enables the button to submit the form.

###### [share.js](/mystocks/static/mystocks/share.js)
The JavaScript file attached to share.html

```sh
document.addEventListener('DOMContentLoaded', () => {
    document.querySelector('#sharenumber').onchange = () => calculate_share(
        document.querySelector('#sharenumber').value
    );
    document.querySelector('#submit').disabled = true;
});

function calculate_share(number)
```
This function gives a similar response to its html file but in a different method. Instead of using the data hidden in html, it uses fetching to react with the api and then gets the current price.

###### [stock.js](/mystocks/static/mystocks/stock.js)
This JavaScript file is attached to stock.html

```sh
document.addEventListener("DOMContentLoaded", function() {
    document.querySelector('.tool').onclick = () => watch_stock(
        (document.querySelector('.tool').dataset.watch == 'false')
    )

    if (document.querySelector('.tool').dataset.watch == 'false') document.querySelector('.tool').innerHTML = "Watch";
    else document.querySelector('.tool').innerHTML = "Is Watched";
});

function watch_stock(watch)
```
This function takes a boolean argument that works as a flag identifying if the stock is watched or not. It acts as a onclick function for the *watch* button.

```sh
document.addEventListener("DOMContentLoaded", function() {
    document.querySelector('select').onchange = () => load_graph(
        document.querySelector('select').value
    );
});

function load_graph(time)
```
The function loads the bar graph when the time period is changed. While the document is initialized, the graph would be initialized with empty value sets. When the button value is changed, fetching is used to retrieve the historical data related to the stock and re-applied to the canvas.

#### templates

The folder that contains all HTML templates for mystocks

###### [company.html](/mystocks/templates/mystocks/company.html)
Contains information related to a particular company in cards

###### [history.html](/mystocks/templates/mystocks/history.html)
Contains cards of transaction records and a pagination of five transactions each

###### [home.html](/mystocks/templates/mystocks/home.html)
Contains a heading of welcome message, a unordered list of username and email with a link to log out

###### [layout.html](/mystocks/templates/mystocks/layout.html)
Contains all the general stylesheets like boostrap and js files together with a button fixed on the bottom of screen and a offcanvas sidebar related to the button

###### [login.html](/mystocks/templates/mystocks/login.html)
Contains a form of username, password, and a submit button

###### [profile.html](/mystocks/templates/mystocks/profile.html)
Contains two charts regarding number of shares held and amount of money paid. Below is a table of the same data

###### [register.html](/mystocks/templates/mystocks/register.html)
Contains a form of username, email, two password fields to double check the password, a submit button, and a link to log in

###### [search.html](/mystocks/templates/mystocks/search.html)
Contains a input field and a list of best matches result that would be filled by the js file attached

###### [sell.html](/mystocks/templates/mystocks/sell.html)
Contains a card regarding the share to sell, and a form with fields of number of shares and a submit button together with invisible price and form-text fields

###### [share.html](/mystocks/templates/mystocks/share.html)
Contains a form with fields of quote, number of shares, hidden price and form-text, and a submit button. A chart of historical trend regarding the stock would implemented by the js file attached, and a table with stock info like highs and lows would be filled with data from the backend

###### [stock.html](/mystocks/templates/mystocks/stock.html)
Contains a toolbar of watch, company, purchse, sell (if purchased), and a time-period select field

###### [watchlist.html](/mystocks/templates/mystocks/watchlist.html)
Contains cards regarding the stocks that are watched and a pagination on the bottom

#### [models.py](/mystocks/models.py)
There are five classes created. For all the classes below, default primary keys of id would not be mentioned. Repetitive fields will not have their details mentioned.

<mark>User class</mark>
The standard user class as a child of django user model

<mark>Watch class</mark>
The class used to fill the watchlist file. Contains four fields:

* *user*: an integer field of user id
* *quote*: a char field with quote name in uppercase
* *company*: a char field of the company related to the stock
* *first_created*: a date-time field that is automatically created with the model is created

<mark>Purchase class</mark>
The class of purchase transactions. Contains six fields:

* *user*
* *quote*
* *first_created*
* *number*: an integer field of number of shares purchase
* *price*: a decimal field containing individual prices when purchased in two decimal places
* *label*: a char field always containing value of *bought*, used for categorization by the backend for history file

<mark>Sell class</mark>
The class of sell transactions. Contains six fields:

* *user*
* *quote*
* *first_created*
* *number*
* *price*
* *label*: a char field always containing value of *sold*, used for categorization by the backend for history file

<mark>Share class</mark>
The class of total shares owned per stock. Contains five fields:

* *user*
* *quote*
* *numberTotal*: an integer field of number of shares owned in total for a particular stock
* *paidTotal*: a decimal field with two decimal places of total amount of money paid to get all shares currently owned for the stock
* *earnedTotal*: a decimal field with two decimal places of total amount of money earned after selling some of the shares owned

#### [urls.py](/mystocks/urls.py)
There are thirteen routes in total:

```sh
path("", views.home, name='home'),
```
The route above is used as default when users open up the app url, log or register them in, and after record some intaks.

```sh
path('login', views.login_view, name='login'),
path('logout', views.logout_view, name='logout'),
path('register', views.register, name='register'),
```
The three paths above are used for the authentication system.

```sh
path("watchlist", views.watchlist, name="watchlist"),
path("profile", views.profile, name="profile"),
path("history", views.history, name="history"),
```
This three routes above lead the user to watchlist, profile, and history pages respectively with no additional variables but user ids

```sh
path("share/<str:quote>", views.share, name="share"),
path("sell/<str:quote>", views.sell, name="sell"),
path("search/<str:category>", views.search, name="search"),
path("stock/<str:quote>", views.stock, name="stock"),
path("company/<str:quote>", views.company, name="company"),
```
The first path is used when users purchase shares and the second when selling. The third is used for company or stock as two different categories. The fourth is the stock page route with a particular stock quote. The last is a company page route with the stock name related as a variable.

```sh
path("stock/<str:quote>/watch/<int:is_watched>", views.watch, name="watch"),
```
The route aboves serves as a special API route which takes two variables used to add the stock to watchlist or delete the stock from watchlist. The first variable is passed from the backend and stored in the html as a field, the second is determined when the watch button is clicked by the JavaScript file.

#### [views.py](/mystocks/views.py)

| Function Name | Request Method | Parameters | Return Value | Description |
| --- | --- | --- | --- | --- | --- |
| home | GET | request | render home page if authenticated, login page otherwise ||
| history | GET | request | render history page ||
| watchlist | GET | request | render watchlist page ||
| watch | GET | request, quote, is_watched | return Json Response | create watch objects or delete watch objects |
| stock | GET | request, quote | render stock page | generate stock info using api |
| sell | GET | request, quote | render sell page ||
|| POST | | redirect to profile page | deal with purchase transactions |
| share | GET | request, quote | render share page ||
|| POST || redirect to profile page | deal with sell transactions |
| search | GET | request, category | render search page ||
|| POST || render search if stock does not exist, redirect to company or stock otherwise depending on category argument ||
| company | GET | request, quote | render company page ||
| profile | GET | request | render profile page ||
| register_view | POST | request | register page if input invalid, home page otherwise ||
| | GET | | render register page | |
| login_view | POST | request | render home page if input valid, login page otherwise ||
| | GET | | render login page | |
| logout_view | GET | request | render login page ||

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- COMPLEXITY -->
## Complexity
The project overall is very complex while working with tens of htmls and multiple related js files.

<ins>Some features:</ins>
* Pagination
* Fetching external api using according to user input
* Provide matches for uncompleted searching input

<ins># of models:</ins> 5
<ins># of js functions:</ins> 8
<ins># of html pages:</ins> 12
<ins># of urls:</ins> 13
<ins># of views:</ins> 13

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- MARKDOWN LINKS & IMAGES -->
[login]: mystocks/static/mystocks/images/login.png
[register]: mystocks/static/mystocks/images/register.png
[home-page]: mystocks/static/mystocks/images/home.png
[sidebar]: mystocks/static/mystocks/images/sidebar.png
[profile]: mystocks/static/mystocks/images/profile.png
[search-sidebar]: mystocks/static/mystocks/images/search-sidebar.png
[search-match]: mystocks/static/mystocks/images/search-match.png
[search]: mystocks/static/mystocks/images/search.png
[stock]: mystocks/static/mystocks/images/stock.png
[company]: mystocks/static/mystocks/images/company.png

[VSCode.com]: https://img.shields.io/badge/Visual%20Studio%20Code-0078d7.svg?style=for-the-badge&logo=visual-studio-code&logoColor=white
[VSCode-url]: https://code.visualstudio.com/docs
[Django.com]: https://img.shields.io/badge/django-%23092E20.svg?style=for-the-badge&logo=django&logoColor=white
[Django-url]: https://docs.djangoproject.com/en/4.1/
[SQLite.com]: https://img.shields.io/badge/sqlite-%2307405e.svg?style=for-the-badge&logo=sqlite&logoColor=white
[SQLite-url]: https://www.sqlite.org/index.html
[HTML5.com]: https://img.shields.io/badge/html5-%23E34F26.svg?style=for-the-badge&logo=html5&logoColor=white
[HTML5-url]: https://developer.mozilla.org/en-US/docs/Web/HTML
[JavaScript.com]: https://img.shields.io/badge/javascript-%23323330.svg?style=for-the-badge&logo=javascript&logoColor=%23F7DF1E
[JavaScript-url]: https://developer.mozilla.org/en-US/docs/Web/JavaScript
[Python.com]: https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54
[Python-url]: https://www.python.org/
[Chart.js]: https://img.shields.io/badge/chart.js-F5788D.svg?style=for-the-badge&logo=chart.js&logoColor=white
[Chart-url]: https://www.chartjs.org/
[Bootstrap.com]: https://img.shields.io/badge/Bootstrap-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white
[Bootstrap-url]: https://getbootstrap.com
[Alphavantage.com]: https://img.shields.io/badge/Alphavantage-42DCA3?style=for-the-badge&logo=alphavantage&logoColor=black
[Alphavantage-url]: https://www.alphavantage.co/documentation/