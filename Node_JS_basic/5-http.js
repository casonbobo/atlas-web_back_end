// create a small HTTP server using the http module

const http = require('http');
const fs = require('fs');
const url = require('url');

// Function to read the CSV file asynchronously
const readFileAsync = ((filePath) => {
  return new Promise((resolve, reject) => {
    fs.readFile(filePath, 'utf8', (err, data) => {
      if (err) {
        reject(err);
      } else {
        resolve(data);
      }
    });
  });
});

// Function to handle requests and send responses
const handleRequest = async (req, res) => {
  const path = url.parse(req.url, true).pathname;

  if (path === '/') {
    res.writeHead(200, { 'Content-Type': 'text/plain' });
    res.end('Hello Holberton School!');
  } else if (path === '/students') {
    try {
      const filePath = './students.csv';
      const fileContent = await readFileAsync(filePath);
      const students = fileContent.split('\n').filter((line) => line.trim() !== '');
      res.writeHead(200, { 'Content-Type': 'text/plain' });
      res.write('This is the list of our students:\n');
      students.forEach((student) => res.write(`${student}\n`));
      res.end();
    } catch (err) {
      console.error(err);
      res.writeHead(500, { 'Content-Type': 'text/plain' });
      res.end('An error occurred while reading the file.');
    }
  } else {
    res.writeHead(404, { 'Content-Type': 'text/plain' });
    res.end('Not Found');
  }
};

// Create the HTTP server
const app = http.createServer(handleRequest);

// Export the app variable
module.exports = app;

// Start listening on port 1245
app.listen((1245), () => {
  console.log('Server is running on port 1245');
});
