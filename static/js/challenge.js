$(document).ready(function() {

    $('.flash').animate({left: "15%"}, "slow", "swing").delay(6000).fadeOut('fast').delay(4000).show('fast');
	
	
// 	Challenge page Question, Attempt and Score counters
	$('div.hidden_question').delay(2000).fadeIn("slow").fadeOut("slow").fadeIn("slow");
	$('div.hidden_attempt').delay(4000).fadeIn("slow").fadeOut("slow").fadeIn("slow").fadeOut("slow").fadeIn("slow");
	$('div.hidden_score').delay(6000).fadeIn("slow")

// Challenge page Challenge text
    $('h2.challenge-number').delay(7000).fadeIn("fast");
    $('p.hidden_para').delay(7500).fadeIn("fast");
    $('h1.challenge_title').delay(8000).fadeIn("fast");
    $('p.challenge-text').delay(8500).fadeIn("fast");
    $('.form-inline').delay(10000).fadeIn("slow");

// Click to hide flash messages
    $(".warning").click(function(){
        $(".warning").hide();
    });
// Hover effect on count cards
    $('.card').mouseover(function(){
        $(this).css('background-color', '#000');
    });    
    $('.card').mouseout(function(){
        $(this).css('background-color', "rgba(66, 24, 59, 0.78)");
    });
    




    // Numbers (need) on Challenge Pages dissolve in on page load
    // $('body').click(function() {
    //     $('h1.hidden').slideDown("slow").removeClass('hidden');
    //     $('h2.hidden').slideDown("slow").removeClass('hidden');
    //     $('h1.hidden_title').slideDown("slow").removeClass('hidden');
    //     $('h2.hidden_title').slideDown("slow").removeClass('hidden');
    //     $('form.hidden_title').slideDown("slow").removeClass('hidden');
    // });


    // Transitions after button click
    // $('.challenge_btn').click(function() {
    //     $(this).slideUp("fast");
    //     $('h2.hidden_answer').delay(1000).show("fast").removeClass('hidden');
    //     $('h1.hidden_answer').delay(2000).show("fast").removeClass('hidden');
    //     $('.hidden_icon').delay(4000).fadeIn(400).fadeOut(400).fadeIn(400).fadeOut(400).fadeIn(400).removeClass('hidden');
    // });
    
    // Display Score
    // $('.username').slideDown(3000).removeClass('hidden');

    // Page Alerts removed
    // $("body").click(function() {
    //     $(".alert").hide("fast");
    // });
});
