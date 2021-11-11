/* All pages: Navbar hide on scroll down, show on scroll up
Code was sourced from https://bootstrap-menu.com/detail-autohide.html */
document.addEventListener("DOMContentLoaded", function(){
    el_autohide = document.querySelector('.autohide');
    // add padding-top to body
    navbar_height = document.querySelector('.navbar').offsetHeight;
    document.body.style.paddingTop = navbar_height + 'px';
  
    if(el_autohide){
      var last_scroll_top = 0;
      window.addEventListener('scroll', function() {
            let scroll_top = window.scrollY;
           if(scroll_top < last_scroll_top) {
                el_autohide.classList.remove('scrolled-down');
                el_autohide.classList.add('scrolled-up');
            }
            else {
                el_autohide.classList.remove('scrolled-up');
                el_autohide.classList.add('scrolled-down');
            }
            last_scroll_top = scroll_top;
      }); 
    }
}); 

/* Home Page: To pass the value of the search box to recipes page */
$("#btn-query").click(function() {
    let query = $("#home-query").val();
    sessionStorage.setItem("query",query);
})
$("#query").attr("value",sessionStorage.getItem("query"))
sessionStorage.removeItem("query");


$(document).ready(function(){
    $('input[type=radio][name=radio-img]').change(function() {
        let radioValue = $('input[name=radio-img]:checked', '#form-register').val();
        if (radioValue === "2") {
            $(".show-image").attr("src","");
            $('#profile-image').val("");
            $("#image-url").change(function(){
                loadImage();
            });

        } else if (radioValue === "3") {
            $(".show-image").attr("src","");
            $('#image-url').val("");
            $("#profile-image").change(function(){
                readURL(this);
            });
        }
    });
});

function readURL(input) {
    if (input.files && input.files[0]) {
        var reader = new FileReader();
        
        reader.onload = function (e) {
            $('.show-image').attr('src', e.target.result);
        }
        reader.readAsDataURL(input.files[0]);
    }
}

function loadImage(){
    var image = document.getElementsByClassName("show-image");
    var url = document.getElementById("image-url");
    console.log(image);
    image[0].src = url.value;
    console.log(image[0]);
}

/* To check passwords match before submitting, addapted from: 
https://stackoverflow.com/questions/21727317/how-to-check-confirm-password-field-in-form-without-reloading-page/21727518
*/
$('#repeat-password').on('keyup', function () {
    console.log("keyup");
    if ($('#password').val() == $('#repeat-password').val()) {
        $('#valid-message').html('Passwords match.').css('color', 'green');
        $('.submit-btn').prop('disabled', false).removeClass('disabled');
    } else {
        $('#valid-message').html('Passwords do not match.').css('color', 'red');
        $('.submit-btn').prop('disabled', true).addClass('disabled');
    }
});

/* Add Recipe / Edit Recipe Page: Add new line to ingredients and directions */
let ingredients = 1;
let maxIngredients = 30;
let directions = 1;
let maxDirections = 30;
$("#add-ing-btn").click(function (e) {
    e.preventDefault();
    $("#ingredients-wrapper").append(
    `<div class="d-flex flex-row">
        <input type="text" class="form-control flex-grow new-field" name="ingredients" placeholder="2 cloves of garlic" required>
        <button class="btn btn-remove" type="button"><i class="fas fa-trash-alt"></i></button>
    </div>`);
    ingredients++
});

$("#add-dir-btn").click(function (e) {
    e.preventDefault();
    $("#directions-wrapper").append(
    `<div class="d-flex flex-row">
        <input type="text" class="form-control new-field" name="directions" placeholder="Mince the garlic and shallots" required>
        <button class="btn btn-remove" type="button"><i class="fas fa-trash-alt"></i></button>
    </div>`);
    ingredients++
});

/* Add Recipe / Edit Recipe Page: Delete parent div when clicking the remove ingredient/direction button,
ref: https://stackoverflow.com/questions/6647736/how-to-delete-parent-element-using-jquery */
$("#ingredients-wrapper").on("click", ".btn-remove", function(e){
    e.preventDefault();
    $(this).parent('div').remove();
    ingredients--;
});

$("#directions-wrapper").on("click", ".btn-remove", function(e){
    e.preventDefault();
    $(this).parent('div').remove();
    ingredients--;
});

/* Display recipe image in add recipe page */
$("#image-url").change(function(){
    loadImage();
});

/* Home Page: Carousel for popular recipes */
/* Code for carousel was sourced and modified from: https://www.codeply.com/p/0CWffz76Q9 */
let popularItems = document.querySelectorAll('#popularRecipesCarousel .carousel-item')
popularItems.forEach((el) => {
    const minPerSlide = 4
    let next = el.nextElementSibling
    for (var i=1; i<minPerSlide; i++) {
        if (!next) {
            // wrap carousel by using first child
        	next = popularItems[0]
      	}
        let cloneChild = next.cloneNode(true)
        el.appendChild(cloneChild.children[0])
        next = next.nextElementSibling
    }
})
$(".popular-item").first().addClass("active");

/* Home Page: Carousel for recent recipes */
let recentItems = document.querySelectorAll('#recentRecipesCarousel .carousel-item')
recentItems.forEach((el) => {
    const minPerSlide = 4
    let next = el.nextElementSibling
    for (var i=1; i<minPerSlide; i++) {
        if (!next) {
            // wrap carousel by using first child
        	next = recentItems[0]
      	}
        let cloneChild = next.cloneNode(true)
        el.appendChild(cloneChild.children[0])
        next = next.nextElementSibling
    }
})
$(".recent-item").first().addClass("active");

/* Home Page: Carousel for cookbooks we love */
let cookbooksItems = document.querySelectorAll('#cookbooksCarousel .carousel-item')
cookbooksItems.forEach((el) => {
    const minPerSlide = 4
    let next = el.nextElementSibling
    for (var i=1; i<minPerSlide; i++) {
        if (!next) {
            // wrap carousel by using first child
        	next = cookbooksItems[0]
      	}
        let cloneChild = next.cloneNode(true)
        el.appendChild(cloneChild.children[0])
        next = next.nextElementSibling
    }
})
$(".cookbooks-item").first().addClass("active");


/* Single Recipe Page: If user clicks Write A Review button, show form */
$("#btn-review").click(function() {
    $("#write-review").toggleClass('d-none')
    $("#write_review").focus();
});

/* Single Recipe Page: If user clicks Edit review button, show form */
$("#btn-edit-review").click(function() {
    $("#edit-review").removeClass('d-none')
    $("#edit_review").focus();
});

/* My Cookbook page: Keep the current pill active on page reload */
$(document).ready(function(){
    $('a[data-mdb-toggle="pill"]').click(function(e) {
        sessionStorage.setItem('activePill', $(e.target).attr('href'));
    })

    let activePill = sessionStorage.getItem("activePill");
    if (activePill) {
        $('#cookbook-pills a[href="' + activePill + '"]').addClass("active")
        let activeContent = activePill.substring(1);
        $('#' + activeContent).addClass("show active");
    } else {
        $('#cookbook-pills a[href="#ex3-pills-1"]').addClass("active")
        $('#ex3-pills-1').addClass("show active")
    }
});

