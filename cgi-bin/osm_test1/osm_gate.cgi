#!/usr/bin/perl

use strict;
use warnings;
use CGI;
use Encode;
use LWP::UserAgent;
use JSON;

my $cgi = CGI->new;

my $address = $cgi->param('address');
my $lat = $cgi->param('lat');
my $lon = $cgi->param('lon');

# Send a request to the OpenStreetMap server to get coordinates
my $result;
my $url = "";
if ($address){
    $url = "https://nominatim.openstreetmap.org/search?q=$address&format=json&accept-language=en";
} elsif($lat && $lon) {
    $url = "https://nominatim.openstreetmap.org/reverse?lat=$lat&lon=$lon&format=json&accept-language=en";
}

if ($url){
    my $ua = LWP::UserAgent->new;
    my $response = $ua->get($url);

    if ($response->is_success) {
        my $decoded_content = decode('utf-8', $response->decoded_content);
        my $data = JSON->new->decode($decoded_content);

        my $location;

        if (ref $data eq 'ARRAY' && @$data) {
            $location = $data->[0];
        } else {
            $location = $data;
        }

        my $prepared_results = "";
        if (ref $location eq 'HASH'){

            if ($location->{lat}){
                $prepared_results .= << "[END]";
<b>$location->{display_name}</b><br>
Latitude: $location->{lat}<br>
Longitude: $location->{lon}<br>
<a class="btn btn-success icon-link" href="https://www.google.com/maps?q=$location->{lat},$location->{lon}" target="_blank">
 Google Maps
</a><br>
[END]
            }

        } else {
            $prepared_results .= "Not found";
        }

        $result = {
            prepared_results => $prepared_results,
            raw_response => $decoded_content
        };
    } else {
        $result = { error => "Error requesting data from OpenStreetMap server" };
    }
} else {
    $result = { error => "params error" };
}

# Output the result in JSON format
print $cgi->header(-type => 'application/json', -charset => 'utf-8');
print encode_json({result => $result});
