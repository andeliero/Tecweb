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
my $type=$cgi->param("type");
my $idutente=CFUN::getSession();
if($idutente eq undef){
    CFUN::redir("/cgi-bin/login.cgi");
}


my $msg1='';
my $msg2='';
my $msg3='';
my $msg4='';
my $msg5='';
my $msg6='';
my $msg7='';
my $msg8='';
my $msg9='';
my $msg10='';
my $msg11='';
my $msg12='';
my $msg13='';
my $msg14='';
my $msg15='';

if(defined $cgi->param('msg1')){
  $msg1="<p class='error'>".$cgi->param('msg1')."</p>";
}

if(defined $cgi->param('msg2')){
  $msg2="<p class='error'>".$cgi->param('msg2')."</p>";
}

if(defined $cgi->param('msg3')){
  $msg3="<p class='error'>".$cgi->param('msg1')."</p>";
}

if(defined $cgi->param('msg4')){
  $msg4="<p class='error'>".$cgi->param('msg4')."</p>";
}

if(defined $cgi->param('msg5')){
  $msg5="<p class='error'>".$cgi->param('msg5')."</p>";
}

if(defined $cgi->param('msg6')){
  $msg6="<p class='error'>".$cgi->param('msg6')."</p>";
}

if(defined $cgi->param('msg7')){
  $msg7="<p class='error'>".$cgi->param('msg7')."</p>";
}

if(defined $cgi->param('msg8')){
  $msg8="<p class='error'>".$cgi->param('msg8')."</p>";
}

if(defined $cgi->param('msg9')){
  $msg9="<p class='error'>".$cgi->param('msg9')."</p>";
}

if(defined $cgi->param('msg10')){
  $msg10="<p class='error'>".$cgi->param('msg10')."</p>";
}

if(defined $cgi->param('msg11')){
  $msg11="<p class='error'>".$cgi->param('msg11')."</p>";
}

if(defined $cgi->param('msg12')){
  $msg12="<p class='error'>".$cgi->param('msg12')."</p>";
}

if(defined $cgi->param('msg13')){
  $msg13="<p class='error'>".$cgi->param('msg13')."</p>";
}

if(defined $cgi->param('msg14')){
  $msg14="<p class='error'>".$cgi->param('msg14')."</p>";
}

if(defined $cgi->param('msg15')){
  $msg15="<p class='error'>".$cgi->param('msg15')."</p>";
}


print $cgi->header({-type=>'text/html', -charset=>'UTF-8'});
print CFUN::printHead("Admin SEZIONE PRIVATA- Music Break","musica, news, news musicali, notizie, album","/javascript/resources/jquery-2.1.1.min.js" ,"/javascript/backend.js");
print CFUN::printHeader(1);
print CFUN::printAdminNav($type);
if ($type eq 'e') {
	print <<EOF;
    <div class="common_box">
      <h1>Gestione Eventi</h1>
    </div>
    <div class="common_box">
    <form id='insertPost' action="$path/cgi-bin/inspost.cgi" enctype="multipart/form-data" method='post'>
                <fieldset id="formfield">
                    <label for="titolo">Titolo</label>$msg1
                    <div><input type="text" name="titolo" id="titolo"/></div><p id="BoxTitoloBk"></p>
                    <label for="src">Immagine </label>$msg2
                    <input type="file" name="src" id="src"/>
                    <label for="alt">Alternativa testuale all'immagine </label>$msg3
                    <div><textarea name="alt" id="alt" cols="15" rows="4"></textarea></div><p id="BoxAltImgBk"></p>
                    <label for="excerpt">Breve didascalia (max 50 parole) </label>$msg4
                    <div><textarea name="excerpt" id="excerpt" cols="15" rows="3"></textarea></div><p id="BoxExcerptBk"></p>
                    <label for="descrizione">Descrizione Completa </label>$msg5
                    <div><textarea name="descrizione" id="descrizione" cols="15" rows="10"></textarea></div><p id="BoxDescrizioneBk"></p>
                    <label for="tags">Elenco di tag, separati da virgola</label>$msg6
                    <div><textarea name="tags" id="tags" cols="15" rows="2"></textarea></div><p id="BoxTagsBk"></p>
                    <label for="dataEvento">Data Evento </label>$msg7
                    <div><input type="text" id="dataEvento" name="dataEvento"/></div>
                    <label for="numGiorni">Numero di giorni </label>$msg8
                    <div><input type="text" id="numGiorni" name="numGiorni"/></div>
                    <label for="luogo">Luogo </label>$msg9
                    <div><input type="text" id="luogo" name="luogo"/></div><p id="BoxluogoBk"></p>
                    <label for="oraInizio">Ora di inizio</label>$msg10
                    <div><input type="text" id="oraInizio" name="oraInizio"/></div>
                     <label for="oraFine">Ora di fine</label>$msg11
                    <div><input type="text" id="oraFine" name="oraFine"/></div>
                    <label for="indirizzo">Indirizzo </label>$msg12
                    <div><input type="text" id="indirizzo" name="indirizzo"/></div><p id="BoxIndirizzoBk"></p>
                    <label for="prezzo">Prezzo </label>$msg13
                    <div><input type="text" id="prezzo" name="prezzo"/></div>
                    <label for="email"> Email </label>$msg14
                    <div><input type="text" id="email" name="email"/></div>
                    <label for="telefono">Numero di telefono </label>$msg15
                    <div><input type="text" id="telefono" name="telefono"/></div>
                    <input type="hidden" name="tipo" id="tipo" value="e" />
                    <input id='inserisci' type="submit" value="Inserisci Evento"/>
                </fieldset>
         </form>
   </div>
EOF
} elsif ($type eq 'i') {
	print <<EOF;
    <div class="common_box">
       <h1>Gestione Interviste</h1>
    </div>

    <div class="common_box">
            <form id='insertPost' action="$path/cgi-bin/inspost.cgi" enctype="multipart/form-data" method='post'>
                <fieldset id="formfield">
                    <label for="titolo">Titolo </label>$msg1
                    <div><input type="text" name="titolo" id="titolo" /></div><p id="BoxTitoloBk"></p>
                    <label for="src">Immagine </label>$msg2
                    <input type="file" name="src" id="src"/>
                    <label for="alt">Alternativa testuale all'immagine </label>$msg3
                    <div><textarea name="alt" id="alt" cols="15" rows="4"></textarea></div><p id="BoxAltImgBk"></p>
                    <label for="excerpt">Breve didascalia (max 50 parole) </label>$msg4
                    <div><textarea name="excerpt" id="excerpt" cols="15" rows="3"></textarea></div><p id="BoxExcerptBk"></p>
                    <label for="descrizione">Descrizione Completa </label>$msg5
                    <div><textarea name="descrizione" id="descrizione" cols="15" rows="10"></textarea></div><p id="BoxDescrizioneBk"></p>
                    <label for="tags">Elenco di tag, separati da virgola</label>$msg6
                    <div><textarea name="tags" id="tags" cols="15" rows="2"></textarea></div><p id="BoxTagsBk"></p>
                    <label for="intervistato">Intervistato </label>$msg7
                    <div><input type="text" name="intervistato" id="intervistato"/></div>
                    <p>Foto Per Gallery </p>$msg8
                    <input type="file" name="fgallery" id="fgallery1"/>
                    <input type="file" name="fgallery" id="fgallery2"/>
                    <input type="file" name="fgallery" id="fgallery3"/>
                    <input type="file" name="fgallery" id="fgallery4"/>
                    <input type="file" name="fgallery" id="fgallery5"/>
                    <input type="file" name="fgallery" id="fgallery6"/>
                    <input type="file" name="fgallery" id="fgallery7"/>
                    <input type="file" name="fgallery" id="fgallery8"/>
                    <input type="file" name="fgallery" id="fgallery9"/>
                    <input type="file" name="fgallery" id="fgallery10"/>
                    <input type="hidden" name="tipo" id="tipo" value="i" />
                    <input id='inserisci' type="submit" value="Inserisci Intervista" />
                </fieldset>
            </form>
    </div>
EOF
} elsif ($type eq 'n') {
#cols="15" rows="4"
	print <<EOF;
      <div class="common_box">
        <h1>Gestione News</h1>
      </div>
      <div class="common_box">
            <form id='insertPost' action="$path/cgi-bin/inspost.cgi" enctype="multipart/form-data" method='post'>
                <fieldset id="formfield">
                    <label for="Titolo">Titolo </label>$msg1
                    <div><input type="text" name="titolo" id="titolo"/></div><p id="BoxTitoloBk"></p>
                    <label for="src">Immagine</label>$msg2
                    <input type="file" name="src" id="src"/>
                    <label for="alt">Alternativa testuale all'immagine </label>$msg3
                    <div><textarea name="alt" id="alt" cols="15" rows="4"></textarea></div><p id="BoxAltImgBk"></p>
                    <label for="excerpt">Breve didascalia (max 50 parole) </label>$msg4
                    <div><textarea name="excerpt" id="excerpt" cols="15" rows="3" ></textarea></div><p id="BoxExcerptBk"></p>
                    <label for="descrizione">Descrizione Completa </label>$msg5
                    <div><textarea name="descrizione" id="descrizione" cols="15" rows="10"></textarea></div><p id="BoxDescrizioneBk"></p>
                    <label for="tags">Elenco di tag, separati da virgola</label>$msg6
                    <div><textarea name="tags" id="tags" cols="15" rows="2"></textarea></div><p id="BoxTagsBk"></p>
                    <input type="hidden" name="tipo" id="tipo" value="n" />
                    <input id='inserisci' type="submit" value="Inserisci News"/>
                </fieldset>
            </form>
      </div>
EOF
} elsif ($type eq 'r') {
	print <<EOF;
    <div class="common_box">
      <h1>Gestione Recensioni</h1>
    </div>

    <div class="common_box">
           <form id='insertPost' action="$path/cgi-bin/inspost.cgi" enctype="multipart/form-data" method='post'>
                <fieldset id="formfield">
                    <label for="titolo">Titolo </label>$msg1
                    <div><input type="text" name="titolo" id="titolo"/></div><p id="BoxTitoloBk"></p>
                    <label for="src">Immagine </label>$msg2
                    <input type="file" name="src" id="src"/>
                    <label for="alt">Alternativa testuale all'immagine </label>$msg3
                    <div><textarea name="alt" id="alt" cols="15" rows="4"></textarea></div><p id="BoxAltImgBk"></p>
                    <label for="excerpt">Breve didascalia (max 50 parole) </label>$msg4
                    <div><textarea name="excerpt" id="excerpt" cols="15" rows="3"></textarea></div><p id="BoxExcerptBk"></p>
                    <label for="descrizione">Descrizione Completa </label>$msg5
                    <div><textarea name="descrizione" id="descrizione" cols="15" rows="10"></textarea></div><p id="BoxDescrizioneBk"></p>
                    <label for="tags">Elenco di tag, separati da virgola</label>$msg6
                    <div><textarea name="tags" id="tags" cols="15" rows="2"></textarea></div><p id="BoxTagsBk"></p>
                    <input type="hidden" name="tipo" id="tipo" value="r" />
                    <input id='inserisci' type="submit" value="Inserisci Recensione" />
                </fieldset>
            </form>
    </div>
EOF
}
print CFUN::printFooter;
