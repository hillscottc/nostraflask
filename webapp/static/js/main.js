
var app = app || {};



app.ajaxPost = function(url, data){
    console.log("Posting to " + url + " with " +  JSON.stringify(data));
    var request = $.ajax({
        url: url,
        type: 'POST',
        contentType: 'application/json; charset=utf-8',
        data: JSON.stringify(data),
        dataType: 'text',
        success: function(result) {
            console.log("Got status " + request['statusText'] + ", " + result);
            //var json_data = JSON.parse(result);
            //console.log(JSON.stringify(json_data.fortune));
        }
    });
}

$("#horo-btn").click(function(){
    var nostra_el = $("#sample-horo");

    nostra_el.hide("scale");

    nostra_el.load(app.nostra_url, function(responseTxt, statusTxt, xhr){
        if(statusTxt == "error") console.log("Err: " + xhr.status + ": " + xhr.statusText);
    });

    app.ajaxPost('/fortune', {});

    nostra_el.show("scale");
});

