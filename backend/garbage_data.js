$(document).ready(function() {
    while (true) {
        $.post("./write_to_db.php", { user_id: Math.random()*2000, sleep_score: Math.random()*2000 });
    }
});