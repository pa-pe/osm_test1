#!/usr/bin/perl

use strict;
use warnings;
use CGI;
#use CGI::Carp qw(fatalsToBrowser);
use Template;

my $cgi = CGI->new;
my $tt = Template->new;
print $cgi->header(-type => 'text/html', -charset => 'utf-8');

my $template_data = {
    title => "Demo of OSM API via Perl backend",
#    cgi_version => "CGI version: ".$CGI::VERSION,
};

$tt->process(\*DATA, $template_data) || die $tt->error();

__DATA__
<!DOCTYPE html>
<html>
<head>
    <title>[% title %]</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" crossorigin="anonymous">
    <!-- link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/bootstrap-icons/1.11.3/font/bootstrap-icons.min.css" / -->
    <link rel="stylesheet" href="/css/style.css">
</head>
<body>
    <div class="container mt-5">

        <div class="row">
            <div class="col">

                <div class="accordion" id="descr_accordion">
 <div class="accordion-item">
    <h2 class="accordion-header">
      <button class="accordion-button collapsed" type="button" data-bs-toggle="collapse" data-bs-target="#collapse_descr" aria-expanded="true" aria-controls="collapseOne">
        Page description (tap to open/close)
      </button>
    </h2>
    <div id="collapse_descr" class="accordion-collapse collapse" data-bs-parent="#descr_accordion">
      <div class="accordion-body">
This is a demonstration project, it allows you to obtain geo-data based on an address and vice versa. The following technologies were used for implementation:<br>
<ul>
  <li>Fron-end:</li>
  <ul>
    <li>HTML+CSS</li>
    <li>Bootstrap 5 - for adaptive layout</li>
    <li>jQuery (also ajax queryes to server with JQ)</li>
  </ul>
  <li>Back-end on Perl with standart modules:</li>
  <ul>
    <li>CGI - Handle Common Gateway Interface</li>
    <li>Template Toolkit - as a basic system for separating algorithms and page layout code.</li>
    <li>LWP - for API requests</li>
    <li>JSON - for parsing API responses and ajax communications with front-end </li>
    <li>Encode - to support locales when interacting with APIs</li>
  </ul>
  <li>OSM API (OpenStreetMap)</li>
</ul>
<p>From an optimization point of view, the best solution would be to route all requests to OpenAPI directly on the client side to reduce the load on the server. But because APIs often use access keys, which for security reasons should be hidden on the server side, this project demonstrates exactly this principle - demonstrating the interaction of the client with the API through the server.</p>
<p>Server side: Apache on Linux on VPS (virtual private server)</p>
<p>GitHub: <a href="https://github.com/pa-pe/osm_test1" target="_blank">https://github.com/pa-pe/osm_test1</a></p>
</ul>

      </div>
    </div>
  </div>
                </div>

            </div>
        </div>
        <div class="row">
            <div class="col-md-6 work_block">

                <h2>Get geo by address</h2>
                <form class="form-inline query-form">
                    <div class="row" id="address-block">
                        <div class="col-10">
                            <input type="text" class="form-control" name="address" placeholder="Enter address">
                        </div>
                        <div class="col-2 text-end">
                            <button type="submit" class="btn btn-primary">Submit</button>
                        </div>
                    </div>
                </form>

<br>
                <div class="error d-none">
                </div>
                <div class="result d-none"></div>
<br>
                <div class="accordion d-none" id="result_accordion1">
 <div class="accordion-item">
    <h2 class="accordion-header">
      <button class="accordion-button collapsed" type="button" data-bs-toggle="collapse" data-bs-target="#collapseOne" aria-expanded="true" aria-controls="collapseOne">
        OSM API answer
      </button>
    </h2>
    <div id="collapseOne" class="accordion-collapse collapse" data-bs-parent="#result_accordion1">
      <div class="accordion-body">
                        <div class="result_raw"></div>
      </div>
    </div>
  </div>
                </div>

            </div>
            <div class="col-md-6 work_block">

                <h2>Get address by geo</h2>
                <form class="form-inline query-form">
                    <div class="row" id="address-block">
                        <div class="col-5">
                            <input type="text" class="form-control" name="lat" placeholder="Latitude">
                        </div>
                        <div class="col-5">
                            <input type="text" class="form-control" name="lon" placeholder="Longitude">
                        </div>
                        <div class="col-2 text-end">
                            <button type="submit" class="btn btn-primary">Submit</button>
                        </div>
                    </div>
                </form>

<br>
                <div class="error d-none">
                </div>
                <div class="result d-none"></div>
<br>
                <div class="accordion d-none" id="result_accordion2">
 <div class="accordion-item">
    <h2 class="accordion-header">
      <button class="accordion-button collapsed" type="button" data-bs-toggle="collapse" data-bs-target="#collapse2" aria-expanded="true" aria-controls="collapseOne">
        OSM API answer
      </button>
    </h2>
    <div id="collapse2" class="accordion-collapse collapse" data-bs-parent="#result_accordion2">
      <div class="accordion-body">
                        <div class="result_raw"></div>
      </div>
    </div>
  </div>
                </div>

            </div>

        </div>
    </div>

    <script src="https://code.jquery.com/jquery-3.7.1.min.js" integrity="sha256-/JqT3SQfawRcv/BIHPThkBvs0OEvtFFmqPF/lYI/Cxo=" crossorigin="anonymous"></script>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-YvpcrYf0tY3lHB60NNkmXc5s9fDVZLESaAA55NDzOxhy9GkcIdslK1eN7N6jIeHz" crossorigin="anonymous"></script>
    <script src="/js/script.js"></script>
</body>
</html>
