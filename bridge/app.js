const portStr = "/dev/tty.usbmodemxxxx";

const SerialPort = require('serialport');
const port = new SerialPort(portStr,{baudRate: 9600});

function writeData(str){
  port.write(str+'\r');
}

const WebSocketServer = require('ws').Server;
const wss = new WebSocketServer({port: 3030}); 

wss.on('connection', function (ws) {
  ws.on('message', function (message,flags) {
    console.log("val: "+message);
    writeData(message);
  });
});

