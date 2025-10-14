$(document).ready(function () {
    $("#create-form").validate({
        rules: {
            "username": {required: true, minlength: 3},
            "password": {required: true, minlength: 8},
            "re-password": {equalTo: "#password_input", minlength: 8}
        },
        messages: {
            "username": {
                required: "Bắt buộc nhập username",
                maxlength: "Hãy nhập tối đa 15 ký tự"
            },
            "password": {
                required: "Bắt buộc nhập password",
                minlength: "Hãy nhập ít nhất 8 ký tự"
            },
            "re-password": {
                equalTo: "Hai password phải giống nhau",
                minlength: "Hãy nhập ít nhất 8 ký tự"
            }
        },
        submitHandler: function (form, event) {
            let is_staff = false
            let staff_check = $("#is_staff_switch_check").prop('checked')

            let data = {
                username: $("#username_input").val(),
                email: $("#email_input").val(),
                password: $("#password_input").val(),
                first_name: $("#first_name_input").val(),
                last_name: $("#last_name_input").val(),
                is_staff: staff_check
            };


            $.ajax({
                url: $(form).attr('data-url'),
                method: $(form).attr('data-method'),
                data: data,
                headers: {"X-CSRFToken": $('input[name="csrfmiddlewaretoken"]').val()},
                success: function (response) {
                    alert('Create success!');
                    window.location.replace($(form).attr('data-url-redirect'))
                },
                error: function (xhr, status, error) {
                    console.log("Status:", status);
                    console.log("Error:", error);
                    console.log("Response JSON:", xhr.responseJSON);

                    const errorObj = xhr.responseJSON;

                    if (errorObj && Object.keys(errorObj).length > 0) {
                        let delay = 0;
                        Object.keys(errorObj).forEach(key => {
                            const message = `${errorObj[key][0]}`;
                            console.log(message);

                            setTimeout(() => {
                                displayToast(message, false);
                            }, delay);
                            delay += 1500;
                        });
                    } else {
                        displayToast("Lỗi không xác định!", false);
                    }
                }
            });
        }
    });

    function displayToast(message, is_success) {
        let toast = $("#toast")

        toast.attr('class', 'toast align-items-center text-light fw-bold border-0')

        if (is_success) {
            toast.addClass('bg-success')
        } else {
            toast.addClass('bg-danger')
        }

        $("#toast-body").text(message)

        let bsToast = new bootstrap.Toast(toast[0], {delay: 3000})
        bsToast.show()
    }
});