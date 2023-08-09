const express = require('express');
const path = require('path');
const app = express();
const morgan = require('morgan');


app.use(function (error, req, res, next) {
  if (error.status === 400) {
    log.info(error.body);
    return res.send(400);
  }

  console.log(error);

});


app.use(express.json());
var cors = require('cors');
app.use(cors());


app.use(morgan("combined"));


/*
app.listen(3000, function () {
  console.log('listening on 3000')
}); 
*/

app.listen(4444, '0.0.0.0');

app.use(express.static(path.join(__dirname, '../frontend/build')));

app.get('/', function (req, res) {
  res.sendFile(path.join(__dirname, '../frontend/build/index.html'));
});

//이건 맨 아래에 놓을 것
app.get('*', function (req, res) {
  res.sendFile(path.join(__dirname, '../frontend/build/index.html'));
});