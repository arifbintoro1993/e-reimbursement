/* Project specific Javascript goes here. */
$(document).ready(function(){
    $('.navbar-static-side .nav li').on('click', function(){
      $(".secondary-sidebar").removeClass('expand');
  
          if($(this).hasClass('has-submenu')){
        $(".secondary-sidebar").addClass('expand');
        $('.secondary-sidebar span').removeClass('collapse');
        $('.secondary-sidebar '+$(this).attr('data-toggle')).addClass('collapse');
      }
           $('li').removeClass('active');
          $(this).addClass('active');
      });
  
      $('.navbar-static-side .nav li a i').hover(function(){
          $('.secondary-sidebar span').removeClass('collapse');
      $(".secondary-sidebar").removeClass('expand');
      });
  });