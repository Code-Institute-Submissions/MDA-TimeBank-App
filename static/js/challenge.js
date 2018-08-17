$(document).ready(function() {

    $('.flash').animate({left: "15%"}, "slow", "swing").delay(6000);
	
	
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
    $(".flash").click(function(){
        $(this).hide();
    });
// Hover effect on count cards
    $('.card').mouseover(function(){
        $(this).css('background-color', '#000');
    });    
    $('.card').mouseout(function(){
        $(this).css('background-color', "rgba(66, 24, 59, 0.78)");
    });

    
});
