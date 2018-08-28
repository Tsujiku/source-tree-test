//node js express 로 서버
var express = require('express');
var app = express();
app.set('view engine', 'ejs');
app.set('views', __dirname+'/view');
app.get('/', (req,res)=>{
    //res.send('hello express');
    res.render('index.ejs');
});

// 원본
// app.listen(3000);

//emp/:id에서 '/'없애 보기
//돌리고 결과 확인하기
app.get('/emp/:id', (req, res)=>{
var id = req.params.id;
var result={
    id: id,
    name: 'gg'
};

res.send(result);
});

//reload 테스트를 위해 추가
app.listen(3000, function(){
    console.log('read Oh!');
});