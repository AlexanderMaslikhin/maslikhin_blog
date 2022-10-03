$("#dataform").submit(function (event) {
    event.preventDefault();
        $.ajax({
            url: window.location.pathname,
            type: 'POST',
            data: new FormData(this),
            success: function (data) {
                let img = $('<img id="result_img">');
                img.attr('src', 'data:image/jpeg;base64,' + btoa(data));
                img.appendTo('#result');
            },
            error: function(data) {
                let resp = $(data.responseText)
                resp.appendTo('#result')
            },
            cache: false,
            contentType: false,
            processData: false
        }
    )
});
