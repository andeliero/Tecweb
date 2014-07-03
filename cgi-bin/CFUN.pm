#!/usr/bin/perl -w
package CFUN;
use strict;
use warnings;
use utf8;
use XML::LibXSLT;
use XML::LibXML;
use CGI qw/:standard/;
use CGI::Session;
use CGI::Carp qw(warningsToBrowser fatalsToBrowser);


my $path="/tecweb/~fros";
my $cgi = CGI->new();
my $xml = XML::LibXML->new('1.0','UTF-8');
my $xslt = XML::LibXSLT->new();
my $DBpath = "../data/XML/DBsite.xml";
my $source = XML::LibXML->load_xml(location => $DBpath);

sub getpath{
	return $path;
}

sub getDB{
	my $nls=$source->findnodes("//span");
	#sostituisco ogni <span lang='' /> con <span xml:lang='' />
	foreach my $node ($nls->get_nodelist()){
	    my $attr = $node->findnodes("./\@lang")->get_node(1)->textContent();
	    my $rn=printRawNode($node);
	    my $strnode = "<span xml:lang='$attr'>$rn</span>";
	    my $newnode=$xml->parse_balanced_chunk($strnode,"UTF-8");
	    $node->replaceNode($newnode);
	}
	return $source;
}

sub getvincpath{
	my $type = $_[0];
	my $vincolo;
	if ($type eq 'e') {
		$vincolo = "eventi/evento";
	}elsif ($type eq 'r') {
		$vincolo = "recensioni/recensione";
	}elsif ($type eq 'i'){
		$vincolo = "interviste/intervista";
	}elsif ($type eq 'n'){
		$vincolo = "news/item";
	}
	return $vincolo;
}

sub getTipologia{
    my $type=$_[0];
    if ($type eq 'e') {
		return "Eventi";
	}elsif ($type eq 'r') {
		return "Recensioni";
	}elsif ($type eq 'i'){
		return "Interviste";
	}elsif ($type eq 'n'){
		return "News";
	}
}

sub getxslpath{
	my $type = $_[0];
	my $style_path;
	if ($type eq 'e') {
		$style_path="../data/XSLT/Eventi.xsl";
	}elsif ($type eq 'r') {
		$style_path="../data/XSLT/Recensioni.xsl";
	}elsif ($type eq 'i'){
		$style_path="../data/XSLT/Interviste.xsl";
	}elsif ($type eq 'n'){
		$style_path="../data/XSLT/News.xsl";
	}
	return $style_path;
}

sub redir{ 
	my $rdr = $_[0];
	print $cgi->header({-type=>'text/html', -charset=>'UTF-8'});
	print "<!DOCTYPE html PUBLIC '-//W3C//DTD XHTML 1.0 Strict//EN' 'http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd'>
	<html xmlns='http://www.w3.org/1999/xhtml' xml:lang='it' lang='it'>
    	<head>
        	<meta http-equiv='Content-Type' content='text/html;charset=utf-8'></meta>
        	<meta http-equiv='refresh' content='0; URL=".$path.$rdr."' />
        	<meta name='author' content='Fabio Ros, Valerio Burlin, Stefano Munari, Alberto Andeliero'/>
	        <meta name='language' content='italian it'/>
		<meta name='rating' content='safe for kids' />
        	<meta name='description' content='Il portale di news, articoli, recensioni ed eventi dedicato alla musica'/>
	        <meta name='keywords' content='musica, news, news musicali, notizie, album'/>
	        <meta name='robots' content='all' />
	        <link rel='icon' href='/tecweb/~fros/img/fav.ico' type='image/icon' />
	        <title>Redirect</title>
	    </head><body><h1>Redirezione...</h1></body>
	</html>";
	exit 0;
}

sub isdef{
	my $par = $_[0];
	if(defined $cgi->param($par)){
		return my $param = $cgi->param($par);
	}else{ 
		return 0; 
	}
}

sub checkfile{
	my $file = $_[0];
	if (!$file) {
		redir("/cgi-bin/adminbk.cgi?msg=upfallito");
	}
	return;
}

sub scrivifile{
	my $file = $_[0];
	my $filename = $_[1];
	my $path = $_[2];
	open (UPLOADFILE,">", $path.$filename);
	while (<$file>){
		print UPLOADFILE;
	}
	close UPLOADFILE;
}

sub getfolderpath{
	my $type=$_[0];
	if($type eq 'n'){
		return "../public_html/img/news/";}
	if($type eq 'r'){
		return "../public_html/img/recensioni/";}
	if($type eq 'i'){
		return "../public_html/img/interviste/";}
	if($type eq 'e'){
		return "../public_html/img/eventi/";}
}

sub printNavPag{
	my $pagina = $_[0]+1;
	my $type = $_[1];
	my $inizio = $_[2];
	my $fine = $_[3];
	my $aux="<div id='nav_pagine'>";
	if ($pagina > $inizio){
		$aux .= "<a href='$path/cgi-bin/show.cgi?type=$type&amp;pag=1'> &#60; </a>";
		$aux .= "<a href='$path/cgi-bin/show.cgi?type=$type&amp;pag=".($pagina-1)."'>&#60; &#60;</a>";
	}
	$aux .= "<span>$pagina</span>";
	if ($pagina < $fine){
		$aux .= "<a href='$path/cgi-bin/show.cgi?type=$type&amp;pag=".($pagina+1)."'>&#62;</a>";
		$aux .= "<a href='$path/cgi-bin/show.cgi?type=$type&amp;pag=$fine'>&#62;&#62;</a>";
	}
	$aux.="</div>";
	return $aux;
}

sub printHead{
	my $title = $_[0];
	my $tags = "<meta name='keywords' content='$_[1]'/>";
	my $scriptpath = '';
	if(defined $_[2]){
		$scriptpath.="<script type='text/javascript' src='$path$_[2]'></script>";
	}
	if(defined $_[3]){
		$scriptpath.="<script type='text/javascript' src='$path$_[3]'></script>";
	}
	if(defined $_[4]){
		$scriptpath.="<script type='text/javascript' src='$path$_[4]'></script>";
	}
	if(defined $_[5]){
		$scriptpath.="<script type='text/javascript' src='$path$_[5]'></script>";
	}
	my $aux = "
	<!DOCTYPE html PUBLIC '-//W3C//DTD XHTML 1.0 Strict//EN' 'http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd'>
	<html xmlns='http://www.w3.org/1999/xhtml' xml:lang='it' lang='it'>
            <head>
                <meta http-equiv='Content-Type' content='text/html; charset=UTF-8' />
                <meta name='author' content='Fabio Ros, Valerio Burlin, Stefano Munari, Alberto Andeliero'/>
                <meta name='language' content='italian it'/>
                <meta name='rating' content='safe for kids' />
                <meta name='description' content='Il portale di news, articoli, recensioni ed eventi dedicato alla musica'/>
                $tags
                <meta name='robots' content='all' />
                <link rel='icon' href='$path/img/fav.ico' type='image/icon' />
                <link rel='stylesheet' type='text/css' media='handheld,screen' href='$path/css/screen.css'/>
                <link rel='stylesheet' type='text/css' media='print' href='$path/css/print.css'/>
                <link rel='stylesheet' type='text/css' media='speech' href='$path/css/aural.css'/>
                $scriptpath
                <title>$title</title>
                
            </head>
            <body>";
	return $aux;
}

sub printHeader{
	my $homil="<span id='logo' class='notAural'>";
	if($_[0]==1){
	    $homil.="<a href=\"$path/cgi-bin/home.cgi\"><img src=\"$path/img/tazza-di-caffe.jpg\" alt=\"Tazza di caffe' fumante in cui viene immersa una pausa di semiminima\" /></a>";
	}else{
	    $homil.="<img src=\"$path/img/tazza-di-caffe.jpg\" alt=\"Tazza di caffe fumante in cui viene immersa una pausa di semiminima\"/>";
	}
	$homil.="</span>";
	my $homl="<h1>";
	if($_[0]==1){
	    $homl.="<a href='$path/cgi-bin/home.cgi'><span xml:lang='en'>Music Break</span></a>";
	}else{
	    $homl.="<span xml:lang='en'>Music Break</span>";
	}
	$homl.="</h1>";
	my $aux = "
	<div id='container'>
	<div id='header'>
            <a class='help' href='#nav'>salta intestazione</a>
            <div id='title'>
		$homil
                $homl
                <h2>Il portale di notizie dedicato alla musica</h2>
            </div>
        </div>";
	return $aux;
}

sub printNav{#questo nav verrà visualizzato all'interno del sito sfogliando i post
    my $type = $_[0];
    my $iu=CFUN::getSession();
    my $aux="<div id='nav'><a class='help' href='#search'>salta menu</a>";
    $aux .= "<ul>"; 
    if ($type eq 'h'){$aux .= "<li id='current_nav'><p><span xml:lang='en'>Home</span></p></li>";}
    else{	$aux .= "<li><a href='$path/cgi-bin/home.cgi'><span xml:lang='en'>Home</span></a></li>";} 
    if ($type eq 'n'){$aux .= "<li id='current_nav'><p><span xml:lang='en'>News</span></p></li>";}
    else {	$aux .= "<li><a href='$path/cgi-bin/show.cgi?type=n'><span xml:lang='en'>News</span></a></li>";}
    if ($type eq 'i'){$aux .= "<li id='current_nav'><p>Interviste</p></li>";}
    else {$aux .= "<li><a href='$path/cgi-bin/show.cgi?type=i'>Interviste</a></li>";}
    if ($type eq 'r'){$aux .= "<li id='current_nav'><p>Recensioni</p></li>";}
    else{$aux .= "<li><a href='$path/cgi-bin/show.cgi?type=r'>Recensioni</a></li>";}
    if ($type eq 'e'){$aux .= "<li id='current_nav'><p>Eventi</p></li>";}
    else{$aux .= "<li><a href='$path/cgi-bin/show.cgi?type=e'>Eventi</a></li>";}
    if($iu ne undef){$aux .= "<li><a href='$path/cgi-bin/adminbk.cgi?type=n'>Admin</a></li>";}
    else{
	if ($type eq 'l') {$aux .="<li id='current_nav'><span xml:lang='en'>Login</span></li>";}
     else{$aux .="<li><a href='$path/cgi-bin/login.cgi'><span xml:lang='en'>Login</span></a></li>";}
    }
    $aux .= "</ul>
    <form action='$path/cgi-bin/searchtags.cgi' method='get'><fieldset id='search' ><legend class='hidelegend'>Form di ricerca</legend>
	<input type='text' name='tag' title='inserire una ricerca' id='text_field' value='Cerca per tag...' />
	<input type='submit' id='button' value='Cerca' /></fieldset>
    </form>
    </div>";
    return $aux;
}

sub printAdminNav{#questo nav verrà visualizzato nel backend dell'editore
    my $type = $_[0];
    my $aux="<div id='nav'><a class='help' href='#search'>salta menu</a><ul>";
    $aux .= "<li><a href='$path/cgi-bin/home.cgi'>Torna al sito</a></li>"; 
    if ($type eq 'n'){$aux .= "<li id='current_nav'><p><span xml:lang='en'>News</span></p></li>";}
    else{$aux .= "<li><a href='$path/cgi-bin/adminbk.cgi?type=n'><span xml:lang='en'>News</span></a></li>";}
    if ($type eq 'i'){$aux .= "<li id='current_nav'><p>Interviste</p></li>";}
    else{$aux .= "<li><a href='$path/cgi-bin/adminbk.cgi?type=i'>Interviste</a></li>";}
    if ($type eq 'r'){$aux .= "<li id='current_nav'><p>Recensioni</p></li>";}
    else{$aux .= "<li><a href='$path/cgi-bin/adminbk.cgi?type=r'>Recensioni</a></li>";} 
    if ($type eq 'e'){$aux .= "<li id='current_nav'>Eventi</li>";}
    else{$aux .= "<li><a href='$path/cgi-bin/adminbk.cgi?type=e'>Eventi</a></li>"; }
    if ($type eq 'd'){$aux .= "<li id='current_nav'><p>Cancella</p></li>";}
    else{$aux .= "<li><a href='$path/cgi-bin/deletepost.cgi'>Cancella</a></li>";}
    $aux .= "<li><a href='$path/cgi-bin/logout.cgi' ><span xml:lang='en'>Logout</span></a></li>";
    $aux .= "</ul></div>";
    return $aux;
}

sub printTags{
	my $ptrtags = $_[0]->findnodes("tag");
	my $aux = '<ul class="tags">';
	foreach my $tag ($ptrtags->get_nodelist){	
		$aux .= "<li>
			<a href='searchtags.cgi?idtag=".$tag->findnodes("\@id")->get_node(1)->textContent."'>".
			$tag->findnodes("node()")->get_node(1)->textContent."</a>
			</li>";
	}
	$aux = $aux.'</ul>';
	return $aux;
}

#ritorna una stringa del nodo XLM e tutti i suoi figli tag compresi
sub printRawNode{
	my $nodes=$_[0];
	my $aux='';
	for (my $var = 1; $var < $nodes->findnodes("node()")->size()+1; $var++) {
		$aux.=$nodes->findnodes("node()")->get_node($var)->serialize();
	}
	return $aux;
}

sub printPosts{
	my $ptrpos = $_[0]->findnodes("/posts/post");
	my $type= $_[1];
	my $aux = '';
	if($type eq 'e'){
		$aux.="<ul class='eventi'>";
		foreach my $post ($ptrpos->get_nodelist){
			my ($year,$mon,$day)=split('-',$post->findnodes("dataEvento")->get_node(1)->textContent);
			$aux.="<li class='evento'>
						<div class='Intestazione'>
							<span class='giorno'>".$day."</span>
							<span class='mese'>".$mon."</span>
							<span class='anno'>".$year."</span>
							<span class='luogo'>".$post->findnodes("luogo")->get_node(1)->textContent."</span>
						</div>
						<div class='dettagli'>
							<div class='copertina'>
								<h1><a href='posts.cgi?post=".$post->findnodes("\@id")->get_node(1)->textContent."'>".printRawNode($post->findnodes("titolo"))."</a></h1>
								<img class='thumbnail' src='".$path.$post->findnodes("foto/src/node()")->get_node(1)->textContent."' alt='".$post->findnodes("foto/alt/node()")->get_node(1)->textContent."'></img>
							</div>
							<p class='description'>".printRawNode($post->findnodes("excerpt"))."</p>
							<p class='info'>
								<span class='luogo_specifico'>".$post->findnodes("luogo")->get_node(1)->textContent."</span>
								<span class='costo_biglietto'>".$post->findnodes("prezzo")->get_node(1)->textContent."</span>
								<span class='email'>".$post->findnodes("email")->get_node(1)->textContent."</span>
								<span class='telefono'>".$post->findnodes("telefono")->get_node(1)->textContent."</span>
							</p>".
							printTags($post)."
						<div class='nav_help'><a href='#header'>torna su</a></div>
					</div>
			</li>";
		}
		$aux .= '</ul>';
	}else{
	    $aux.="<ul>";
		foreach my $post ($ptrpos->get_nodelist){
			$aux .= "
			<li class='article'>
			<h1><a href='posts.cgi?post=".$post->findnodes("\@id")->get_node(1)->textContent."' title=\"vai all\' articolo - ".($post->findnodes("titolo")->get_node(1)->textContent)."\">".printRawNode($post->findnodes("titolo"))."</a></h1> 
			<span class='author'>di ".$post->findnodes("editore/nome")->get_node(1)->textContent." ".$post->findnodes("editore/cognome")->get_node(1)->textContent." ".$post->findnodes("data")->get_node(1)->textContent."</span>". 
			"<img src='".$path.$post->findnodes("foto/src/node()")->get_node(1)->textContent."' alt='".$post->findnodes("foto/alt/node()")->get_node(1)->textContent."' /> 
			<p>".printRawNode($post->findnodes("excerpt"))."</p> 
			<a class='continua' href='$path/cgi-bin/posts.cgi?post=".$post->findnodes("\@id")->get_node(1)->textContent."' title=\"continua a leggere l\' articolo - ".$post->findnodes("titolo")->get_node(1)->textContent."\">continua →</a>". 
			printTags($post).
			"<div class='nav_help'><a href='#header'>torna su</a></div></li>";
		}
	    $aux.="</ul>";
	}
	return $aux;
}

sub printFooter{
	my $aux = "
	</div>
	<div id='footer'>
    	        <a class='help' href='#header'>salta testo a fine pagina</a>
    	        <a href='http://validator.w3.org/check?uri=referer'>
    	        	<img src='http://www.w3.org/Icons/valid-xhtml10' alt='Valid XHTML 1.0 Strict'/></a>
            	<a href='http://jigsaw.w3.org/css-validator/check/referer'><img src='http://jigsaw.w3.org/css-validator/images/vcss-blue' alt='CSS Valido!' /></a>
            	<p>&#169; 2014 <span xml:lang='en'>Music Break All Right Reserved.</span> | 
                <a href='$path/chi_siamo.html'> Chi siamo</a> | 
                <a href='$path/condizioni.html'>Condizioni d'uso</a> | 
                <a href='$path/contatti.html'> Contatti</a>  
            </p>
        </div>
    	</body>
	</html>";
	return $aux;
}


sub getuniqueid{
	my $ptrnodes = $_[0];
	my $type = $_[1];
	my $size = $ptrnodes->size();
	if($size==0){
		return $type."0";
	}
	my $lastnode = $ptrnodes->get_node($size);
	my $pid = $lastnode->findnodes("\@id")->get_node(1)->textContent;
	my $nid = substr($pid, 1, length($pid));
	$nid+=1;
	return $type.($nid);
}

sub createtag{
	my $tag = $_[0];
	my $src = $_[1];
	my $roottags = $src->findnodes("/root/tags")->get_node(1);
	my $tags = $roottags->findnodes("tag");
	my $id = $tags->size();
	my $tagnode = "<tag id='$id'>$tag</tag>";
	my $node = $xml->parse_balanced_chunk($tagnode,'UTF-8');
	$roottags->appendChild($node);
	return $id;
}

sub searchidtag{
	my $tag = $_[0];
	my $src = $_[1];
	my $DBtags = $src->findnodes("/root/tags/tag");
	foreach my $DBtag ($DBtags->get_nodelist){
		my $txttag = $DBtag->textContent;
		if($tag eq $txttag){
			return $DBtag->findnodes("\@id")->get_node(1)->textContent;
		}
	}
	return -1;
}

sub buildtagnodes{
	my $strtags = $_[0];
	my $src = $_[1];
	my $node = "";
	my @tags=split(',', $strtags);
	foreach my $tag (@tags){
		$tag=lc($tag);
		my $idtag=searchidtag($tag,$src);
		if($idtag==-1){
			$idtag = createtag($tag,$src);
		}
		$node = $node."<tag>$idtag</tag>";
	}
	return $node;
}

sub creategallery{
	my $src = $_[0];
	my @gallerynms = @{$_[1]};
	my $rtgal = $src->findnodes("/root/gallerie")->get_node(1);
	my $id = $rtgal->findnodes("galleria[position() = last()]/\@id")->get_node(1)->nodeValue();
	$id = $id+1;
	my $node = "<galleria id='$id'>";
	my $size = scalar @gallerynms;
	for (my $var=0; $var<$size; $var += 1) {
		$node =$node . "<foto><titolo>Foto galleria numero $var</titolo><srcPath>/img/interviste/gallery/photogalleria-$id-$var.jpg</srcPath></foto>";
	}
	$node.="</galleria>";
	my $aux = $xml->parse_balanced_chunk($node,'UTF-8');
	$rtgal->appendChild($aux);
	return $id;
}

sub deletepost {
    my $idPost = $_[0];
    my $src = $_[1];
    my $posttype = substr($idPost, 0, 1);
    my $vincolo=getvincpath($posttype);
    my $node = $src->findnodes("/root/posts/".$vincolo."[\@id='$idPost']")->get_node(1);
    my $photoname =  $node->findnodes("foto/src")->get_node(1)->textContent();
    unlink("../public_html"..$photoname);
    if ($posttype eq "i") {
	my $idgal = $node->findnodes("galleria")->get_node(1)->textContent();
	my $galphotosnodes = $src->findnodes("/root/gallerie/galleria[\@id=$idgal]/srcPath");
	foreach my $imggal ($galphotosnodes->get_nodelist()) {
	    unlink("../public_html".$imggal->textContent());
	}
	my $gallery = $galphotosnodes->parentNode();
	my $gallfath = $gallery->parentNode();
	$gallfath->removeChild($gallery);
    }
    my $father = $node->parentNode();
    $father->removeChild($node);
}

sub getSession{
    my $session = CGI::Session->load();
    if($session->is_expired || $session->is_empty){
	return undef;
    }else{
	my $utente=$session->param('id');
	return $utente;
    }
}

sub createSession{
	my $idUtente = $_[0];
	my $rdr = $_[1];
	my $session = new CGI::Session();
	$session->param('id', $idUtente);
	print $session->header(-location=> $path.$rdr);
	exit 0;
}

sub destroySession{
	my $session = new CGI::Session();
	my $SID = $session->id();
	$session->close();
	$session->delete();
	$session->flush();
}
