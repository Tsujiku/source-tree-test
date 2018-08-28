process.on('exit', function(){ //이벤트 핸들 함수
    console.log('callback exit event');
});

//process.emit('exit'); //이벤트 강제 호출
console.log('emd of file');
