//node js express 로 서버
var express = require('express');
var app = express();
var routerEmp=require('./myrouter');
app.use('/emp', routerEmp);

//reload 테스트를 위해 추가
app.listen(3000, function(){
    console.log('read Oh!');
});