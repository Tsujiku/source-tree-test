var fs = require('fs');
fs.readFile('./sample.txt', function(err, data) {
    if(err){
        console.log(err);
    }
    console.log(data);
});
console.log('end of file.');