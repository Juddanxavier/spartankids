/* Please ❤ this if you like it! */


(function ($) {
	"use strict";

	$(function () {
		var header = $(".start-style");
		$(window).scroll(function () {
			var scroll = $(window).scrollTop();

			if (scroll >= 10) {
				header.removeClass('start-style').addClass("scroll-on");
			} else {
				header.removeClass("scroll-on").addClass('start-style');
			}
		});
	});


	//Menu On Hover

	$('body').on('mouseenter mouseleave', '.nav-item', function (e) {
		if ($(window).width() > 750) {
			var _d = $(e.target).closest('.nav-item');
			_d.addClass('show');
			setTimeout(function () {
				_d[_d.is(':hover') ? 'addClass' : 'removeClass']('show');
			}, 1);
		}
	});

})(jQuery);

const height = (elem) => {

	return elem.getBoundingClientRect().height

}

const distance = (elemA, elemB, prop) => {

	const sizeA = elemA.getBoundingClientRect()[prop]
	const sizeB = elemB.getBoundingClientRect()[prop]

	return sizeB - sizeA

}

const factor = (elemA, elemB, prop) => {

	const sizeA = elemA.getBoundingClientRect()[prop]
	const sizeB = elemB.getBoundingClientRect()[prop]

	return sizeB / sizeA

}

document.querySelectorAll('.card').forEach((elem) => {

	const head = elem.querySelector('.card__head')
	const image = elem.querySelector('.card__image_daycare, .card__image_preschool, .card__image_afterschool, .card__image_summercamp')

	const author = elem.querySelector('.card__author')
	const body = elem.querySelector('.card__body')
	const foot = elem.querySelector('.card__foot')

	elem.onmouseenter = () => {

		elem.classList.add('hover')

		const imageScale = 1 + factor(head, body, 'height')
		image.style.transform = `scale(${ imageScale })`

		const bodyDistance = height(foot) * -1
		body.style.transform = `translateY(${ bodyDistance }px)`

		const authorDistance = distance(head, author, 'height')
		author.style.transform = `translateY(${ authorDistance }px)`

	}

	elem.onmouseleave = () => {

		elem.classList.remove('hover')

		image.style.transform = `none`
		body.style.transform = `none`
		author.style.transform = `none`

	}

})
$(".nav .nav-link").on("click", function () {
	$(".nav").find(".active").removeClass("active");
	$(this).addClass("active");
});