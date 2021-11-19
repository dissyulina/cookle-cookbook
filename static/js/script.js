/* All pages: Navbar hide on scroll down, show on scroll up
Code was sourced from https://bootstrap-menu.com/detail-autohide.html */
document.addEventListener("DOMContentLoaded", function(){
    let el_autohide = document.querySelector('.autohide');
    // add padding-top to body
    let navbar_height = document.querySelector('.navbar').offsetHeight;
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
});
$("#query").attr("value",sessionStorage.getItem("query"));
sessionStorage.removeItem("query");

/* Register page, Edit profile page, Add recipe page, and Edit Recipe page: 
To render/display image based on url input */
$(".image-url").on("input", function(){
    $(".show-image").attr("src", $(".image-url").val());
});

/* Register page, Change Password page:
To check passwords match before submitting, addapted from: 
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

/* Add Recipe page and Edit Recipe Page: Add new line to ingredients (maximum 30 lines) */
let ingredients;
let maxIngredients = 15;

if ($("#number-ingredients").text()) {
    ingredients = parseInt($("#number-ingredients").text()); 
} else {
    ingredients = 1;
}

$("#add-ing-btn").click(function (e) {
    if (ingredients < maxIngredients) {
        e.preventDefault();
        $("#ingredients-wrapper").append(
        `<div class="d-flex flex-row">
            <input type="text" class="form-control flex-grow new-field" name="ingredients" required>
            <button class="btn btn-remove" type="button"><i class="fas fa-trash-alt"></i></button>
        </div>`);
        ingredients++;
    } else {
        $("#add-ing-btn").text("You can't add more ingredients.");
        e.preventDefault();
    }
});

/* Add Recipe page and Edit Recipe Page: Add new line to directions (maximum 30 lines) */
let directions;
let maxDirections = 15; 

if ($("#number-directions").text()) {
    directions = parseInt($("#number-directions").text()); 
} else {
    directions = 1;
}

$("#add-dir-btn").click(function (e) {
    if (directions < maxDirections) {
        e.preventDefault();
        $("#directions-wrapper").append(
        `<div class="d-flex flex-row">
            <input type="text" class="form-control new-field" name="directions" required>
            <button class="btn btn-remove" type="button"><i class="fas fa-trash-alt"></i></button>
        </div>`);
        directions++;
    } else {
        $("#add-dir-btn").text("You can't add more directions.");
        e.preventDefault();
    }
});

/* Add Recipe and Edit Recipe Page: Delete parent div when clicking the remove ingredient/direction button,
ref: https://stackoverflow.com/questions/6647736/how-to-delete-parent-element-using-jquery */
$("#ingredients-wrapper").on("click", ".btn-remove", function(e){
    e.preventDefault();
    $(this).parent('div').remove();
    $("#add-ing-btn").html('<i class="fas fa-plus"></i> Add more ingredients');
    ingredients--;
});

$("#directions-wrapper").on("click", ".btn-remove", function(e){
    e.preventDefault();
    $(this).parent('div').remove();
    $("#add-dir-btn").html('<i class="fas fa-plus"></i> Add more directions');
    directions--;
});

/* Single Recipe Page: If user clicks Write A Review button, show form */
$("#btn-review").click(function() {
    $("#write-review").toggleClass('d-none');
    $("#write_review").focus();
});

/* Single Recipe Page: If user clicks Edit review button, show form and move it up */
$(".btn-edit-review").click(function(e) {
    let reviewId = $(e.target).attr('data-id');
    $('#edit-review' + reviewId).removeClass('d-none').focus();
    $('#edit-review' + reviewId).detach().appendTo("#new-edit-review");
});

/* My Cookbook page: Keep the current pill active on page reload */
$(document).ready(function(){
    $('a[data-mdb-toggle="pill"]').click(function(e) {
        sessionStorage.setItem('activePill', $(e.target).attr('href'));
    });

    let activePill = sessionStorage.getItem("activePill");
    if (activePill) {
        $('#cookbook-pills a[href="' + activePill + '"]').addClass("active");
        let activeContent = activePill.substring(1);
        $('#' + activeContent).addClass("show active");
    } else {
        $('#cookbook-pills a[href="#all-pills"]').addClass("active");
        $('#all-pills').addClass("show active");
    }
});

/* Homepage: EmailJS for Inviting Friends*/
$('#invite-form').on('submit', function (e) {
    e.preventDefault();
    sendInvitation(this); 
});

function sendInvitation(inviteForm) {
    emailjs.send("yahoo","cookle_ms3", {"send_to": inviteForm.emailInvite.value})
    .then(function(response) {
        console.log('SUCCESS!', response.status, response.text);
        // Change the display
        $("#btn-invite").html('<i class="fas fa-check"></i> Sent');
        // After 2 seconds turn it back to empty form
        setTimeout(function(){
            $('#invite-form')[0].reset();
            $("#btn-invite").html('Send Invitation');
        }, 2000);
    }, 
    function(error) {
        console.log('FAILED...', error);
    });
    return false;
}

/* Footer (All Pages) : EmailJS for Contact Form*/
$('#contact-form').on('submit', function (e) {
    e.preventDefault();
    sendMail(this); 
});

function sendMail(contactForm) {
    emailjs.send("yahoo", "contact_cookle", {
        "from_name": contactForm.name.value,
        "from_email": contactForm.email.value,
        "message": contactForm.message.value,
    })
    .then(function(response) {
        console.log('SUCCESS!', response.status, response.text);
        // Change the display
        $("#message-sent").removeClass("d-none");
        $("#contact-modal").addClass("d-none");
        // After 2 seconds turn it back to contact form
        setTimeout(function(){
            $('#contact-form')[0].reset();
            $("#message-sent").addClass("d-none");
            $("#contact-modal").removeClass("d-none");
        }, 2000);
    }, 
    function(error) {
        console.log('FAILED...', error);
    });
    return false;
}

