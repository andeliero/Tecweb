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
use Email::Valid;
use CFUN;

my $path=CFUN::getpath();
my $cgi = CGI->new();
my $xml = XML::LibXML->new();
my $xslt = XML::LibXSLT->new();
my $DBpath = "../data/XML/DBsite.xml";
my $source = XML::LibXML->load_xml(location => $DBpath);
my $idutente=CFUN::getSession();
if($idutente eq undef){
    CFUN::redir("/cgi-bin/login.cgi");
}

my $tm = localtime;
my ($day,$month,$year)=($tm->mday,$tm->mon+1,$tm->year+1900);



my $fail = 0;
my $msg = "&&";
my $type = $cgi->param('tipo');
my $titolo;
if($cgi->param('titolo') eq ""){
	$fail=1;
	$msg = $msg."msg1=stringavuota&&";
}else{$titolo=$cgi->param('titolo');}

#controllo della foto
my $srcfoto = $cgi->upload('src');
my $filename;
my $imgpath = CFUN::getfolderpath($type);
if($cgi->param('src') eq ""){
	$fail=1;
	$msg = $msg."msg2=nome%20del%20file%20vuoto&&";
}
else{$filename=$cgi->param('src');}

my $altfoto;
if($cgi->param('alt') eq ""){
	$fail=1;
	$msg = $msg."msg3=descrizione%20della%20foto%20vuota&&";
}else{$altfoto=$cgi->param('alt');}

my $descrizione;
if($cgi->param('excerpt') eq ""){
	$fail=1;
	$msg = $msg."msg4=descrizione%20del%20post%20vuoto&&";
}else{$descrizione=$cgi->param('excerpt');}


my $testo;
if($cgi->param('descrizione') eq ""){
	$fail=1;
	$msg=$msg."msg5=testo%20del%20post%20vuoto&&";
}else{$testo=$cgi->param('descrizione');}


my $tags;
if($cgi->param('tags') eq ""){
	$fail=1;
	$msg=$msg."msg6=nessun%20tag%20inserito&&";
}else{$tags=$cgi->param('tags');}


my $dataEvento;
my $numgiorni;
my $luogo;
my $oraInizio;
my $oraFine;
my $indirizzo;
my $price;
my $mail;
my $phone;
if($type eq 'e'){
	if((!defined $cgi->param('dataEvento')) && $cgi->param('dataEvento') eq ""){
		$fail=1;
		$msg=$msg."msg7=data%20vuota&&";
	}else{$dataEvento=$cgi->param('dataEvento');}

	if((!defined $cgi->param('numGiorni')) && $cgi->param('numGiorni') eq ""){
		$fail=1;
		$msg=$msg."msg8=numero%20giorni%20vuoto&&";
	}else{$numgiorni=$cgi->param('numGiorni');}

	if((!defined $cgi->param('luogo')) && $cgi->param('luogo') eq ""){
		$fail=1;
		$msg=$msg."msg9=nessun%20luogo%20inserito&&";
	}else{$luogo=$cgi->param('luogo');}

	if((!defined $cgi->param('oraInizio')) && $cgi->param('oraInizio') eq ""){
		$fail=1;
		$msg.="msg10=manca%20ora%20inizio&&";
	}else{
	    #<xsd:pattern value="[0-9]{2}:[0-9]{2}"/>
	    $oraInizio=$cgi->param('oraInizio');
	    if($oraInizio=~m/[0-9]{2}\:[0-9]{2}$/ && substr($oraInizio,0,2)<24 && substr($oraInizio,3,2)<60){
		#ora valida
	    }else{
		$fail=1;
		$msg.="msg10=oraInizio%20non%20valida&&";
	      }
	    }

	if((!defined $cgi->param('oraFine')) && $cgi->param('oraFine') eq ""){
		$fail=1;
		$msg.="msg11=manca%20ora%20fine&&";
	}else{
	  #<xsd:pattern value="[0-9]{2}:[0-9]{2}"/>
	  $oraFine=$cgi->param('oraFine');
	  if($oraFine=~m/[0-9]{2}\:[0-9]{2}$/ && substr($oraFine,0,2)<24 && substr($oraFine,3,2)<60){
		#ora valida
	    }else{
		$fail=1;
		$msg.="msg11=oraFine%20non%20valida&&";
	      }
	  }

	if((!defined $cgi->param('indirizzo')) && $cgi->param('indirizzo') eq ""){
		$fail=1;
		$msg=$msg."msg12=manca%20indirizzo&&";
	}else{$indirizzo=$cgi->param('indirizzo');}

	if((!defined $cgi->param('prezzo')) && $cgi->param('prezzo') eq ""){
		$fail=1;
		$msg.="msg13=manca%20il%20prezzo&&";
	}else{
	    #<xsd:pattern value="€[0-9]+\.[0-9]{2}"/>
	    $price=$cgi->param('prezzo');
	    if($price=~m/[0-9]+\.[0-9]{2}$/){
		#numero di telefono valido
		$price="€".$price;
	    }else{
		$fail=1;
		$msg=$msg."msg13=prezzo%20non%20valido&&";
	      }
	    }

	if((!defined $cgi->param('email')) && $cgi->param('email') eq ""){
		$fail=1;
		$msg.="msg14=manca%20la%20mail&&";
	}else{
	  #<xsd:pattern value="[_\-a-zA-Z0-9\.\+]+@[a-zA-Z0-9](\.?[\-a-zA-Z0-9]*[a-zA-Z0-9])*"/>
	  close ($MYFILE);
	  if (! $mail=~m/^([\w\-\+\.]+)\@([\w\-\+\.]+)\.([\w\-\+\.]+)$/) {
	    $fail=1;
	    $msg.="msg14=indirizzo%20email%20nonvalido&&";
	  }
	}

	if((!defined $cgi->param('telefono')) && $cgi->param('telefono') eq ""){
		$fail=1;
		$msg=$msg."msg15=manca%20il%20telefono&&";
	}else{
	    #<xsd:pattern value="[0-9]{1,}\s([0-9])+"/>
	    $phone=$cgi->param('telefono');
	    if($phone=~m/[0-9]{10}$/){
		#numero di telefono valido
	    }else{
		$fail=1;
		$msg=$msg."msg15=numero%20di%20telefono%20non%20valido&&";
	    }
	}
}

my $intervistato;
my @gallery;
my @gallerynames;
if ($type eq 'i'){

	if((!defined $cgi->param('intervistato')) && $cgi->param('intervistato') eq ""){
		$fail=1;
		$msg=$msg."msg7=manca%20il%20nome%20intervistato&&";
	}else{$intervistato=$cgi->param('intervistato');}

	my @gal = $cgi->upload("fgallery");
	my @galnms = $cgi->param("fgallery");
	my $galsize = scalar @gal;
	if($galsize==0){
	    $fail=1;
	    $msg=$msg."msg8=nessuna%20foto%20aggiunta";
	}else{
	    for(my $var = 0; $var< $galsize; $var++){
		    if(@gal[$var]){
			    @gallery[$var]=@gal[$var];
			    @gallerynames[$var]=@galnms[$var];
		    }
	    }
	}
}
if ($fail) {
	CFUN::redir("/cgi-bin/adminbk.cgi?type=".$type.$msg);
}else{
	
	my $vincolo = CFUN::getvincpath($type);
	my $ptrposts = $source->findnodes("/root/posts/$vincolo");
	my $father = $ptrposts->get_node(1)->parentNode;
	my $id = CFUN::getuniqueid($ptrposts,$type);
	
	my $tagnodes = CFUN::buildtagnodes($tags,$source);
	if ($type eq 'e') {
		my $fotopath = "/img/eventi/photopost$id.jpg";
		my $strpost="<evento id='$id'>
			<titolo>$titolo</titolo>
			<foto>
			<src>$fotopath</src>
			<alt>$altfoto</alt>
			</foto>
			<excerpt>$descrizione</excerpt>
			<descrizione>$testo</descrizione>
			<idautore>$idutente</idautore>
			<data>$year-$month-$day</data>
			$tagnodes
			<dataEvento>$dataEvento</dataEvento>
            <luogo>$luogo</luogo>
            <oraInizio>$oraInizio</oraInizio>
            <oraFine>$oraFine</oraFine>
            <indirizzo>$indirizzo</indirizzo>
            <prezzo>$price</prezzo>
            <email>$mail</email>
            <telefono>$phone</telefono></evento>";
		my $novopost = $xml->parse_balanced_chunk($strpost,'UTF-8');
		$father->appendChild($novopost);
	}elsif ($type eq 'r') {
		my $fotopath = "/img/recensioni/photopost$id.jpg";
		my $strpost="<recensione id='$id'>
			<titolo>$titolo</titolo>
			<foto>
			<src>$fotopath</src>
			<alt>$altfoto</alt>
			</foto>
			<excerpt>$descrizione</excerpt>
			<descrizione>$testo</descrizione>
			<idautore>$idutente</idautore>
			<data>$year-$month-$day</data>
			$tagnodes
			</recensione>";
		my $novopost = $xml->parse_balanced_chunk($strpost,'UTF-8');
		$father->appendChild($novopost);
	}elsif ($type eq 'i'){
		my $fotopath = "/img/interviste/photopost$id.jpg";
		my $idgallery = CFUN::creategallery($source,\@gallerynames);
		
		my $strpost="<intervista id='$id'>
			<titolo>$titolo</titolo>
			<foto>
			<src>$fotopath</src>
			<alt>$altfoto</alt>
			</foto>
			<excerpt>$descrizione</excerpt>
			<descrizione>$testo</descrizione>
			<idautore>$idutente</idautore>
			<data>$year-$month-$day</data>
			$tagnodes
			<intervistato>$intervistato</intervistato>
			<galleria>$idgallery</galleria>
			</intervista>";
		my $novopost = $xml->parse_balanced_chunk($strpost,'UTF-8');
		$father->appendChild($novopost);
		
		my $size = scalar @gallery;
		for (my $var = 0; $var < $size; $var++) {
		    CFUN::scrivifile(@gallery[$var],"photogalleria-$idgallery-$var.jpg","../public_html/img/interviste/gallery/");
		}
	}elsif ($type eq 'n'){
		my $fotopath = "/img/news/photopost$id.jpg";
		my $strpost="<item id='$id'>
			<titolo>$titolo</titolo>
			<foto>
			<src>$fotopath</src>
			<alt>$altfoto</alt>
			</foto>
			<excerpt>$descrizione</excerpt>
			<descrizione>$testo</descrizione>
			<idautore>$idutente</idautore>
			<data>$year-$month-$day</data>
			$tagnodes
			</item>";
		my $novopost = $xml->parse_balanced_chunk($strpost,'UTF-8');
		$father->appendChild($novopost);
	}
	CFUN::scrivifile($srcfoto, "photopost$id.jpg" ,$imgpath);
	open(OUT,">$DBpath");
	print OUT $source->toString;
	close(OUT);
	CFUN::redir("/cgi-bin/adminbk.cgi?type=".$type."&msg=post%20inserito%20con%20successo");
}
