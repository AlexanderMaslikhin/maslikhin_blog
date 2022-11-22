$("#imgfile").onchange(function() {
    $("#dataform").submit();
});

$("#dataform").submit(function (event) {
    event.preventDefault();
        $('#result').empty();
        $.ajax({
            url: window.location.pathname,
            type: 'POST',
            data: new FormData(this),
            success: function (data) {
                let img = $('<img id="result_img">');
                bytes_str = data.split('\'')[1]
                img.attr('src', 'data:image/jpeg;base64,' + bytes_str);
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
