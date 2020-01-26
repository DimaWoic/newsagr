$.ajax({
    type: "GET",
    url: "http://127.0.0.1:8000/news/",
    dataType: "html",
    success: function(data){
        $('.col-6 bg-white').html(data);
    }
});