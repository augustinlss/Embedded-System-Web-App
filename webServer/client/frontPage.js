import React from 'react';
const axios = require('axios');
const { render } = require('ejs');
const url = 'http://131.155.192.194:3000/call-function'

function MyComponent() {
  return (
    <div>
      <h1>Hello from React!</h1>
      <p>This is a React component rendered on the server side.</p>
    </div>
  );
}
export default MyComponent

function makePostRequest() {
    // axios.post(url, {
    //     functionName: "",
    // })
    //     .then(function (res){
    //     })
    //     .catch(function (error) {
    //         // Handle the error
    //         console.error(error);
    //     });
    
    
}

setInterval(makePostRequest, 1000);