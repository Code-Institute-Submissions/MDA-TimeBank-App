$(document).ready(function() {
    
    // Numbers (need) on Challenge Pages dissolve in on page load
    $('h1.hidden').fadeIn(2000).removeClass('hidden');
    $('h2.hidden').show(2000).removeClass('hidden');
    $('h1.hidden_title').delay(3000).show("fast").removeClass('hidden');
    $('h2.hidden_title').delay(5000).show("fast").removeClass('hidden');
    $('form.hidden_title').delay(8000).show("fast").removeClass('hidden');
    



});