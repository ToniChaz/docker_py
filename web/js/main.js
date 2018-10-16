(function (w, $) {
    $(function () {
        $.ajax('/api')
            .done(function (response) {
                $('#visitTimes').html(response)
            })
            .fail(function (error) {
                console.error(error)
            })
    })
})(window, jQuery)
