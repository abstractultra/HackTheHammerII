var app = require('express')();
var http = require('http').createServer(app);
var io = require('socket.io')(http);

var p = [];

app.get('/', function(req, res) {
    res.sendfile(__dirname + '/index.html');
});

app.get('/update', function(req, res) {
    for (var i = 0; i < 4; i++) {
        p[i] = (Math.random()*10000)%100;
        io.sockets.emit('broadcast_' + i, { message: p[i]});
    }
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
    console.log("Listening on port 3000");
});
