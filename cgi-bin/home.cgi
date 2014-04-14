#!/usr/bin/perl -w

use strict;
use warnings;
use XML::LibXSLT;
use XML::LibXML;
use CGI qw/:standard/;
use CGI::Session;
use CGI::Carp qw(warningsToBrowser fatalsToBrowser);
use Time::localtime;
use CFUN;

my $cgi = CGI->new();
my $path = CFUN::getpath();
my $xml = XML::LibXML->new();
my $DBpath = "../data/XML/DBsite.xml";
my $source = XML::LibXML->load_xml(location => $DBpath);

my $ptrposts = $source->findnodes("/root/posts/*/*[last()]");
foreach my $post ($ptrposts->get_nodelist){
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

my $ptrlinksn = $source->findnodes("/root/posts/news/item[last() or last()-1 or last()-2]");
my $ptrlinksi = $source->findnodes("/root/posts/interviste/intervista[last() or last()-1 or last()-2]");
my $ptrlinksr = $source->findnodes("/root/posts/recensioni/recensione[last() or last()-1 or last()-2]");




print $cgi->header({-type=>'text/html', -charset=>'UTF-8'});
print CFUN::printHead("Home - Music Break","musica, news, news musicali, notizie, album","/javascript/screen.js");
print CFUN::printHeader();
print CFUN::printNav('h');
print "<div id='sidebar'>
        <a class='help' href='#contents_home'>salta sidebar</a>
        <h1>Ultime <span xml:lang='en'>News</span></h1>
        <ol id='UlNews' class='box effect'>";
foreach my $link ($ptrlinksn->get_nodelist){
		print "<li><a href='".$path."posts.cgi?post=".$link->findnodes("\@id")->get_node(1)->textContent."'>".$link->findnodes("titolo")->get_node(1)->textContent."</a></li>";
	}
print "</ol>
        <h1>Ultime Interviste</h1>
        <ol id='UlInterviste' class='box effect'>";
foreach my $link ($ptrlinksi->get_nodelist){
		print "<li><a href='".$path."posts.cgi?post=".$link->findnodes("\@id")->get_node(1)->textContent."'>".$link->findnodes("titolo")->get_node(1)->textContent."</a></li>";
	}
print "</ol>
        <h1>Ultime Recensioni</h1>
        <ol id='UlRecensioni' class='box effect'>";
foreach my $link ($ptrlinksr->get_nodelist){
		print "<li><a href='".$path."posts.cgi?post=".$link->findnodes("\@id")->get_node(1)->textContent."'>".$link->findnodes("titolo")->get_node(1)->textContent."</a></li>";
	}
print "</ol>
        </div>";
print "<div id='contents_home'>
		<h1>Ricerca per il tag</h1>
		<a class='help' href='#footer'>salta il contenuto</a>";
foreach my $post ($ptrposts->get_nodelist){
			print "
			<div class='article'>
			<h2><a href='".$path."/cgi-bin/posts.cgi?post=".$post->findnodes("\@id")->get_node(1)->textContent."'>".$post->findnodes("titolo")->get_node(1)->textContent."</a></h2> 
			<span class='author'>di ".$post->findnodes("editore/nome")->get_node(1)->textContent." ".$post->findnodes("editore/cognome")->get_node(1)->textContent." ".$post->findnodes("data")->get_node(1)->textContent."</span>". 
			"<img src='".$path.$post->findnodes("foto/src/node()")->get_node(1)->textContent."' alt='".$post->findnodes("foto/alt/node()")->get_node(1)->textContent."' /> 
			<p>".$post->findnodes("excerpt")->get_node(1)->textContent."</p> 
			<a class='continua' href='$path/cgi-bin/posts.cgi?post=".$post->findnodes("\@id")->get_node(1)->textContent."'>continua →</a>". 
			CFUN::printTags($post).
			"</div>";
		}
print "</div>";
print CFUN::printFooter();

