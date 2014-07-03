#!/usr/bin/perl -w

#script per la ricerca di un determinato tag
use strict;
use warnings;
use utf8;
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


print $cgi->header({-type=>'text/html', -charset=>'utf-8'});
print CFUN::printHead("Ricerca per il tag $tag - Music Break","musica, news, news musicali, notizie, album","/javascript/resources/jquery-2.1.1.min.js","/javascript/screen.js");
print CFUN::printHeader(1);
print CFUN::printNav();
print "
<div id='breadcrumb'>
    <ul>
	<li><a href='home.cgi'>Home&gt;&gt;</a></li>
	<li>Ricerca per il tag</li>
    </ul>
</div>
<div id='contents'>
<a class='help' href='#footer'>salta il contenuto</a>";
foreach my $post ($ptrposts->get_nodelist){
    print "<div class='article'>
      <h1><a href='posts.cgi?post=".$post->findnodes("\@id")->get_node(1)->textContent."'>".$post->findnodes("titolo")->get_node(1)->textContent."</a></h1>
	<img src='".$path.$post->findnodes("foto/src/node()")->get_node(1)->textContent."' alt='".$post->findnodes("foto/alt/node()")->get_node(1)->textContent."' />".
	CFUN::printTags($post)."</div>";
}
print "</div>";
print CFUN::printFooter();
