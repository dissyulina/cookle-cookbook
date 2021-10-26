$(document).ready(function(){
    $('input[type=radio][name=radio-img]').change(function() {
        let radioValue = $('input[name=radio-img]:checked', '#form-register').val();
        if (radioValue === "2") {
            alert(radioValue);
            $(".show-image").attr("src","");
            $('#profile-image').val("");
            $("#profile-url").change(function(){
                loadImage();
            });

        } else if (radioValue === "3") {
            alert(radioValue);
            $(".show-image").attr("src","");
            $('#profile-url').val("");
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
    var url = document.getElementById("profile-url");
    image[0].src = url.value;
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


/* When login button is clicked, change pills login to active 
$("#login-btn").click(function(e) {
    e.preventDefault();
    $("#tab-login").addClass("active").attr("aria-selected","true");
    $("#tab-register").removeClass("active").attr("aria-selected","false");
    $("#pills-login").addClass("show active");
    $("#pills-register").removeClass("show active");

});
*/

/* Make sure user image is square 
var divWidth = $('.square-image').width(); 

$(window).resize(function(){
    $('.square-image').height(divWidth);
});
*/

/* Add Recipe page */
let ingredients = 1;
let maxIngredients = 30;
let directions = 1;
let maxDirections = 30;

$("#add-ing-btn").click(function (e) {
    e.preventDefault();
    $("#ingredients-wrapper").append(
    `<div class="d-flex flex-row">
        <input type="text" class="form-control flex-grow new-field" name="ingredients" placeholder="2 cloves of garlic">
        <button class="btn btn-remove" type="button"><i class="fas fa-trash-alt"></i></button>
    </div>`);
    ingredients++
});

$("#add-dir-btn").click(function (e) {
    e.preventDefault();
    $("#directions-wrapper").append(
    `<div class="d-flex flex-row">
        <input type="text" class="form-control new-field" name="directions" placeholder="Mince the garlic and shallots">
        <button class="btn btn-remove" type="button"><i class="fas fa-trash-alt"></i></button>
    </div>`);
    ingredients++
});

/* Delete parent div when clicking the remove button,
ref: https://stackoverflow.com/questions/6647736/how-to-delete-parent-element-using-jquery */
$("#ingredients-wrapper").on("click", ".btn-remove", function(e){
    e.preventDefault();
    $(this).parent('div').remove();
    ingredients--;
});

$("#ingredients-wrapper").on("click", ".btn-remove", function(e){
    e.preventDefault();
    $(this).parent('div').remove();
    ingredients--;
});