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