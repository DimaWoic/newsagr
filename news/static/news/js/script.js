
    //get_json()

    //setInterval(get_json, 15000)
    

    function get_json() {
        let json = $.getJSON("http://127.0.0.1:8000/news/api/",
        function (data) {
            const news_title = [];
            for (let i = 0; i < data.length; i++) {
                const title = data[i].title;
                news_title.push(title);
                $('#news').append('<p>'+title+'</p>'); 
            }
            
            
    });
}