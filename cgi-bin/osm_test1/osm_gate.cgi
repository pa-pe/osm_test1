#!/usr/bin/perl

use strict;
use warnings;
use CGI;
use Encode;
use LWP::UserAgent;
use JSON;

my $cgi = CGI->new;

my $address = $cgi->param('address');

# Send a request to the OpenStreetMap server to get coordinates
my $ua = LWP::UserAgent->new;
my $url = "https://nominatim.openstreetmap.org/search?q=$address&format=json&accept-language=en";
my $response = $ua->get($url);

my $result;
if ($response->is_success) {
    my $decoded_content = decode('utf-8', $response->decoded_content);
    my $data = JSON->new->decode($decoded_content);
    if (@$data) {
        my $location = $data->[0];

        my $prepared_results = << "[END]";
<b>$location->{display_name}</b><br>
Latitude: $location->{lat}<br>
Longitude: $location->{lat}<br>
[END]

        $result = {
#            name => $location->{name},
#            latitude => $location->{lat},
#            longitude => $location->{lon},
            prepared_results => $prepared_results,
            raw_response => $decoded_content
        };
    } else {
        $result = { error => "Address not found" };
    }
} else {
    $result = "Error requesting data from OpenStreetMap server";
}

# Output the result in JSON format
print $cgi->header(-type => 'application/json', -charset => 'utf-8');
print encode_json({result => $result});
