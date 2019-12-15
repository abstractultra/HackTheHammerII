var div_content = "<h3>Statistics:</h3><br>";
var total_scores = 0;
var user_scores = [];
$(document).ready(function() {
    $.getJSON("./read_from_db.php", function(data) {
        $.each(data, function(user_id, sleep_score) {
            //console.log(user_id + " : " + sleep_score);
            total_scores += parseInt(sleep_score);
            div_content += "Person " + user_id + " score: " + sleep_score + "<br>";
        });
    });
    console.log(div_content);
});
function load_scores() {
    document.getElementById("content_box").innerHTML=div_content;
}