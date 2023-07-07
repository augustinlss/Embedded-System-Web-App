//require dependencies
const express = require('express');
const { exec } = require('child_process');
const React = require('react');
const ReactDOMServer = require('react-dom');
const loader = require('./loadData.js');

const app = express();
const port = 3000;
var availableActivation = 0;
var toBinary;
let availableResult = false;

app.use(express.json());
app.use(express.static('public'));

const searchingForBlack = false;
const searchingForWhite = false;
let display = "undefined";


app.get('/', (req, res) => {
  // Render the React component to a string
  // const markup = ReactDOMServer.renderToString(React.createElement(MyComponent));

  // Send the rendered component as the response
  res.send(`
  <!DOCTYPE html>
  <html>
    <head>
        <meta charset="UTF-8" />
        <meta name="viewport" content="width=device-width, initial-scale=1.0" />
        <title>Example-1</title>
        <link rel="stylesheet" href="/style.css" />
        <link href="https://fonts.googleapis.com/css2?family=Alexandria:wght@700&family=Caveat:wght@500&family=Indie+Flower&family=Kanit:wght@300&family=M+PLUS+1p&family=Satisfy&display=swap" rel="stylesheet">
        
    </head>
    <main>
      <div class="home-landing">
          <img src="/landing.BKGRD.jpg" alt="" />
          <div class="landing-text">
              <h1>Initialize the robot!</h1>
              <p>Brought to you by the wonderful DBL group 1</p>
          </div>
      </div>
      <div class="section-testimony">
          <div class="testimony-text">
              <div class="info-text-title">
                  Controlling your robot just got
                  <span class='ut'> easier</span>
              </div>
              <div class="info-text-content">
                  This is where you can visualize important infomation concerning the robot, like the input that is being processed, and the necessary discs that are needed!
              </div>
          </div>
          <div class="info-display">
                <div class="title">
                    Input in process:
                </div> 
                <div class="value">
                    <h1 id='bin'>
                        ${toBinary}
                    </h1>
                </div>
                <div class="title">
                    Current iteration:
                </div> 
                <div class="value">
                    <h1>
                        ${display}
                    </h1>
                </div>
            </div>
      </div>
      
          
      
  </main>
  </html>
  `);
});



//Serial monitor keyword await on post request
app.post('/call-function', async (req, res) => {
    console.log('Received a POST request');

    const data = req.body;
    console.log(data)
    if (data.functionName === 'active') {

      startGR((err, result) => {
        if (err) {
          res.status(500).send('Error processing data');
        } else {
          display = "Computer vision AI active."
          // Send the result back as the response
          res.send(result);
          // res.render('template', {result});
        }
      });
    }else if (data.functionName === "0 color") {
      //Print Searching for white on HTML
      console.log("0 command");
      const searchingForBlack = false;
      const searchingForWhite = true;
      display = "Searching for White Disc.";
      res.send("0");
    }else if (data.functionName === "1 color"){
      //Print Searching for black
      console.log("1 command");
      const searchingForBlack = true;
      const searchingForWhite = false;
      display = "Searching for Black Disc.";
      res.send("1");
    }else if (data.functionName === "-1 color"){
      //Print searching for nothing
      const searchingForBlack = false;
      const searchingForWhite = false;
      display = "Program has completed, omitting incoming discs.";
      console.log("-1 command");
      res.send("-1");
    }else if (data.functionName === "init white"){
        //Print searching for nothing
        const searchingForBlack = false;
        const searchingForWhite = false;
        display = "Calibrating sensor for white discs.";
        toBinary = undefined;
        console.log("White Init");
        res.send("white init");
    }else if (data.functionName === "init black"){
        //Print searching for nothing
        const searchingForBlack = false;
        const searchingForWhite = false;
        display = "Calibrating sensor for black discs.";
        console.log("Black Init");
        res.send("black init");
    }else if(data.functionName === "retrieveData"){
      res.send(toBinary);
    }else { 
      res.status(400).send('Invalid function name');
    }
  });
app.listen(port, '192.168.142.59', () => {
  console.log(`Server running at http://192.168.142.59:${port}`);
});


function startGR(callback) {
  const command = 'python3 sender.py';
  exec(command, (error, stdout, stderr) => {
    if (error) {
      console.error(`Error executing Python script: ${error}`);
      return;
    }
    const finalOutput = parseInt(stdout);
    toBinary = parseInt(finalOutput).toString(2);
    if(toBinary.length < 4) {
      while(toBinary.length < 4) {
        toBinary = "0" + toBinary;
      }
    }
    console.log(toBinary);
    callback(null, toBinary);
    // displayToBinaryOnWebsite(toBinary);
  });
}

// function displayToBinaryOnWebsite(value) {
//   // Assuming you have an HTML element with id "binaryValue"
//   const binaryValueElement = document.getElementById('binaryValue');
//   binaryValueElement.innerText = value;
// }







