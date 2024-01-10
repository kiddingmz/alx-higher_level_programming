$(function () {
    const sayHelloByLanguage = () => {
        const code = $("INPUT#language_code").val();

        $.get('https://www.fourtonfish.com/hellosalut/hello/',
            { lang: code },
            function (data, textStatus, jqXHR) {
                $("DIV#hello").text(data.hello);
            }
        );
    };

    $("INPUT#btn_translate").click(function (event) {
       sayHelloByLanguage();
    });

    $("INPUT#language_code").keypress(function (event) {
        if (event.keyCode === 13) {
            sayHelloByLanguage();
            return false;
        }
    });
});
