$(document).ready(function() {
    $.getJSON("./read_from_db.php", function(data) {
        $.each(data, function(user_id, sleep_score) {
            console.log(user_id + " : " + sleep_score);
        });
    });
});