var app = require('express')();
var http = require('http').createServer(app);
var io = require('socket.io')(http);

var p = [];

app.get('/', function(req, res) {
    res.sendfile(__dirname + '/web2.html');
});

app.get('/clouds_blur.png', function(req, res) {
    res.sendfile(__dirname + '/clouds_blur.png');
});

app.get('/update', function(req, res) {
    for (var i = 0; i < 4; i++) {
        p[i] = (Math.random()*10000)%100;
        io.sockets.emit('broadcast_' + i, { message: p[i]});
    }
});

app.get('/jquery-3.4.1.min.js', function(req, res) {
    res.sendfile(__dirname + '/jquery-3.4.1.min.js');
});

app.post("/post", function (req, res) {
    console.log(req.body['user_id']);
    console.log(req.body['sleep_score']);
});

io.on('connection', function(socket) {
    console.log("User connected");
    socket.broadcast.emit('broadcast', 'Test');
}) 

http.listen(8000, function() {
    console.log("Listening on port 8000");
});
