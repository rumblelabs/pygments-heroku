# pygments-heroku

[http://pygmentize.herokuapp.com](http://pygmentize.herokuapp.com) is an HTTP API for the syntax highligher [Pygments](http://pygments.org/).

* Runs on [Heroku](http://heroku.com) (Cedar)
* Uses **pygments** version **1.4**
* Uses PIP to manage dependencies (as per the [Heroku Python Tutorial](http://devcenter.heroku.com/articles/python))

## API

Issue a `HTTP POST` request to the service running at `http://pygmentize.herokuapp.com`

    **POST**: http://pygmentize.herokuapp.com
              PARAMS {:lang => "html", :code => "<h1>Hello World</h1>"}

The **response** body will contain the *pygmentized* HTML. 

### Examples

#### curl

    curl --data "lang=html&code=<h1>Hello World</h1>" http://pygmentize.herokuapp.com

#### Ruby

    require 'net/http'
    require 'uri'

    lang = 'python'
    code = 'print "Hello World"'

    request = Net::HTTP.post_form(URI.parse('http://pygmentize.herokuapp.com'), {'lang'=>lang, 'code'=>code})
    puts request.body

## Server

### Dependencies

    easy_install pip
    pip install virtualenv

### Usage

    git@github.com:rumblelabs/pygments-heroku.git
    cd heroku-pygments
    virtualenv --no-site-packages .
    source bin/activate
    bin/pip install -r requirements.txt
    python app.py

### Run on Heroku

    heroku create my-pygments-app --stack cedar
    git push heroku
    heroku open

## Credits

Inspired by [trevorturk/pygments](http://github.com/trevorturk/pygments).

## License

MIT License. Copyright 2011 Rumble Labs Ltd. [rumblelabs.com](http://rumblelabs.com)