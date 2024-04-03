$(document).ready(function() {
    $('#address-form').submit(function(event) {
        event.preventDefault(); // Prevent default form submission behavior

        // Get the address value from the input field
        var address = $('#address-input').val();

        // Send an AJAX request to the server
        $.ajax({
            url: '/cgi-bin/osm_test1/osm_gate.cgi',
            method: 'POST',
            data: {address: address},
            dataType: 'json',
            success: function(response) {
//console.log(response);

                // Display latitude and longitude in the result element
//                $('#result').html('Latitude: ' + response.result.latitude + '<br>Longitude: ' + response.result.longitude);
                $('#result').html(response.result.prepared_results);
                // Display the full response in the result_raw element with proper formatting
                var jsonResponse = JSON.parse(response.result.raw_response);
                $('#result_raw').html('<pre>' + JSON.stringify(jsonResponse, null, 2) + '</pre>');

                // unhide results
                $('.results').removeClass('d-none');
            },
            error: function() {
                $('#result').text('Error executing request');
                $('#result_raw').text('');
            }
        });
    });
});
