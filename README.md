## Pygments-Heroku ##

http://pygments.herokuapp.com is an HTTP API for [Pygments](http://pygments.org/).

* Runs on [Heroku](http://heroku.com) (Cedar)
* Upgraded to use the latest dev build of **pygments**.
* Uses PIP to manage dependencies (as per the [Heroku Python Tutorial](http://devcenter.heroku.com/articles/python))

Inspired by [trevorturk/pygments](http://github.com/trevorturk/pygments).

## Usage ##

Issue a `HTTP POST` request to the service running at `http://pygments.herokuapp.com`

    **POST**: http://pygments.herokuapp.com
              PARAMS {:lang => "html", :code => "<h1>Hello World</h1>"}

The **response** body will contain the *pygmentized* HTML. 

## Examples

### curl

    curl --data "lang=html&code=<h1>Hello World</h1>" http://pygments.herokuapp.com

### Ruby

    require 'net/http'
    require 'uri'

    lang = 'python'
    code = 'print "Hello World"'

    request = Net::HTTP.post_form(URI.parse('http://pygments.appspot.com/'), {'lang'=>lang, 'code'=>code})
    puts request.body


## License

MIT License. Copyright 2011 Rumble Labs Ltd. [rumblelabs.com](http://rumblelabs.com)