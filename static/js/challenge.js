$(document).ready(function() {

// Fly in the message following guess
    $('.flash').animate({left: "15%"}, "slow", "swing");
	
// 	Challenge page Question, Attempt and Score counters
	$('div.hidden_question').fadeIn("slow").fadeOut("slow").fadeIn("slow");
	$('div.hidden_attempt').delay(1000).fadeIn("slow").fadeOut("slow").fadeIn("slow").fadeOut("slow").fadeIn("slow");
	$('div.hidden_score').delay(2000).fadeIn("slow")

// Challenge page Challenge text
    $('h2.challenge-number').delay(3000).fadeIn("fast");
    $('p.hidden_para').delay(3500).fadeIn("fast");
    $('h1.challenge_title').delay(4000).fadeIn("fast");
    $('p.challenge-text').delay(4500).fadeIn("fast");
    $('.form-inline').delay(5000).fadeIn("slow");

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
