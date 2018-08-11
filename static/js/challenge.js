$(document).ready(function() {
	

    // Numbers (need) on Challenge Pages dissolve in on page load
    $('body').click(function() {
        $('h1.hidden').slideDown("slow").removeClass('hidden');
        $('h2.hidden').slideDown("slow").removeClass('hidden');
        $('h1.hidden_title').slideDown("slow").removeClass('hidden');
        $('h2.hidden_title').slideDown("slow").removeClass('hidden');
        $('form.hidden_title').slideDown("slow").removeClass('hidden');
    });


    // AJAX POST Request
    // $('.challenge_btn').click(function() {
    //     var score = $('#numScore').val();
    //     $.ajax({
    //         data: $('form').serialize(),
    //         type: 'POST',
    //         success: function(response) {
    //             return ("SUCCESS!");
    //         },
    //         error: function(error) {
    //             return false;
    //         }
    //     });
    // });

    // Transitions after button click
    $('.challenge_btn').click(function() {
        $(this).slideUp("fast");
        $('h2.hidden_answer').delay(1000).show("fast").removeClass('hidden');
        $('h1.hidden_answer').delay(2000).show("fast").removeClass('hidden');
        $('.hidden_icon').delay(4000).fadeIn(400).fadeOut(400).fadeIn(400).fadeOut(400).fadeIn(400).removeClass('hidden');
    });
    
    // Display Score
    $('.username').slideDown(3000).removeClass('hidden');

    // Page Alerts removed
    $("body").click(function() {
        $(".alert").hide("fast");
    });
});
