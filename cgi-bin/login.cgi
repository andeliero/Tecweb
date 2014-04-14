#!/usr/bin/perl -w

use strict;
use warnings;
use XML::LibXSLT;
use XML::LibXML;
use CGI qw/:standard/;
use CGI::Session;
use CGI::Carp qw(warningsToBrowser fatalsToBrowser);
use CFUN;

my $path = CFUN::getpath();
my $cgi = CGI->new();
my $parser = XML::LibXML->new();
my $xslt = XML::LibXSLT->new();

my $DBpath = "../data/XML/Amministratori.xml";
my $source = XML::LibXML->load_xml(location => $DBpath);

my $username;
my $password;

if (defined $cgi->param('username')){
	$username = $cgi->param('username');
}
if (defined $cgi->param('password')){
	$password = $cgi->param('password');
}

my $ptradmins = $source->findnodes("/amministratori/admin");
my $found = 0;
my $ptruser;
for (my $var = 0; $var < $ptradmins->size() && !$found; $var++) {
	my $user = $ptradmins->get_node($var);
	my $name = $user->findnodes("username")->get_node(1)->textContent;
	if ($name eq $username){
		$ptruser=$user;
		$found=1;
	}
}

my $rdr;
if($found == 1){
	my $pass = $ptruser->findnodes("password")->get_node(1)->textContent;
	if($password eq $pass){
		my $attruser = $ptruser->findnodes("\@id")->get_node(1)->textContent;
		my $session = new CGI::Session(undef, $cgi, {Directory=>"../data/tmp"});
		$session->param('userid', $attruser);

		$rdr ="/cgi-bin/adminbk.cgi?type=n";
	}else{
		$rdr ="/cgi-bin/admin.cgi?err=password%20sbagliata";
	}
}else{
	$rdr ="/cgi-bin/admin.cgi?err=username%20sbagliato";
}

print $cgi->header({-type=>'text/html', -charset=>'UTF-8'});
CFUN::redir($rdr);
