$('input').focus(function () {
        $('#errMsg').text('')
    });
$(function () {
    $('#inputUsername').blur(function () {
        if (this.value.trim().length == 0) {
            $('#errMsg').text('用户名不能为空');
        }
    });
    $('#inputPassword').blur(function () {
        if (this.value.trim().length == 0) {
            $('#errMsg').text('密码不能为空');
        }
    });
});