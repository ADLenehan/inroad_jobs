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
        $.ajax({
            url: position_id+'/comments',
            type: 'get',
            dataType: 'json',
            success: function (data) {
                $.each(data.results, function(index, element) {
                    $('#comments').append("<div class='card-block'>"+element.text+element.author+"</div>");
                });
            },
            failure: function(data) {
                alert('Got an error dude');
            }
        });
    });
});