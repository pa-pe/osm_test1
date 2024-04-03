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
    title => "Hello ;)",
#    cgi_version => "CGI version: ".$CGI::VERSION,
};

$tt->process(\*DATA, $template_data) || die $tt->error();

__DATA__
<!DOCTYPE html>
<html>
<head>
    <title>[% title %]</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" crossorigin="anonymous">
    <link rel="stylesheet" href="/css/style.css">
</head>
<body>
    <div class="container mt-5">
        <div class="row">
            <div class="col-md-6">
                <h2>Get geo by address</h2>
                <form id="address-form" class="form-inline">
                    <div class="row" id="address-block">
                        <div class="col-10">
                            <input type="text" class="form-control" id="address-input" placeholder="Enter address">
                        </div>
                        <div class="col-2 text-end">
                            <button type="submit" class="btn btn-primary">Submit</button>
                        </div>
                    </div>
                </form>

<br>
                <div class="results d-none">
                    <div id="result"></div>
<br>
                    <div class="accordion" id="result_accordion">

 <div class="accordion-item">
    <h2 class="accordion-header">
      <button class="accordion-button collapsed" type="button" data-bs-toggle="collapse" data-bs-target="#collapseOne" aria-expanded="true" aria-controls="collapseOne">
        OSM API answer
      </button>
    </h2>
    <div id="collapseOne" class="accordion-collapse collapse" data-bs-parent="#accordionExample">
      <div class="accordion-body">
                        <div id="result_raw"></div>
      </div>
    </div>
  </div>

                    </div>
                </div>
            </div>
            <div class="col-md-6">
                <!-- Another block (if needed) -->
            </div>
        </div>
    </div>

    <script src="https://code.jquery.com/jquery-3.7.1.min.js" integrity="sha256-/JqT3SQfawRcv/BIHPThkBvs0OEvtFFmqPF/lYI/Cxo=" crossorigin="anonymous"></script>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-YvpcrYf0tY3lHB60NNkmXc5s9fDVZLESaAA55NDzOxhy9GkcIdslK1eN7N6jIeHz" crossorigin="anonymous"></script>
    <script src="/js/script.js"></script>
</body>
</html>
