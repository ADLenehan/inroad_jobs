$(document).ready(function() {
    $('.card').click(function(event){

        var header = $('.modal-header');
        var body = $('.modal-body')

        header.empty();
        header.html($(this).find(".card-img-top").html());
        header.css("background-color",$(this).find(".card-img-top").css("background-color"));
        body.empty();
        body.html($(this).find(".card-block").html());
        $(".modal-profile").modal({show:true});

        position_id = $(this).attr("position-id");

        $('#comments').empty();
        $('#modal-buttons').empty();
        $.ajax({
            url: '/NY-tech/'+position_id+'/comments',
            type: 'get',
            dataType: 'json',
            success: function (data) {
                $.each(data, function(key,element) {
                    if (key=='comments'){
                        if (element!=false){
                            $('#comments').append("<div class='card-block comment-block'><div class='row'><div class='col-1'><img class='nav-icon' src='"+element.picture_url+"'></div><div class='col-11'><h5>"+element.user_position+"</h5><h6>"+element.company+"</h6>"+element.text+"</div></div></div>");
                        }
                    } else if (key=='saved') {
                         if (element==false){
                            $('#modal-buttons').append("<a href = \"/"+position_id+"/save_job/\"><button class='btn btn-inroad' type='button' style = 'margin-right: 2px;'>Save</button></a>");
                            } else {
                            $('#modal-buttons').append("<a href = \"/"+position_id+"/unsave_job/\"><button class='btn btn-inroad-red' type='button' style = 'margin-right: 2px;'>Unsave</button></a>");
                         }
                    }
                });
            },
            failure: function(data) {
                alert("test");
            }
        });
    });
});