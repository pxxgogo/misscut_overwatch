let model_id = -1;

$(document).ready(function () {
    bsCustomFileInput.init();
    get_text();
    $("#submit-btn").click(function () {
        Swal.fire({
            title: '您确定要提交结果吗？',
            text: "提交后将会继续切到下一段话",
            icon: 'info',
            showCancelButton: true,
            confirmButtonText: '继续',
            cancelButtonText: "取消",
        }).then((result) => {
            if (result.value) {
                next_text();
            }
        })
    })

})

function get_text() {
    const username = $("#username").html();
    $.ajax({ // 提交文本，处理json
        type: 'post',
        url: "/text/get_text",
        data: {'username': username},
        datatype: "json",
        beforeSend: function () {
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
                $("#template-panel").text(response.text);
                $("#input-panel").text("");
                model_id = response.model_id
            } else {
                Swal.close()
                Swal.fire("服务器错误", "请稍后再试，或联系conviction.p@gmail.com。感谢您的配合！", 'error');
            }
        },
        error: function () {
            Swal.close()
            Swal.fire("服务器错误", "请稍后再试，或联系conviction.p@gmail.com。感谢您的配合！", 'error');
        },
        timeout: 10000000,
    });
}

function next_text() {
    const username = $("#username").html();
    const ret_content = $("#input-panel").get(0).innerText;
    console.log(ret_content);
    $.ajax({ // 提交文本，处理json
        type: 'post',
        url: "/text/next_text",
        data: {'username': username, "model_id": model_id, "ret_content": ret_content},
        datatype: "json",
        beforeSend: function () {
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
                $("#template-panel").text(response.text);
                $("#input-panel").text("");
                model_id = response.model_id
            } else {
                Swal.close()
                Swal.fire("服务器错误", "请稍后再试，或联系conviction.p@gmail.com。感谢您的配合！", 'error');
            }
        },
        error: function () {
            Swal.close()
            Swal.fire("服务器错误", "请稍后再试，或联系conviction.p@gmail.com。感谢您的配合！", 'error');
        },
        timeout: 10000000,
    });
}

function paste_text(e) {
    e.preventDefault();
}