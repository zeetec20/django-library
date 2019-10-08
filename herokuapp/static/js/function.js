function refreshAjaxInterval(time) {
    return setInterval(() => {
        $.ajax({
            type: 'GET',
            url: '/',
            data: {
    
            },
            success: function (returnData) {
                $('.list').html(returnData);
            }
        });

    }, time);
}

function editBook() {
    
}