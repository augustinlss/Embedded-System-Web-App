const axios = require('axios');
const url = 'http://131.155.120.234:3000/'


function makePostRequest(){
    axios.get(url, {
        functionName: "retrieveData",
    })
        .then(function (res){
            // window.location.reload();
        })
        .catch(function (error) {
            // Handle the error
        });

}

setInterval(makePostRequest, 1000);
