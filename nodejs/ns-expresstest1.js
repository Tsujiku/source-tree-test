//node js express 로 서버
var express = require('express');
var app = express();
app.get('/', (req,res)=>{
    res.send('hello express');
});

// 원본
// app.listen(3000);

//reload 테스트를 위해 추가
app.listen(3000, function(){
    console.log('read Oh!');
});