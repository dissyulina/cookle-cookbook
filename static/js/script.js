$(document).ready(function(){
    $('input[type=radio][name=radio-img]').change(function() {
        let radioValue = $('input[name=radio-img]:checked', '#form-register').val();
        if (radioValue === "2") {
            alert(radioValue);
            $("#show-image").attr("src","");
            $('#profile-image').val("");
            $("#profile-url").change(function(){
                loadImage();
            });
        } else if (radioValue === "3") {
            alert(radioValue);
            $("#show-image").attr("src","");
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
            $('#show-image').attr('src', e.target.result);
        }
        reader.readAsDataURL(input.files[0]);
    }
}

function loadImage(){
    var image = document.getElementById("show-image");
    var url = document.getElementById("profile-url");
    image.src = url.value;
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
