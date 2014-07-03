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

my $cgi = CGI->new();
my $path = CFUN::getpath();

my $iu=CFUN::getSession();
if($iu ne undef){
  CFUN::redir("/cgi-bin/adminbk.cgi?type=n");
}

my $errmsg = '';
if (defined $cgi->param('err')){
	$errmsg="<p class='error'>".$cgi->param('err')."</p>";
}

print $cgi->header({-type=>'text/html', -charset=>'utf-8'});
print CFUN::printHead("Login - Music Break","musica, news, news musicali, notizie, album","/javascript/resources/jquery-2.1.1.min.js" ,"/javascript/backend.js","/javascript/screen.js");
print CFUN::printHeader(1);
print CFUN::printNav('l');
print "
    <div class='common_box'>
      <h1>Pagina di <span xml:lang='en'>Login</span></h1>
    </div>
    <div class='common_box'>
        <form action='$path/cgi-bin/checklogin.cgi' enctype='multipart/form-data' method='post' onsubmit='return checkLogin();'>
        <fieldset id='formfield'><legend class='hidelegend'>Form di Autenticazione</legend>
           <label for='username'><span xml:lang='en'>Username: </span></label>
           <div><input type='text' name='username' id='username' onclick='Wbar(\"username\");' onblur='Bbar(\"username\");' /></div>
           <label for='password'><span xml:lang='en'>Password: </span></label>
           <div><input type='password' name='password' id='password' onclick='Wbar(\"password\");' onblur='Bbar(\"password\");' /></div>
           <input type='submit' value='Accedi' />
           $errmsg
        </fieldset>
        </form>
    </div>";
print CFUN::printFooter;
