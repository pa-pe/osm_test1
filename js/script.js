$(document).ready(function() {
    $('.query-form').submit(function(event) {
        event.preventDefault(); // Prevent default form submission behavior

        var formData = $(this).serializeArray();
        var work_block = $(this).parent('.work_block');
        var block_error = work_block.children('.error');
        var block_result = work_block.children('.result');
        var block_result_raw = work_block.find('.result_raw');
        var accordion = work_block.children('.accordion');



        // Send an AJAX request to the server
        $.ajax({
            url: '/cgi-bin/osm_test1/osm_gate.cgi',
            method: 'POST',
            data: formData,
            dataType: 'json',
            success: function(response) {
                if (response.result.error){
                    // Display server answer error
                    block_error.html(response.result.error).removeClass('d-none');

                    // Clear and hide result fields
                    block_result.html('').addClass('d-none');
                    block_result_raw.html('');
                    accordion.addClass('d-none');
                } else {
                    block_error.html('').addClass('d-none');

                    // Display server prepared results and unhide block
                    block_result.html(response.result.prepared_results).removeClass('d-none');

                    // Display the result_raw element with proper formatting
                    var jsonResponse = JSON.parse(response.result.raw_response);
                    block_result_raw.html('<pre>' + JSON.stringify(jsonResponse, null, 2) + '</pre>');
                    accordion.removeClass('d-none');
                }
            },
            error: function() {
                // Display error
                block_error.html('Error executing request').removeClass('d-none');

                // Clear and hide result fields
                block_result.html('').addClass('d-none');
                block_result_raw.html('');
                accordion.addClass('d-none');
            }
        });
    });
});
