var app = require('express')();
var http = require('http').createServer(app);
var io = require('socket.io')(http);

app.get('/', function(req, res) {
    res.sendfile(__dirname + '/index.html');
});

io.on('connection', function(socket) {
    console.log("User connected");
    var get_
}) 

http.listen(8000, function() {
    console.log("Listening on port 3000");
});
