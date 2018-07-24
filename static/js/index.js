//获取滚动条当前的位置
function getScrollTop() {
    var scrollTop = 0;
    if (document.documentElement && document.documentElement.scrollTop) {
        scrollTop = document.documentElement.scrollTop;
    } else if (document.body) {
        scrollTop = document.body.scrollTop;
    }
    return scrollTop;
}
//获取当前可视范围的高度
function getClientHeight() {
    var clientHeight = 0;
    if (document.body.clientHeight && document.documentElement.clientHeight) {
        clientHeight = Math.min(document.body.clientHeight, document.documentElement.clientHeight);
    } else {
        clientHeight = Math.max(document.body.clientHeight, document.documentElement.clientHeight);
    }
    return clientHeight;
}
//获取文档完整的高度
function getScrollHeight() {
    return Math.max(document.body.scrollHeight, document.documentElement.scrollHeight);
}

//滚动事件触发
window.onscroll = function () {
    if (getScrollTop() + getClientHeight()+50 > getScrollHeight()) {
        console.log('下拉刷新了');
        //此处发起AJAX请求图片
        var xhr = new XMLHttpRequest();
        xhr.open('post', 'imagepath', true);
        xhr.onload = function (ev) {
            if (xhr.status == 200 && xhr.readyState == 4) {
                // console.log(xhr.responseText);
                data = JSON.parse(xhr.responseText);
                if (data.state == 'ok') {
                    $('#userImg').attr('src', 'imagepath' + data.path)
                }
            }
        };
        var formdata = new FormData();
        formdata.append('img', file);
        xhr.send(formdata);
    }
};