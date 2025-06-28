const fs = require('fs');
let input = '';
process.stdin.on('data', chunk => input += chunk);
process.stdin.on('end', () => {
  const msg = JSON.parse(input);
  // Example transformation: wrap message
  const output = { wrapped: msg };
  process.stdout.write(JSON.stringify(output));
});
