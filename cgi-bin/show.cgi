#!/usr/bin/perl -w

use strict;
use warnings;
use XML::LibXSLT;
use XML::LibXML;
use CGI qw/:standard/;
use CGI::Session;
use CGI::Carp qw(warningsToBrowser fatalsToBrowser);
use CFUN;

my $path=CFUN::getpath();
my $cgi = CGI->new();
my $parser = XML::LibXML->new();
my $DBpath = "../data/XML/DBsite.xml";
my $source = XML::LibXML->load_xml(location => $DBpath);

my $type = $cgi->param('type');
my $pag = 1;
if (defined $cgi->param('pag')){
	$pag = $cgi->param('pag');
}
my %in= ( 'type' => $type);
$pag=$pag-1;



my $posttype = substr($type, 0, 1);
my $title;
my $vincolo;
if ($posttype eq "e") {
	$vincolo = "eventi/evento";
	$title = "Eventi";
}elsif ($posttype eq "r") {
	$vincolo = "recensioni/recensione";
	$title = "Recensioni";
}elsif ($posttype eq "i"){
	$vincolo = "interviste/intervista";
	$title = "Intervista";
}elsif ($posttype eq "n"){
	$vincolo = "news/item";
	$title = "News";
}

my $dom = XML::LibXML::Document->new( "1.0", "UTF-8");
my $ptrposts = $source->findnodes("/root/posts/".$vincolo);
my $radice = $parser->parse_balanced_chunk("<posts></posts>","UTF-8");
my $ptrradice = $radice->findnodes("posts")->get_node(1);
$dom->setDocumentElement($ptrradice,"UTF-8");
my $ptrdompost =$dom->findnodes("/posts")->get_node(1);


#estraggo 4 post a seconda della pagina
for (my $var = $ptrposts->size()-($pag*4); $var>0 && $var>($ptrposts->size()-(($pag+1)*4)); $var--) {#nel caso che voglia vedere 4 articoli in una pagina
	my $ptrpost = $ptrposts->get_node($var);
	$ptrpost->setNodeName('post');
	$ptrdompost->addChild($ptrpost);
}


#individio l'autore del post
my $posts = $dom->findnodes("/posts/post");
my $end=$posts->size()/4;
foreach my $post ($posts->get_nodelist){
	my $ptridautor = $post->findnodes('idautore')->get_node(1);
	my $idautor = $ptridautor->textContent;
	my $ptrautor = $source->findnodes("/root/editori/editore[\@id='$idautor']")->get_node(1);
	my $newnodoautore = $ptrautor->cloneNode(1);
	$ptridautor->replaceNode($newnodoautore);
	my $ptridtags = $post->findnodes('tag');
	foreach my $ptridtag ($ptridtags->get_nodelist){
		my $idtag = $ptridtag->textContent;
		my $ptrtag = $source->findnodes("/root/tags/tag[\@id='$idtag']")->get_node(1);
		my $newnodotag = $ptrtag->cloneNode(1);
		$ptridtag->replaceNode($newnodotag);
	}
}


#stampo la pagina
print $cgi->header({-type=>'text/html', -charset=>'UTF-8'});
print CFUN::printHead("$title - Music Break","$title");
print CFUN::printHeader();
print CFUN::printNav($type);
print "<div id='contents'>
		<h1>$title</h1>
		<a class='help' href='#nav_pagine'>salta il contenuto</a>".
		CFUN::printPosts($dom,$type).
		"</div>";
print CFUN::printNavPag($pag,$type,1,$end);
print CFUN::printFooter();
