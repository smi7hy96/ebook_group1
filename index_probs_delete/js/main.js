 AOS.init({
 	duration: 800,
 	easing: 'slide',
 	once: true
 });

jQuery(document).ready(function($) {

	"use strict";

	

	var siteMenuClone = function() {

		$('.js-clone-nav').each(function() {
			var $this = $(this);
			$this.clone().attr('class', 'site-nav-wrap').appendTo('.site-mobile-menu-body');
		});


		setTimeout(function() {
			
			var counter = 0;
      $('.site-mobile-menu .has-children').each(function(){
        var $this = $(this);
        
        $this.prepend('<span class="arrow-collapse collapsed">');

        $this.find('.arrow-collapse').attr({
          'data-toggle' : 'collapse',
          'data-target' : '#collapseItem' + counter,
        });

        $this.find('> ul').attr({
          'class' : 'collapse',
          'id' : 'collapseItem' + counter,
        });

        counter++;

      });

    }, 1000);

		$('body').on('click', '.arrow-collapse', function(e) {
      var $this = $(this);
      if ( $this.closest('li').find('.collapse').hasClass('show') ) {
        $this.removeClass('active');
      } else {
        $this.addClass('active');
      }
      e.preventDefault();  
      
    });

		$(window).resize(function() {
			var $this = $(this),
				w = $this.width();

			if ( w > 768 ) {
				if ( $('body').hasClass('offcanvas-menu') ) {
					$('body').removeClass('offcanvas-menu');
				}
			}
		})

		$('body').on('click', '.js-menu-toggle', function(e) {
			var $this = $(this);
			e.preventDefault();

			if ( $('body').hasClass('offcanvas-menu') ) {
				$('body').removeClass('offcanvas-menu');
				$this.removeClass('active');
			} else {
				$('body').addClass('offcanvas-menu');
				$this.addClass('active');
			}
		}) 

		// click outisde offcanvas
		$(document).mouseup(function(e) {
	    var container = $(".site-mobile-menu");
	    if (!container.is(e.target) && container.has(e.target).length === 0) {
	      if ( $('body').hasClass('offcanvas-menu') ) {
					$('body').removeClass('offcanvas-menu');
				}
	    }
		});
	}; 
	siteMenuClone();


	var sitePlusMinus = function() {
		$('.js-btn-minus').on('click', function(e){
			e.preventDefault();
			if ( $(this).closest('.input-group').find('.form-control').val() != 0  ) {
				$(this).closest('.input-group').find('.form-control').val(parseInt($(this).closest('.input-group').find('.form-control').val()) - 1);
			} else {
				$(this).closest('.input-group').find('.form-control').val(parseInt(0));
			}
		});
		$('.js-btn-plus').on('click', function(e){
			e.preventDefault();
			$(this).closest('.input-group').find('.form-control').val(parseInt($(this).closest('.input-group').find('.form-control').val()) + 1);
		});
	};
	// sitePlusMinus();


	var siteSliderRange = function() {
    $( "#slider-range" ).slider({
      range: true,
      min: 0,
      max: 500,
      values: [ 75, 300 ],
      slide: function( event, ui ) {
        $( "#amount" ).val( "$" + ui.values[ 0 ] + " - $" + ui.values[ 1 ] );
      }
    });
    $( "#amount" ).val( "$" + $( "#slider-range" ).slider( "values", 0 ) +
      " - $" + $( "#slider-range" ).slider( "values", 1 ) );
	};
	// siteSliderRange();


	var siteMagnificPopup = function() {
		$('.image-popup').magnificPopup({
	    type: 'image',
	    closeOnContentClick: true,
	    closeBtnInside: false,
	    fixedContentPos: true,
	    mainClass: 'mfp-no-margins mfp-with-zoom', // class to remove default margin from left and right side
	     gallery: {
	      enabled: true,
	      navigateByImgClick: true,
	      preload: [0,1] // Will preload 0 - before current, and 1 after the current image
	    },
	    image: {
	      verticalFit: true
	    },
	    zoom: {
	      enabled: true,
	      duration: 300 // don't foget to change the duration also in CSS
	    }
	  });

	  $('.popup-youtube, .popup-vimeo, .popup-gmaps').magnificPopup({
	    disableOn: 700,
	    type: 'iframe',
	    mainClass: 'mfp-fade',
	    removalDelay: 160,
	    preloader: false,

	    fixedContentPos: false
	  });
	};
	siteMagnificPopup();


	var siteCarousel = function () {
		if ( $('.nonloop-block-13').length > 0 ) {
			$('.nonloop-block-13').owlCarousel({
		    center: false,
		    items: 1,
			loop: false,
			rewind: true,
				stagePadding: 0,
		    margin: 0,
		    autoplay: true,
		    nav: true,
				navText: ['<span class="icon-arrow_back">', '<span class="icon-arrow_forward">'],
		    responsive:{
	        600:{
	        	margin: 0,
	        	nav: true,
	          items: 2
	        },
	        1000:{
	        	margin: 0,
	        	stagePadding: 0,
	        	nav: true,
	          items: 3
	        },
	        1200:{
	        	margin: 0,
	        	stagePadding: 0,
	        	nav: true,
	          items: 4
	        }
		    }
			});
		}

		$('.slide-one-item').owlCarousel({
	    center: false,
	    items: 1,
		loop: false,
		rewind: true,
			stagePadding: 0,
	    margin: 0,
	    autoplay: true,
	    pauseOnHover: false,
	    nav: true,
	    navText: ['<span class="icon-keyboard_arrow_left">', '<span class="icon-keyboard_arrow_right">']
	  });
	};
	siteCarousel();

	var siteStellar = function() {
		$(window).stellar({
	    responsive: false,
	    parallaxBackgrounds: true,
	    parallaxElements: true,
	    horizontalScrolling: false,
	    hideDistantElements: false,
	    scrollProperty: 'scroll'
	  });
	};
	siteStellar();

	var siteCountDown = function() {

		$('#date-countdown').countdown('2020/10/10', function(event) {
		  var $this = $(this).html(event.strftime(''
		    + '<span class="countdown-block"><span class="label">%w</span> weeks </span>'
		    + '<span class="countdown-block"><span class="label">%d</span> days </span>'
		    + '<span class="countdown-block"><span class="label">%H</span> hr </span>'
		    + '<span class="countdown-block"><span class="label">%M</span> min </span>'
		    + '<span class="countdown-block"><span class="label">%S</span> sec</span>'));
		});
				
	};
	siteCountDown();

	var siteDatePicker = function() {

		if ( $('.datepicker').length > 0 ) {
			$('.datepicker').datepicker();
		}

	};
	siteDatePicker();

});


//1
$(".button").click(function() {
	var buttonId = $(this).attr("id");
	$("#modal-container")
	  .removeAttr("class")
	  .addClass(buttonId);
	$("body").addClass("modal-active");
  });
  
  $("#modal-container").click(function() {
	$(this).addClass("out");
	$("body").removeClass("modal-active");
  });
  

  //2
  $(".button1").click(function() {
	var buttonId = $(this).attr("id");
	$("#modal-container1")
	  .removeAttr("class")
	  .addClass(buttonId);
	$("body").addClass("modal-active");
  });
  
  $("#modal-container1").click(function() {
	$(this).addClass("out");
	$("body").removeClass("modal-active");
  });

  //3
$(".button2").click(function() {
	var buttonId = $(this).attr("id");
	$("#modal-container2")
	  .removeAttr("class")
	  .addClass(buttonId);
	$("body").addClass("modal-active");
  });
  
  $("#modal-container2").click(function() {
	$(this).addClass("out");
	$("body").removeClass("modal-active");
  });


  //4
$(".button3").click(function() {
	var buttonId = $(this).attr("id");
	$("#modal-container3")
	  .removeAttr("class")
	  .addClass(buttonId);
	$("body").addClass("modal-active");
  });
  
  $("#modal-container3").click(function() {
	$(this).addClass("out");
	$("body").removeClass("modal-active");
  });


  //5
$(".button4").click(function() {
	var buttonId = $(this).attr("id");
	$("#modal-container4")
	  .removeAttr("class")
	  .addClass(buttonId);
	$("body").addClass("modal-active");
  });
  
  $("#modal-container4").click(function() {
	$(this).addClass("out");
	$("body").removeClass("modal-active");
  });


  //6
$(".button5").click(function() {
	var buttonId = $(this).attr("id");
	$("#modal-container5")
	  .removeAttr("class")
	  .addClass(buttonId);
	$("body").addClass("modal-active");
  });
  
  $("#modal-container5").click(function() {
	$(this).addClass("out");
	$("body").removeClass("modal-active");
  });

  console.clear();

class Carousel {
	constructor (config) {
  	this.target = config.target;
    this.items = config.items;
    this.active = 0;
    this.animating = false;
    
    this.populate();
  }
  
  slide (forward) {
  	const delay = 50;
    
    this.elements.items.out.classList.add('static');
    
  	switch (forward) {
   		case true: 
      	setTimeout(() => {
        	this.elements.items.out.classList.add('carousel__item--right');
        	this.elements.items.out.classList.remove('carousel__item--left');
          
          setTimeout(() => {
          	this.elements.items.out.classList.remove('static');
          	
            setTimeout(() => {
              this.elements.items.left.classList.add('carousel__item--out');
              
              this.elements.items.center.classList.remove('carousel__item--center');
              this.elements.items.center.classList.add('carousel__item--left');
              
              this.elements.items.right.classList.remove('carousel__item--right');
              this.elements.items.right.classList.add('carousel__item--center');
              
              this.elements.items.out.classList.remove('carousel__item--out');
            }, delay);
          }, delay);
        }, delay);
      break;
      
      case false:
      	setTimeout(() => {
        	this.elements.items.out.classList.add('carousel__item--left');
        	this.elements.items.out.classList.remove('carousel__item--right');
          
          setTimeout(() => {
          	this.elements.items.out.classList.remove('static');
          
            setTimeout(() => {
              this.elements.items.right.classList.add('carousel__item--out');

              this.elements.items.center.classList.remove('carousel__item--center');
              this.elements.items.center.classList.add('carousel__item--right');

              this.elements.items.left.classList.remove('carousel__item--left');
              this.elements.items.left.classList.add('carousel__item--center');

              this.elements.items.out.classList.remove('carousel__item--out');
            }, delay);
          }, delay);
        }, delay);      
      break;
    }  
              
    setTimeout(() => {
      this.elements.items.left = this.target.querySelector('.carousel__item--left:not(.carousel__item--out)');
      this.elements.items.center = this.target.querySelector('.carousel__item--center');
      this.elements.items.right = this.target.querySelector('.carousel__item--right:not(.carousel__item--out)');
      this.elements.items.out = this.target.querySelector('.carousel__item--out');
      
      this.animating = false;
    }, delay * 4);
  }
  
  updateValues (forward) {
  	if (!this.animating) {
    	this.animating = true;
      
      let newItem = 0;

			switch (forward) {
        case true:
          if (this.active < this.items.length - 1) {
            ++this.active;
          } else {
            this.active = 0;
          }

          newItem = this.active + 1 <= this.items.length - 1 ? this.active + 1 : 0;
        break;
        
        case false:
          if (this.active > 0) {
            --this.active;
          } else {
            this.active = this.items.length - 1;
          }

          newItem = this.active - 1 >= 0 ? this.active - 1 : this.items.length - 1;
        break;
      }

      this.elements.items.out.style.backgroundImage = `url('${this.items[newItem].image}')`;

      this.slide(forward);
    }
  }
  
  eventListeners () {
  	this.elements.arrows.left.addEventListener('click', this.updateValues.bind(this, false));
  	this.elements.arrows.right.addEventListener('click', this.updateValues.bind(this, true));
  }
  
  populate () {
    function append (obj, target) {
      for (const el in obj) {
        if (obj[el].nodeName) {
          target.appendChild(obj[el]);
        } else {
          append(obj[el], target);
        }
      }
    }

  	this.elements = {};
    this.elements.items = {};
    this.elements.arrows = {};
    
    this.elements.items.left = document.createElement('div');
    this.elements.items.center = document.createElement('div');
    this.elements.items.right = document.createElement('div');
    this.elements.items.out = document.createElement('div');
    this.elements.arrows.left = document.createElement('div');
    this.elements.arrows.right = document.createElement('div');
    
    this.elements.items.left.classList.add('carousel__item');
    this.elements.items.center.classList.add('carousel__item');
    this.elements.items.right.classList.add('carousel__item');
    this.elements.items.out.classList.add('carousel__item');
    this.elements.items.left.classList.add('carousel__item--left');
    this.elements.items.center.classList.add('carousel__item--center');
    this.elements.items.right.classList.add('carousel__item--right');
    this.elements.items.out.classList.add('carousel__item--right');
    this.elements.items.out.classList.add('carousel__item--out');
    this.elements.arrows.left.classList.add('carousel__arrow');
    this.elements.arrows.right.classList.add('carousel__arrow');
    this.elements.arrows.left.classList.add('carousel__arrow--left');
    this.elements.arrows.right.classList.add('carousel__arrow--right');
    
    this.elements.items.left.style.backgroundImage = `url('${this.items[this.items.length - 1].image}')`;
    this.elements.items.center.style.backgroundImage = `url('${this.items[0].image}')`;
    this.elements.items.right.style.backgroundImage = `url('${this.items[1].image}')`;
    
    append(this.elements, this.target);
    
    this.eventListeners();
  }
}

new Carousel({
	target: document.querySelector('.carousel'),
  items: [
  	{
    	image: "./images/Tall-Mercedes.jpg"
    },
  	{
    	image: "./images/Tall Mustang.jpg"
    },
  	{
    	image: "./images/VW.jpeg"
    },
  	{
    	image: "./images/Tall Toyota.jpg"
    },
  	{
    	image: "./images/Tall Audi.jpg"
    }
  ]
});
