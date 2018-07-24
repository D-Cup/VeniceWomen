var isSubmitable = true;

$(function () {
    $('input').focus(function () {
        $('#errMsg').text('')
    });
    $('#inputUsername').blur(function () {
        if (this.value.trim().length == 0) {
            $('#errMsg').text('用户名不能为空');
            isSubmitable = false;
            return
        }
    });
    $('#inputPassword').blur(function () {
        if (this.value.trim().length == 0) {
            $('#errMsg').text('密码不能为空');
            isSubmitable = false;
            return
        }
    });
    $('#inputPassword2').blur(function () {
        var passwd1 = $('input[name=password]').val();
        if (this.value.trim() != passwd1.trim()) {
            $('#errMsg').text('两次口令不相同！');
            isSubmitable = false;
            return
        }else {
            isSubmitable = true;
            return
        }
    });
    $('#inputEmail').blur(function () {
        if (this.value.trim().length == 0) {
            $('#errMsg').text('邮箱不能为空');
            isSubmitable = false;
            return
        }
    });
    $('#inputPhone').blur(function () {
        if (this.value.trim().length == 0) {
            $('#errMsg').text('电话不能为空');
            isSubmitable = false;
            // alert($('#errMsg').text);
            return
        } else if (!/1[3-9]\d{9}/.test(this.value.trim())) {
            $('#errMsg').text('手机号无效');
            alert('手机号无效');
            isSubmitable = false;
            return
        }else {
            isSubmitable = true;
        }
    });
});


function submitForm() {
    var inputs = $('input');
    // 验证是否为空的
    for (var i = 0; i < inputs.length; i++) {
        var input = inputs.get(i);
        if ($(input).val().trim() == '') {
            $(input).parent().addClass('has-error');
            $(input).parent().next().fadeIn();
            isSubmitable = false;
            return
        } else {
            $(input).parent().removeClass('has-error');
            $(input).parent().next().fadeOut()
        }
    }

    if (isSubmitable)
        $('form').submit();  // 提交注册
    console.log('--check regist----');
}


