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
my $xslt = XML::LibXSLT->new();

my $DBpath = "../data/XML/DBsite.xml";

my $idPost = $cgi->param('post');


my $source = XML::LibXML->load_xml(location => $DBpath);

my $posttype = substr($idPost, 0, 1);
my $vincolo=CFUN::getvincpath($posttype);
my $style_path=CFUN::getxslpath($posttype);


#individuo il post
my $ptrpost = $source->findnodes("/root/posts/".$vincolo."[\@id='$idPost']")->get_node(1);

#individio l'autore del post
my $ptridautor = $ptrpost->findnodes("idautore")->get_node(1);
my $idautor = $ptridautor->textContent;
my $ptrautor = $source->findnodes("/root/editori/editore[\@id='$idautor']")->get_node(1);
$ptridautor->replaceNode($ptrautor);


#individuo i tags che mi interessano
my $tags = $source->findnodes("/root/tags")->get_node(1);
my $ptridtags = $ptrpost->findnodes("tag");

foreach my $ptrtag ($ptridtags->get_nodelist){
	my $valtag = $ptrtag->textContent;
	my $tagname = $tags->findnodes("tag[\@id=$valtag]")->get_node(1);
	my $newtagnode = $tagname;
	$ptrtag->replaceNode($newtagnode);
}
$ptridtags=$ptrpost->findnodes("tag");
my $texttags ='';
foreach my $ptrtag ($ptridtags->get_nodelist){
	$texttags.= $ptrtag->textContent." ";
}

#aggiungo la galleria ad una eventuale intervista
if ("$posttype" eq 'i'){
	my $ptridgallery = $ptrpost->findnodes("galleria")->get_node(1);
	my $idgallery = $ptridgallery->textContent;
	my $ptrgallery = $source->findnodes("/root/gallerie/galleria[\@id='$idgallery']")->get_node(1);
	$ptridgallery->replaceNode($ptrgallery);
}

#stampo la pagina
print $cgi->header({-type=>'text/html', -charset=>'UTF-8'});
my $style_doc =XML::LibXML->load_xml(location=>$style_path);
my $stylesheet = $xslt->parse_stylesheet($style_doc);
my $results = $stylesheet->transform($ptrpost);
print $stylesheet->output_as_bytes($results);
