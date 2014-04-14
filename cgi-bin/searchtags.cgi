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
my $xml = XML::LibXML->new();
my $DBpath = "../data/XML/DBsite.xml";
my $source = XML::LibXML->load_xml(location => $DBpath);


my $tag;
if (defined $cgi->param('tag')){
	my $str = $cgi->param('tag');
	$tag = CFUN::searchidtag($str,$source);
}
if (defined $cgi->param('idtag')) {
	$tag=$cgi->param('idtag');
}

my $ptrposts = $source->findnodes("/root/posts//tag[text()='$tag']/..");

foreach my $post ($ptrposts->get_nodelist){
	my $ptridtags = $post->findnodes('tag');
	foreach my $ptridtag ($ptridtags->get_nodelist){
		my $idtag = $ptridtag->textContent;
		my $ptrtag = $source->findnodes("/root/tags/tag[\@id='$idtag']")->get_node(1);
		my $newnodotag = $ptrtag->cloneNode(1);
		$ptridtag->replaceNode($newnodotag);
	}
}


print $cgi->header({-type=>'text/html', -charset=>'UTF-8'});
print CFUN::printHead();
print CFUN::printHeader();
print CFUN::printNav();
print "<div id='contents'>
		<h1>Ricerca per il tag</h1>
		<a class='help' href='#footer'>salta il contenuto</a>";
foreach my $post ($ptrposts->get_nodelist){
	print "<div class='article'>
					<h2><a href='posts.cgi?post=".$post->findnodes("\@id")->get_node(1)->textContent."'>".$post->findnodes("titolo")->get_node(1)->textContent."</a></h2>
					<img src='".$path.$post->findnodes("foto/src/node()")->get_node(1)->textContent."' alt='".$post->findnodes("foto/alt/node()")->get_node(1)->textContent."' />".
					CFUN::printTags($post).
					"</div>";
}
print "</div>";
print CFUN::printFooter();
