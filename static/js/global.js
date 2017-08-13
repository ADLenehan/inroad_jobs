$(function () {

    //Append CSRF token to each internal ajax request
    $.ajaxSetup({
        beforeSend: function (xhr, settings) {
            function getCookie(name) {
                var cookieValue = null;
                if (document.cookie && document.cookie != '') {
                    var cookies = document.cookie.split(';');
                    for (var i = 0; i < cookies.length; i++) {
                        var cookie = jQuery.trim(cookies[i]);
                        // Does this cookie string begin with the name we want?
                        if (cookie.substring(0, name.length + 1) == (name + '=')) {
                            cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                            break;
                        }
                    }
                }
                return cookieValue;
            }

            if (!(/^http:.*/.test(settings.url) || /^https:.*/.test(settings.url))) {
                // Only send the token to relative URLs i.e. locally.
                xhr.setRequestHeader("X-CSRFToken", getCookie('csrftoken'));
            }
        }
    });


    $('#social_post_modal').on('show.bs.modal', function (event) {
        var button = $(event.relatedTarget);
        var social_auth_type = button.data('social-auth-type');
        var social_auth_uid = button.data('social-auth-uid');
        var social_auth_token = button.data('social-auth-token');
        var position_id = button.data('position-id');

        var modal = $(this);
        var modal_title = modal.find('#social_post_modal_label');

        if (social_auth_type == 'facebook') {

            modal_title.text('New Facebook Posts');

        } else if (social_auth_type == 'linkedin-oauth2') {

            modal_title.text('New Linkedin Post');
        }

        modal.find('#post_text').val('');
        modal.find('#post_headline').val('');
        modal.find('#social_auth_type').val(social_auth_type);
        modal.find('#social_auth_uid').val(social_auth_uid);
        modal.find('#social_auth_token').val(social_auth_token);
        modal.find('#position_id').val(position_id);
    });
});

function social_post(el) {

    post_form = $(el).closest('form[name="social_post_form"]');
    post_text = post_form.find('#post_text').val();
    post_headline = post_form.find('#post_headline').val();
    social_auth_type = post_form.find('#social_auth_type').val();
    social_auth_uid = post_form.find('#social_auth_uid').val();
    social_auth_token = post_form.find('#social_auth_token').val();
    position_id = post_form.find('#position_id').val();
    domain = post_form.find('#domain').val();

    var position_link = domain + "/application/" + position_id;

    if (social_auth_type == 'facebook') {
        postPositionFacebook(social_auth_uid, social_auth_token, position_id, post_text, post_headline, position_link);
    }
    else if (social_auth_type == 'linkedin-oauth2') {
        //postPositionLinkedin(social_auth_uid, social_auth_token, position_id, post_text, position_link);

        $.ajax({
            type: "POST",
            url: "/social_post/",
            data: {
                social_auth_uid: social_auth_uid,
                social_auth_token: social_auth_token,
                social_auth_type: social_auth_type,
                position_id: position_id,
                post_text: post_text,
                post_headline: post_headline,
                position_link: position_link
            },
            success: function (json) {

                var social_post_modal = $('#social_post_modal');
                var social_post_success_modal = $('#social_post_success_modal');
                var social_post_fail_modal = $('#social_post_fail_modal');

                if (json.response == 'success') {

                    social_post_success_modal.find("input[name='social_post_link']").val(json.link);
                    social_post_modal.modal('hide');
                    social_post_success_modal.modal('show');

                } else {
                    social_post_modal.modal('hide');
                    social_post_fail_modal.modal('show');
                }
            }
        });
    }
}