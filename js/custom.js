$(document).ready(function() {
	$(".videoOvelap").click(function(){
		$(this).fadeOut();
		$("#video")[0].src += "&autoplay=1";
		$("#video").css("position", "relative");
	});


	var myFullpage = new fullpage('#fullpage', {
		anchors: ['home', 'about', 'wwd', 'init', 'run', 'redc', 'media', 'contact'],
		sectionsColor: ['#000000', '#ffffff', '#ffffff', '#ffffff', '#ffffff', '#ffffff', '#ffffff', '#1a1a1a'],
		menu: '.navbar-nav',
		scrollOverflow: true,
		onLeave: function (origin, destination, direction) {
			var leavingSection = this;
			if (origin.index == 0 && direction == "down") {
				$("#header").addClass("headerAnimation");
			} else if (origin.index == 1 && direction == "up") {
				$("#header").removeClass("headerAnimation");
			}
		},
		onSlideLeave: function( section, origin, destination, direction){
			var leavingSlide = this;

			//leaving the first slide of the 2nd Section to the right
			if(section.index == 1 && origin.index == 0 && direction == 'right'){
				$("#header").addClass("videoActive");
			} else {
				$("#header").removeClass("videoActive");
			}
		}
	});

	$(document).on('click', '.gotoSection', function () {
		fullpage_api.moveTo($(this).data("section"), $(this).data("moveto"));
	});	


	$(".fp-next").html("&#x203a;");
	$(".fp-prev").html("&#x2039;");

	var owl = $('.runwaycarousel');
			owl.owlCarousel({
			    lazyLoad:true,
				nav: true,
				dots: false,
				loop: false,
				responsive: {
					0: {
						items: 1
					},
					600: {
						items: 3
					},
					1000: {
						items: 4
					}
				}
			});

$(document).on('keydown', function( event ) {
    if(event.keyCode == 37) {
        owl.trigger('prev.owl')
    }
    if(event.keyCode == 39) {
        owl.trigger('next.owl')
    }
});
	$(".skipper").click(function(){
		$(".splash_screen").fadeOut();
		$(".splash_screen").find("img").attr("src", " ");
	});

	$('.navbar-nav>li>a').on('click', function(){
		$(".hamburger").removeClass("is-active");
	    $('.navbar-collapse').collapse('hide');
	});
	$('body').on('click', function(){
	    // $('.navbar-toggler[aria-expanded="true"]').trigger('click');
	    $('.navbar-collapse.show').prev().removeClass("is-active");
	    $('.navbar-collapse').collapse('hide');
	});
	$(".hamburger").click(function(){
	    $(this).toggleClass("is-active");
	});

	if ($(window).width() < 960) {
		if (window.orientation == 0) {
		    $(".RotateYourView").hide();
		    $(".actualBody").show();
	  } else {
	    $(".RotateYourView").show();
	    $(".actualBody").hide();
	  }
	}

	$(window).on("orientationchange",function(){
	    if ($(window).width() < 960) {
		  if(window.orientation === 0) // Portrait
		  {
		    $(".RotateYourView").hide();
		    $(".actualBody").show();
		  }
		  else // Landscape
		  {
		    $(".RotateYourView").show();
		    $(".actualBody").hide();
		  }
		}
	});

	$('.AlphaOnly').bind('keyup blur',function(){ 

    var node = $(this);

    node.val(node.val().replace(/[^A-Za-z_\s]/,'') ); }   // (/[^a-z]/g,''

);

     $(".NumberOnly").keypress(function(evt){

 evt = (evt) ? evt : window.event;

    var charCode = (evt.which) ? evt.which : evt.keyCode;

    if (charCode > 31 && (charCode < 48 || charCode > 57)) {

        return false;

    }

    return true;

     });   
});

document.onreadystatechange = function () {
var state = document.readyState
if (state == 'interactive') {
	$(".splash_screen").find("img").attr("src", "images/logo-splash-farruch.gif");
	$(".skipper").hide();
} else if (state == 'complete') {
	if($(window).width() > 960){
		var position = $(".navbar-brand").offset();
	} else {
		var position = $(".mob-navbar-brand").offset();
	}
	$(".skipper").show();
	setTimeout(function(){
		$(".splash_screen").find("img").addClass("splashLogo");
		$(".splash_screen").find("img").css({
			left: position.left,
			top: position.top,
			transform: "translate(0,0)"
		});
		setTimeout(function(){
			$(".splash_screen").fadeOut();
		},3000);
	},5000);
}
}