$(function () {
    const code = $("INPUT#language_code").val();

    $("INPUT#btn_translate").click(function (event) {
        $.get('https://www.fourtonfish.com/hellosalut/hello/',
            { lang: code },
            function (data, textStatus, jqXHR) {
                $("DIV#hello").text(data.hello);
            }
        );
    });
});
