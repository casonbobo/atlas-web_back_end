// Create a small http sever using the http module

const http = require('http');

const app = http.createServer((res) => {
  res.writeHead(200, { 'Content-Type': 'text/plain' });
  res.end('Hello Holberton School!');
});

app.listen(1245);

module.exports = app;
