#!/usr/bin/perl -w

use strict;
use warnings;
use XML::LibXSLT;
use XML::LibXML;
use CGI qw/:standard/;
use CGI::Session;
use CGI::Carp qw(warningsToBrowser fatalsToBrowser);

my $page = CGI->new();
my $rdr;
my $session = CGI::Session->load();
my $SID = $session->id();
$session->close();
$session->delete();
$session->flush();
$rdr ="admin.cgi?err=logout%20eseguito%20con%20successo";


print $page->header({-type=>'text/html', -charset=>'UTF-8'});
print $page->start_html(
	-title => "Logout - Music Break",
	-head => meta({-http_equiv => 'refresh',-content=> "0;url=$rdr"}),
	-dtd => ['-//W3C//DTD XHTML 1.0 Strict//EN','http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd'],
	-lang => 'it'
	);

print $page->end_html;