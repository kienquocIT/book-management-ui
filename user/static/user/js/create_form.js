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
            let data = {
                username: $("#username_input").val(),
                email: $("#email_input").val(),
                password: $("#password_input").val(),
                first_name: $("#first_name_input").val(),
                last_name: $("#last_name_input").val(),
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
                error: function (xhr) {
                    alert('Create user fail!');
                    console.log(xhr.responseText);
                }
            });
        }
    });
});