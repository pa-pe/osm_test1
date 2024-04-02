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
    cgi_version => "CGI version: ".$CGI::VERSION,
};

$tt->process(\*DATA, $template_data) || die $tt->error();

__DATA__
<!DOCTYPE html>
<html>
<head>
    <title>[% title %]</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" crossorigin="anonymous">
    <link rel="stylesheet" href="/css/style.css">
    <script src="https://code.jquery.com/jquery-3.7.1.min.js" integrity="sha256-/JqT3SQfawRcv/BIHPThkBvs0OEvtFFmqPF/lYI/Cxo=" crossorigin="anonymous"></script>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-YvpcrYf0tY3lHB60NNkmXc5s9fDVZLESaAA55NDzOxhy9GkcIdslK1eN7N6jIeHz" crossorigin="anonymous"></script>
</head>
<body>
    <h1>[% title %]</h1>
    <p>[% cgi_version %]</p>
</body>
</html>
