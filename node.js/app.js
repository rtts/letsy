
/**
 * Module dependencies.
 */

var express = require('express')
  , routes = require('./routes')
  , user = require('./routes/user')
  , http = require('http')
  , path = require('path');


var pg = require('pg');
var connectionString = "pg://node:konijn@localhost/letsy";
var crypto = require('crypto');

var app = express();

app.configure(function(){
    app.set('port', process.env.PORT || 3000);
    app.set('views', __dirname + '/views');
    app.set('view engine', 'jade');
    app.use(express.favicon());
    app.use(express.logger('dev'));
    app.use(express.bodyParser());
    app.use(express.methodOverride());
    app.use(express.cookieParser('mijn geheime string'));
    app.use(express.session({key: 'session'}));
    app.use(app.router);
    app.use(express.static(path.join(__dirname, 'public')));
});

app.configure('development', function(){
  app.use(express.errorHandler());
});

//app.get('/', routes.index);
//app.get('/users', user.list);

function login(req, res) {
    var email_token = req.params.token;
    var user;

    pg.connect(connectionString, function(err, client, done) {
        client.query('SELECT * FROM users WHERE email_token = $1', [email_token], function(err, result) {
            var email = result.rows[0].email;
            done();
        });
    });

    // invalidate email token
    var login_token;
    // res.cookie('login_token', login_token),
}

app.get('/login/:token?', function(req, res){
    req.session.count = req.session.count || 0;
    var n = req.session.count++;
    res.cookie('koekje', 'van eigen deeg', {signed:true});
    res.send('viewed ' + n + ' times\n(token=' + req.params.token);
})

http.createServer(app).listen(app.get('port'), function(){
  console.log("Express server listening on port " + app.get('port'));
});
