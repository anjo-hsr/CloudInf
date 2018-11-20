const express = require('express');
const router = express.Router();
const request = require('request');


const api_url = 'http://' + process.env.API_HOST + '/api/status';

/* GET home page. */
router.get('/', function(req, res, next) {
  request(
    {
      method: 'GET',
      url: api_url,
      json: true
    },
    function (error, response, body) {
      if (error || response.statusCode !== 200) {
        console.log("Status vom api backend war: " + error)
        return res.status(500).send('error running request to ' + api_url);
      } else {
        res.render('index', {
          title: 'CloudInf' ,
          request_uuid: body.request_uuid,
          time: body.time
        });
      }
    }
  );
});

module.exports = router;
