//POST, body-parser
//node js express 로 서버
var express = require('express');
var app = express();

//post기 때문에 bodyParser사용
var bodyParser = require('body-parser');
app.use(bodyParser.json());


app.set('view engine', 'ejs');
app.set('views', __dirname+'/view');

//restful
app.post('/emp', (req, res)=>{
    console.log(req.body.name);
    res.send('post is okay');
});