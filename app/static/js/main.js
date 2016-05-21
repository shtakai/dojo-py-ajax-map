$(document).ready(function() {
  console.log('emit');
  $('form').submit(function() {
    console.log('submit-', $(this));
    $('#result').html('<img src="/static/img/default.gif">');
    // load up any gif you want, this will be shown while user is waiting for response
    $.post($(this).attr('action'), $(this).serialize(), function(res) {
      // pay careful attention to the response object
      console.log('the response object:');
      console.log(res);
      var html_string = "";
      if(res.results.length !== 0) {
        html_string = "<video controls src='" + res.results[0].previewUrl + "'><\/video>";
      } else {
        html_string = "Not Found";
      }
      console.log('the html string:');
      console.log(html_string);
      $('#result').html(html_string);
    }, 'json');
    // don't forget, without it the page will refresh
    return false;
  });
});
