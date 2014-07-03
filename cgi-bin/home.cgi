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

my $cgi = CGI->new();
my $path = CFUN::getpath();
my $xml = XML::LibXML->new('1.0','UTF-8');
my $source = CFUN::getDB();

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

my $ptrlinksn = $source->findnodes("/root/posts/news/item[position() >= last() - 2]");
my $ptrlinksi = $source->findnodes("/root/posts/interviste/intervista[position() >= last() - 2]");
my $ptrlinksr = $source->findnodes("/root/posts/recensioni/recensione[position() >= last() - 2]");




print $cgi->header({-type=>'text/html', -charset=>'utf-8'});
print CFUN::printHead("Home - Music Break","musica, news, news musicali, notizie, album","/javascript/resources/jquery-2.1.1.min.js" ,"/javascript/screen.js");
print CFUN::printHeader(0);
print CFUN::printNav('h');
print "<div id='sidebar'>
        <a class='help' href='#contents_home'>salta sidebar</a>
        <h1>Ultime <span xml:lang='en'>News</span></h1>
        <ol id='UlNews' class='box effect'>";
foreach my $link ($ptrlinksn->get_nodelist()){
		print "<li><a href='".$path."/cgi-bin/posts.cgi?post=".$link->findnodes("\@id")->get_node(1)->textContent."'>".$link->findnodes("titolo")->get_node(1)->textContent."</a></li>";
	}
print "</ol>
        <h1>Ultime Interviste</h1>
        <ol id='UlInterviste' class='box effect'>";
foreach my $link ($ptrlinksi->get_nodelist){
		print "<li><a href='".$path."/cgi-bin/posts.cgi?post=".$link->findnodes("\@id")->get_node(1)->textContent."'>".$link->findnodes("titolo")->get_node(1)->textContent."</a></li>";
	}
print "</ol>
        <h1>Ultime Recensioni</h1>
        <ol id='UlRecensioni' class='box effect'>";
foreach my $link ($ptrlinksr->get_nodelist){
		print "<li><a href='".$path."/cgi-bin/posts.cgi?post=".$link->findnodes("\@id")->get_node(1)->textContent."'>".$link->findnodes("titolo")->get_node(1)->textContent."</a></li>";
	}
print "</ol>
        </div>";
print "
<div id='breadcrumb'>
			<ul>
				<li>Home</li>
			</ul>
		</div>
<div id='contents_home'>
		<a class='help' href='#footer'>salta il contenuto</a><ul>";
foreach my $post ($ptrposts->get_nodelist){
			my $ribbon='';
			if($post->nodeName eq 'intervista'){
				$ribbon="<a href='$path/cgi-bin/show.cgi?type=i' class='ribbon intervisteRibbon' >Interviste</a>";
			}elsif($post->nodeName eq 'recensione'){
				$ribbon="<a href='$path/cgi-bin/show.cgi?type=r' class='ribbon RecensioniRibbon' >Recensioni</a>";
			}elsif($post->nodeName eq 'evento'){
				$ribbon="<a href='$path/cgi-bin/show.cgi?type=e' class='ribbon eventRibbon' >Eventi</a>";
			}elsif($post->nodeName eq 'item'){
				$ribbon="<a href='$path/cgi-bin/show.cgi?type=n' class='ribbon newsRibbon' >News</a>";
			}
			print "
			<li class='article'>
			$ribbon
			<h1><a href='".$path."/cgi-bin/posts.cgi?post=".$post->findnodes("\@id")->get_node(1)->textContent."' title=\"vai all\' articolo - ".($post->findnodes("titolo")->get_node(1)->textContent)."\" >".$post->findnodes("titolo")->get_node(1)->textContent."</a></h1> 
			<span class='author'>di ".$post->findnodes("editore/nome")->get_node(1)->textContent." ".$post->findnodes("editore/cognome")->get_node(1)->textContent." ".$post->findnodes("data")->get_node(1)->textContent."</span>". 
			"<img src='".$path.$post->findnodes("foto/src/node()")->get_node(1)->textContent."' alt='".$post->findnodes("foto/alt/node()")->get_node(1)->textContent."' /> 
			<p>".$post->findnodes("excerpt")->get_node(1)->textContent."</p> 
			<a class='continua' href='$path/cgi-bin/posts.cgi?post=".$post->findnodes("\@id")->get_node(1)->textContent."' title=\"continua a leggere l\' articolo - ".$post->findnodes("titolo")->get_node(1)->textContent."\" >continua →</a>". 
			CFUN::printTags($post).
			"<div class='nav_help'><a href='#header'>torna su</a></div>
			</li>";
		}

print "</ul><div class='nav_help'><a href='#header'>torna su</a></div>
	</div>";
print CFUN::printFooter();

