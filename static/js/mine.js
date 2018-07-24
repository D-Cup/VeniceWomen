function upload(file) {
    // 上传文件
    var xhr = new XMLHttpRequest();
    xhr.open('post', '/app/upload/', true);
    xhr.onload = function (ev) {
        if(xhr.status == 200 && xhr.readyState == 4){
            console.log(xhr.responseText);
            data = JSON.parse(xhr.responseText);
            console.log(data);
            if(data.state == 'ok'){
                $('#userImg').attr('src', '/static/'+data.path);
                alert('头像更新成功!');
            }
        }
    };
    var formdata = new FormData();
    formdata.append('img', file);
    xhr.send(formdata);
}