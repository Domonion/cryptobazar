<img src="ico-icon.jpeg" align="center"/>

<h1 align="center">ICO Framework on QuarkChain in sharded way</h1>
<p align="center">
  <a href="#key-features">Key Features</a> •
  <a href="#how-to-use">How To Use</a> •
  <a href="#credits">Credits</a> •
  <a href="#setting-up-your-own-ico-framework">Setting up your own ICO Framework</a> •
  <a href="#used-tenchologies">Used technologies</a>
</p>

## Key Features

* Fast and secure blockchain ICO framework
* Optimal implementation
  - with usage of newest technologies
  - client-server architecture with secure connection establishment
* Docker Container-based environment
* Completely standalone
  - no user-side installation required
  - no further setting after installation required
* User-friendly web interface
  - intuitive and understandable web form
  - innovative interface design
  - calming and relaxing interface colors
* Crossplatform
  - availaible on Linux, Max and Windows

## How to use

This is an ICO Framework for smart-contracts. It helps you to operate smart-contracts by selecting the type of cryptocurrency, the amount of tokens and dates of operations. Everything is operated on the server side, so the client side is not overloaded. 

Client-side has a responsive simple interface designed with most modern tendencies for the most comfortable use. Server side is operated by Django, with high-quality code and optimal blockchain algorythms of cryptocurrency operating.

### Installation guide

You should install Docker, run our container and just open your browser.

### Using the tool

Opening the page you will see simple (though yet functional) interface with web form of **seven fields**:

#### Name

_Type: string_
The name of the token for the sale (example: Bitcoin).

#### Abbreviation

_Type: string_
The abbreviation of the token name (example: BTC).

#### Amount of tokens

_Type: big integer_
The amount of tokens used for this sale. You can actualy put any 256-bit number in this `<input>` element, because many cryptocurrency types require large amount of tokens to reach the desired amount of money.

#### Sale start

_Type: date_
The date of the beginning of the sale. You can select the date from the webpage-integrated calendar, or you can type the date by keyboard if `DD.MM.YYYY` format, so anyone can choose the best option.
All the dates are further converted to UNIX format.

#### Sale duration

_Type: int_
The duration of the sale in days.

#### Purse address
Address of ICO starter's purse.

#### Creator percentage
Amount of award that will be given to ICO creator.

## Setting up your own ICO Framework

### Installation

Installation is fully managed by **Docker** itself. This installation guide is presented for **version 1.0.0 and later**. After donwnloading the source code just install the requirements and run the Docker in the source directory to set up the environment:

for docker:
```cmd
docker run domonion/cryptobazar:latest
```

for git:
```cmd
git clone github.com/Domonion/cryptobazar
pip3 install -r requirements.txt
python3 ./server/manage.py runserver
```

### Setting up

Actualy, you don't even need to have any further troubles with installation before using this **ICO Framework**. All dependencies from [requirements.txt] are managed by Docker and after the program is started, the connection with server is established automatically by Django.

### Using the tool

Open your browser on `<server-address>:<port>`, where `<server-address>` is actually where you have started the server using Docker and `<port>` is your set up port for connection. By default (if you didn't interfere with the source code itself) the port is set to `8000`.
After you've opened the page you should see that everything is working and you can start using the tool.

If you have any issues or troubles, please feel free to create an issue on [our github](https://github.com/Domonion/cryptobazar/issues) and contact the creators.

## Credits

Developed by **Jd42D3**, which is actualy
<p align="center">
  <a href="https://github.com/Domonion">Domonion</a> • 
  <a href="https://github.com/EgorGornak">EgorGornak</a> • 
  <a href="https://github.com/rbkn99 ">rbkn99</a> with the help from
  <a href="https://github.com/geranazavr555">geranazavr</a> • 
  <a href="https://github.com/doreshnikov">doreshnikov</a>
</p>

## Used tenchnologies

* [Python](https://python.org) with [Django](https://www.djangoproject.com)
  - for server part
* [JavaScript ECMA 5](https://www.javascript.com)
  - for user interface
* HTML5 + CSS with [Bootstrap](http://getbootstrap.com)
  - for beautiful responsive interface
* [Docker](https://www.docker.com)
  - for environment and dependencies management
  - `pip3` for dependencies management
