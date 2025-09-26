$(document).ready(function () {
    let pk = getPkFromUrl()
    let url_detail = $("#update-form").attr('data-url').replace('0', pk)
    let url_redirect = $("#update-form").attr('data-url-redirect').replace('0', pk)
    let url_redirect_list = $("#update-form").attr('data-url-redirect').replace('/0', '')


    $.ajax({
        url: url_detail,
        method: 'GET',
        success: function (response) {
            $("input[name='username']").val(response?.['username'])
            $("input[name='email']").val(response?.['email'])
            $("input[name='first_name']").val(response?.['first_name'])
            $("input[name='last_name']").val(response?.['last_name'])
        },
        error: function (xhr) {
            alert('Get user fail!');
            console.log(xhr.responseText);
        }
    })

    $("#update-form").validate({
        submitHandler: function (form, event) {
            let data = {
                email: $("#email_input").val(),
                first_name: $("#first_name_input").val(),
                last_name: $("#last_name_input").val(),
            };

            $.ajax({
                url: url_detail,
                method: $(form).attr('data-method'),
                data: data,
                headers: {"X-CSRFToken": $('input[name="csrfmiddlewaretoken"]').val()},
                success: function (response) {
                    alert('Update success!');
                    window.location.replace(url_redirect)
                },
                error: function (xhr) {
                    alert('Update user fail!');
                    console.log(xhr.responseText);
                }
            });
        }
    });

    $("#btn-delete").on('click', function () {
        $.ajax({
            url: url_detail,
            method: 'DELETE',
            success: function (response) {
                alert('Delete user success')
                window.location.replace(url_redirect_list)
            },
            error: function (xhr) {
                alert('Delete user fail!');
                console.log(xhr.responseText);
            }
        });
    })
})

function getPkFromUrl() {
    let current_url = window.location.href
    let url_split = current_url.split('/')
    return url_split.at(url_split.length - 1)
}