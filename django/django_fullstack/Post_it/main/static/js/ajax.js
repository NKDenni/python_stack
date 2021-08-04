$(document).ready(function () {
    $('form').submit(function (e) {
        // preventDefault stops the default action of the event (e) from being triggered.
        e.preventDefault();
        console.log("Form submitted but no HTTP request sent to server!");
        $.ajax({
            url: "/new_note", /* Where should this go? */
            method: "POST", /* Which HTTP verb? */
            data: $(this).serialize(), /* Any data to send along? */
            success: function (serverResponse) {
                $('#notes').prepend(serverResponse)
                console.log("Received this from server: ", serverResponse)/* What code should we run when the server responds? */
            }
        })
        $(this).trigger('reset')
    });
})