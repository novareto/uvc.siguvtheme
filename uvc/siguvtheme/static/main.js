$(document).ready(function() {
	$("#portal-globalnav").prepend('<li id="portaltab-burger-menu"><i class="glyphicon glyphicon-menu-hamburger" /></li>'),
        /*
		$("body").on("mousemove", function(e) {
			e.pageX < 20 && $("body").attr("data-with-sidebar", "true")
		}),
        */
		$("#portaltab-burger-menu").click(function(e) {
			e.preventDefault(),
				$("body").attr("data-with-sidebar", "true")
		}),
		$("#portal-navigation-cover").click(function(e) {
			e.preventDefault(),
				$("body").attr("data-with-sidebar", "")
		})
})
