function error_cb(error) {
  console.log(error);
}

/* follow and unfollow */

function follow_user(success_cb, error_cb, type) {
  var follow_profile_pk = $(this).closest('.follow__card').attr('id')
                        || $(this).attr('id');
  console.log(follow_profile_pk);

  $.ajax({
    type: "POST",
    url: '/feed/follow_toggle/',
    data: {
      follow_profile_pk: follow_profile_pk,
      type: type
    },
    success: function(data) { success_cb(data); },
    error: function(error) { error_cb(error); }
  });
}


function update_follow_view(data) {
  console.log('data',data);
  var $button = $('.follow__card#' + data.follow_profile_pk
                + ' .btn, .profile .follow-toggle__container .btn');
  $button.addClass('unfollow-user').removeClass('follow-user');
  $button.text('Following');
}

function update_unfollow_view(data) {
  console.log('data',data);
  var $button = $('.follow__card#' + data.follow_profile_pk
                + ' .btn, .profile .follow-toggle__container .btn');
  $button.addClass('follow-user').removeClass('unfollow-user');
  $button.text('Follow');
}


$('.follow-toggle__container').on('click', '.follow-user', function() {
  follow_user.call(this, update_follow_view, error_cb, 'follow');
});

$('.follow-toggle__container').on('click', '.unfollow-user', function() {
  follow_user.call(this, update_unfollow_view, error_cb, 'unfollow');
});
