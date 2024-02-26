// Using the db create a function countStud in the file 2

const fs = require('fs');

function countStudents(path) {
  if (!fs.existsSync(path)) {
    throw new Error('Cannot load the database');
  }

  const data = fs.readFileSync(path, 'utf8');
  const students = data.trim().split('\n').slice(1);
  const studentClasses = {};

  students.forEach((student) => {
    const [firstName,, , field] = student.split(',');
    if (!studentClasses[field]) studentClasses[field] = [];
    studentClasses[field].push(firstName);
  });

  const totalStudents = students.length;
  console.log(`Number of students: ${totalStudents}`);

  Object.entries(studentClasses).forEach(([field, names]) => {
    console.log(`Number of students in ${field}: ${names.length}. List: ${names.join(', ')}`);
  });
}

module.exports = countStudents;
