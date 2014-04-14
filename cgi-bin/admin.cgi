#!/usr/bin/perl -w

use strict;
use warnings;
use XML::LibXSLT;
use XML::LibXML;
use CGI qw/:standard/;
use CGI::Session;
use CGI::Carp qw(warningsToBrowser fatalsToBrowser);
use CFUN;

my $cgi = CGI->new();

my $errmsg;
if (defined $cgi->param('err')){
	$errmsg=$cgi->param('err');
}

print $cgi->header({-type=>'text/html', -charset=>'UTF-8'});
print CFUN::printHead("Login - Music Break","musica, news, news musicali, notizie, album");#,"/javascript/backend.js");
print CFUN::printHeader();
print "
    <div class='common_box'>
      <h1>Pagina di <span xml:lang='en'>Login</span></h1>
    </div>
    <div class='common_box'>
        <form action='/tecweb/~fros/cgi-bin/login.cgi' enctype='multipart/form-data' method='post' onsubmit='return checkLogin();'>
        <fieldset id='formfield'> 
           <label for='username'><span xml:lang='en'>Username: </span></label>
           <div><input type='text' name='username' id='username' onclick='Wbar('username');' onblur='Bbar('username');' value='inserire username...'/></div>
           <label for='password'><span xml:lang='en'>Password: </span></label>
           <div><input type='password' name='password' id='password' value='inserire password...' onclick='Wbar('password');' onblur='Bbar('password');' /></div>
           <input type='submit' value='Accedi' />
        </fieldset>
        </form>
    </div>";
print CFUN::printFooter;
