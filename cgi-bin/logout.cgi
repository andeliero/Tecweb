#!/usr/bin/perl -w

use strict;
use warnings;
use utf8;
use XML::LibXSLT;
use XML::LibXML;
use CGI qw/:standard/;
use CGI::Session;
use CGI::Carp qw(warningsToBrowser fatalsToBrowser);
use CFUN;


CFUN::destroySession();
CFUN::redir("/cgi-bin/login.cgi");