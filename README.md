# Djangazon!! Bangazon on Django
[![standard-readme compliant](https://img.shields.io/badge/readme%20style-standard-brightgreen.svg?style=flat-square)](https://github.com/RichardLitt/standard-readme)

Djangazon is Bangazon's e-commerce website powered by Python and Django.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)   
- [Contribute](#contribute)
- [Credits](#credits)
- [License](#license)


### Prerequisites
Install [pip](https://packaging.python.org/installing/)

Install [Python 3.6](https://www.python.org/downloads/)

Install Django:
```
pip install django
```

## Installation
```
git clone https://github.com/solanum-tuberosums/djangazon.git
cd djangazon
```
Create and Seed the Database:

```
python manage.py builddb
```
Host a Server:

```
python manage.py runserver
```
Then, open your favorite internet browser and go to your [Local Host - port: 8000](http://localhost:8000/)


## Usage
In order to use all of the Bangazon website's features, users must create an account by clicking the "Register" button in the top left corner of the splash page.

#### Registered users can:
* Can Add Products to Sell
* Browse All Products
* Browse All Product Categories
* Browse 20 Most Recently Added Products
* Browse Products by Category
* Add and Delete Multiple Payment Types
* Add Products to or delete products from a Shopping Cart
* Logout

#### Users that are _not_ registered can:
* Sign Up
* Browse All Products
* Browse All Product Categories
* Browse Products by Category
* Browse 20 Most Recently Added Products


## Contribute
1. Fork it!
2. Create your feature branch:
```git checkout -b <new-feature-branch-name-here>```
3. Commit your changes:
```git commit -m 'Add some feature'```
4. Push to the branch:
```git push origin <new-feature-branch-name-here-too>```
5. Submit a pull request!

## Credits
Project Manager:
  - [Jurnell Cockhren](https://github.com/jcockhren)

API Build Contributors:
  * [Jeremy Bakker](https://github.com/JeremyBakker)
  * [Blaise Roberts](https://github.com/BlaiseRoberts)
  * [Jessica Younker](https://github.com/jessica-younker)
  * [Will Sims](https://github.com/willsims14)

## License
MIT © Potatoes