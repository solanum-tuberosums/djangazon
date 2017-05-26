# Djangazon!! Bangazon on Django
[![standard-readme compliant](https://img.shields.io/badge/readme%20style-standard-brightgreen.svg?style=flat-square)](https://github.com/RichardLitt/standard-readme)

A django webapp where users can buy and sell products!

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
Setting up the database:

```
python manage.py builddb
```
Run project in browser:

```
python manage.py runserver
```



## Usage
Djangazon is Bangazon's e-commerce website powered by Python and Django. Djangazon gives its users the ability to buy and sell products.

#### Registered users can:
* Sell Products
* Browse All Products
* Browse 20 Most Recently Added Products
* Browse Products by Category
* Add Multiple Payment Types
* Add Products to a (persistent) Shopping Cart
* Logout

#### Users that are _not_ registered can:
* Sign Up
* Browse All Products
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

Small note: If editing the Readme, please conform to the [standard-readme](https://github.com/RichardLitt/standard-readme) specification.

## Credits
Project Manager:
  - [Jurnell Cockhren](https://github.com/jcockhren)

API Build Contributors:
  * [Jeremy Bakker](https://github.com/JeremyBakker)
  * [Blaise Roberts](https://github.com/BlaiseRoberts)
  * [Jessica Younker](https://github.com/jessica-younker)
  * [Will Sims](https://github.com/willsims14)

## License
[MIT © Potatoes](./LICENSE)