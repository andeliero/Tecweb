#!/usr/bin/perl -w

use strict;
use warnings;
use utf8;
use XML::LibXSLT;
use XML::LibXML;
use CGI qw/:standard/;
use CGI::Session;
use CGI::Carp qw(warningsToBrowser fatalsToBrowser);
use Time::localtime;
use CFUN;

my $path = CFUN::getpath();
my $cgi = CGI->new();
my $xml = XML::LibXML->new();
my $xslt = XML::LibXSLT->new();
my $DBpath = "../data/XML/DBsite.xml";
my $source = XML::LibXML->load_xml(location => $DBpath);


my $idutente=CFUN::getSession();
if (defined $cgi->param('delete')) {
	CFUN::deletepost($cgi->param('delete'),$source);
	open(OUT,">$DBpath");
	print OUT $source->toString;
	close(OUT);
}


my $ptrposts = $source->findnodes("/root/posts//idautore[text()='$idutente']/..");

my $aux;
my $size =$ptrposts->size();


print $cgi->header({-type=>'text/html', -charset=>'UTF-8'});
print CFUN::printHead("Admin SEZIONE PRIVATA- Music Break","musica, news, news musicali, notizie, album","/javascript/backend.js");
print CFUN::printHeader(1);
print CFUN::printAdminNav('d');
print "<div id='contents'>
        <div class='common_box'><h1>Rimozione dei propri contenuti</h1></div>
        <a class='help' href='#nav_pagine'>salta il contenuto</a>";
if(!$size){
    print "<h1>La ricerca non ha restituito risultati</h1><div id='spacer'></div>";   
}else{
    print "<ul id='elencoArticoliCancellazione'>";
    foreach my $post ($ptrposts->get_nodelist){
        print "<li class='article'>
                <h2>".$post->findnodes("titolo")->get_node(1)->textContent."</h2>
                <img src='".$path.$post->findnodes("foto/src/node()")->get_node(1)->textContent."' alt='".$post->findnodes("foto/alt/node()")->get_node(1)->textContent."'/>
                <a href='".$path."/cgi-bin/deletepost.cgi?delete=".$post->findnodes("\@id")->get_node(1)->textContent."'>Cancella articolo</a>
                </li>";
    }
    print "</ul>";
}
print "</div>";
print CFUN::printFooter;
