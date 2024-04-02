#!/usr/bin/perl

use strict;
use warnings;
use CGI;
use CGI::Carp qw(fatalsToBrowser);

my $cgi = CGI->new;

print $cgi->header,
      $cgi->start_html(
          -title => "OSM API test1",
          -style => {src => '/css/style.css'},
          -script => [{-type => 'text/javascript', -src => 'https://code.jquery.com/jquery-3.7.1.min.js'}]
      );

print $cgi->h1("Hello ;)");

print $cgi->end_html;
