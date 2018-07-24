var isSubmitable = true;

$(function () {
   $('input').focus(function () {
        $('#errMsg').text('')
    });
   $('#newPassword').blur(function () {
        if (this.value.trim().length == 0) {
            $('#errMsg').text('密码不能为空');
            isSubmitable = false;
            return
        }
    });
   $('#newPasswordAgain').blur(function () {
        var passwd1 = $('input[id=newPassword]').val();
        if (this.value.trim() != passwd1.trim()) {
            $('#errMsg').text('两次口令不相同！');
            isSubmitable = false;
            return
        }else {
            isSubmitable = true;
            return
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
    console.log('---check regist---');
}
