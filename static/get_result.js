$("#dataform").submit(function (event) {
    event.preventDefault();
        $.ajax({
            url: window.location.pathname,
            type: 'POST',
            data: new FormData(this),
            success: function (data) {
                let img = $('<img id="result_img">');
                img.attr('src', data);
                img.appendTo('#result');
            },
            error: (data) => alert(data),
            cache: false,
            contentType: false,
            processData: false
        }
    )
});
