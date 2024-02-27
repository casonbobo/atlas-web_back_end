const fs = require('fs').promises;

async function countStudents(path) {
  try {
    const data = await fs.readFile(path, 'utf8');
    const lines = data.split('\n').filter(line => (line.trim() !== '')); // Filter out empty lines
    const fields = lines[0].split(','); // Assuming the first line contains field names
    const studentData = lines.slice(1); // Skip the header line

    let totalStudents = 0;
    console.log(`Number of students: ${studentData.length}`);

    fields.forEach((field, index) => {
      const studentsInField = studentData.filter(line => (line.split(',')[index]).length);
      const studentNames = studentData.filter(line => (line.split(',')[index])).map(line => (line.split(',')[0]));
      console.log(`Number of students in ${field}: ${studentsInField}. List: ${studentNames.join(', ')}`);
      totalStudents += studentsInField;
    });

    return totalStudents;
  } catch (error) {
    throw new Error('Cannot load the database');
  }
}

module.exports = countStudents;
