//POST, body-parser
//node js express 로 서버
var express = require('express');
var app = express();
var router=express.Router();
var bodyParser = require('body-parser');
router.use(bodyParser.json());

var list=[];
var counter=0;

//restful
router.post('/', (req, res)=>{
    console.log(req.body.name);
    var name = req.body.name;
    var age =  req.body.age;
    let tempEmp={id:counter++, name:name, age:age};
    list.push(tempEmp);

    for(var emp in list){
        console.log(list[emp]);
    }

    res.send('post is okay');
});

//emp/:id에서 '/'없애 보기
//돌리고 결과 확인하기
router.get('/:id', (req, res)=>{
    var id = req.params.id;
    var result={
        id: id,
        name: 'gg'
    };
    res.send(result);
});

router.get('/', (req,res)=>{

});

module.exports = router;