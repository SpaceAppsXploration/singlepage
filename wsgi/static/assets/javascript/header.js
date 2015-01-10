/*
	This file deals with functionality for the header.
	It should take care of running itself as long as it's included. It
	will probably break if it's included and the items with the correct 
	classes aren't there.
	
	Dependencies: 
	- jQuery (tested with 1.11)
	- jQuery scrollToFixed

*/

(function( $ ){
	var $header = $('.site--header');
	var $nav = $('.site--navigation');
	var $logo = $('.logo', $header );

	// an animation loop for the header pictograms, this will run itself at 
	// least twice, before settling on a random pictogram
	var interval = 100;
	var frameCount = 12;
	var totalFrame = (frameCount * 2) + Math.floor( Math.random() * frameCount );
	var changeCount = 0;
	var nextPictogramFrame = function(){		
		$logo.css('background-position', (changeCount * 100) + '%' );
		changeCount++;
		if( changeCount < totalFrame ){
			setTimeout( nextPictogramFrame, interval );
		}
	};

	// start the pictogram animation
	nextPictogramFrame();

	// run JQuery scrollToFixed on the navigation to make it conditionally
	// sticky to the top of the window.
	$nav.scrollToFixed();	

})( jQuery );