$("#login-button").click(function(event){
     event.preventDefault();

 $('form').hide(500).show(1000);
 $('.wrapper').addClass('form-success');
});