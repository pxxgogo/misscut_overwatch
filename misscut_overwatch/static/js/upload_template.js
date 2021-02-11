$(document).ready(function () {
    bsCustomFileInput.init();
    $("#submit-btn").click(function () {
        const text = $("#input-panel").get(0).innerText;
        $.ajax({ // 提交文本，处理json
            type: 'post',
            url: "/text/submit_text",
            data: {'text': text},
            datatype: "json",
            beforeSend: function () {
                $("#submit-btn").attr("disabled", true);
                Swal.fire({
                    title: '请稍候',
                    onBeforeOpen: () => {
                        Swal.showLoading()
                    },
                    allowOutsideClick: false,
                })
            },
            success: function (response) { // html元素动作，进度条……
                // 非常重要
                if (response.return_code === 0) {
                    Swal.close();
                    Swal.fire('上传成功', `可以找校对人员来生成测例啦`, 'success');
                    $("#input-panel").text("");
                } else {
                    Swal.close()
                    Swal.fire("服务器错误", "请稍后再试，或联系conviction.p@gmail.com。感谢您的配合！", 'error');
                }
                $("#submit-btn").attr("disabled", false);
            },
            error: function () {
                Swal.close()
                Swal.fire("服务器错误", "请稍后再试，或联系conviction.p@gmail.com。感谢您的配合！", 'error');
                $("#submit-btn").attr("disabled", false);
            },
            timeout: 10000000,
        });
    })
})

