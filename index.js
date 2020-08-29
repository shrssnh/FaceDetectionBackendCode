const express = require('express')
const fs = require('fs')
const {spawn} = require('child_process');
const app = express()
const port = 5000
var bodyParser = require('body-parser')

// app.use(express.bodyParser());
// app.configure(function(){
  app.use(bodyParser({limit: '200mb'}));
 // });
// app.use(express.json());
app.get('/', (req, res) => {
 
 var dataToSend;
 // spawn new child process to call the python script
 
 // collect data from script
 python.stdout.on('data', function (data) {
  console.log('Pipe data from python script ...');
  dataToSend = data.toString();
 });
 // in close event we are sure that stream from child process is closed
 python.on('close', (code) => {
 console.log(`child process close all stdio with code ${code}`);
 // send data to browser
 res.send(dataToSend)
 });

})

app.post('/saveImage',function(req,res){
	const base64Data = (req.body.photo.replace(/^data:image\/png;base64,/, ""));

	 fs.writeFile("image.png", base64Data, 'base64', function(err) {
            if(err){
               console.log(err);
             }
        });
	 const python = spawn('python', ['code.py']);
	 var dataToSend;
	 python.stdout.on('data', function (data) {
	 	dataToSend = data.toString();
	 	});
	  python.on('close', (code) => {
 	console.log(`child process close all stdio with code ${code}`);

	 console.log(dataToSend)
	 res.send(dataToSend);
	});
});
app.listen(port, () => console.log(`Example app listening on port 
${port}!`))