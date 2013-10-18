$(document).ready(function () {

    $(".deletePostBtn").click(function () {
        $("#deleteForm").toggle();
    });

    $("#deletePost").click(function () {
        var url = $(this).attr('data-target');
        var token = $("input[name=csrfmiddlewaretoken]").val();
        var redirect = $(this).attr('data-redirect');
        $.ajax({
            type: 'POST',
            url: url,
            data: { csrfmiddlewaretoken: token},
            success: function () {
                // We are unable to do anything about the autoredirect
                // performed by the browser before we receive it here
                // so there will be a "wasted" GET call
                window.location = redirect;
            }
        });

    });
});