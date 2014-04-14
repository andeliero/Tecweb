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

my $path = CFUN::getpath();
my $cgi = CGI->new();
my $type=$cgi->param("type");
my $idutente=2;#CFUN::getSession;

#my $session = CGI::Session->new();
#my $sid = $session->id();
#$session->flush;
#my $session = CGI::Session->new(undef,$sid, {Directory=>"../data/tmp"});
#my $usernumb = $session->param("userid");

print $cgi->header({-type=>'text/html', -charset=>'UTF-8'});
print CFUN::printHead("Admin SEZIONE PRIVATA- Music Break","musica, news, news musicali, notizie, album");#,"/javascript/backend.js");
print CFUN::printHeader();
print CFUN::printAdminNav($type);
if ($type eq 'e') {
	print <<EOF;
    <div class="common_box">
      <h1>Gestione Eventi</h1>
    </div>
    <div class="common_box">
    <form action="$path/cgi-bin/inspost.cgi" enctype="multipart/form-data" method='post' onsubmit="return checkSubmit();">
                <fieldset id="formfield">
                    <label for="titoloEvento">Titolo</label>
                    <div><input type="text" name="titolo" id="titolo" value="Inserire un titolo..." onclick="Wbar('titolo');" onblur="Bbar('titolo');" /></div>
                    <label for="src">Immagine </label>
                    <input type="file" name="src" id="src"/>
                    <label for="alt">Alternativa testuale all'immagine </label>
                    <div><textarea name="alt" id="alt" rows="4" value="Inserire una descrizione testuale dell'immagine..." onclick="Wbar('alt');" onblur="Bbar('alt');">Inserire una descrizione testuale dell'immagine...</textarea></div>
                    <label for="excerpt">Breve didascalia (max 50 parole) </label>
                    <div><textarea name="excerpt" id="excerpt" rows="3" value="Inserire una breve didascalia testuale..." onclick="Wbar('excerpt');" onblur="Bbar('excerpt');" >Inserire una breve didascalia testuale...</textarea></div>
                    <label for="descrizione">Descrizione Completa </label>
                    <div><textarea name="descrizione" id="descrizione" rows="10" value="Inserire il testo completo dell'articolo..." onclick="Wbar('descrizione');" onblur="Bbar('descrizione');">Inserire il testo completo dell'articolo...</textarea></div>
                    <label for="tags">Elenco di tag, separati da virgola</label>
                    <div><textarea name="tags" id="tags" rows="2" value="Inserire dei tags separandoli con una virgola..." onclick="Wbar('tags');" onblur="Bbar('tags');">Inserire dei tags separandoli con una virgola...</textarea></div>
                    <label for="dataEvento">Data Evento </label>
                    <div><input type="text" id="dataEvento" name="dataEvento" value="mm/gg/aaaa" onclick="Wbar('dataEvento');" onblur="Bbar('dataEvento');" /></div>
                    <label for="numGiorni">Numero di giorni </label>
                    <div><input type="text" id="numGiorni" name="numGiorni" value="Inserire la durata dell'evento in giorni..." onclick="Wbar('numGiorni');" onblur="Bbar('numGiorni');"/></div>
                    <label for="luogo">Luogo </label>
                    <div><input type="text" id="luogo" name="luogo" value="Inserire il luogo dell'evento..." onclick="Wbar('luogo');" onblur="Bbar('luogo');"/></div>
                    <label for="oraInizio">Ora di inizio</label>
                    <div><input type="text" id="oraInizio" name="oraInizio" value="Inserire un orario..." onclick="Wbar('oraInizio');" onblur="Bbar('oraInizio');"/></div>
                     <label for="oraFine">Ora di fine</label>
                    <div><input type="text" id="oraFine" name="oraFine" value="Inserire un orario..." onclick="Wbar('oraFine');" onblur="Bbar('oraFine');"/></div>
                    <label for="indirizzo">Indirizzo </label>
                    <div><input type="text" id="indirizzo" name="indirizzo" value="Inserire il nome della via..." onclick="Wbar('indirizzo');" onblur="Bbar('indirizzo');"/></div>
                    <label for="prezzo">Prezzo </label>
                    <div><input type="text" id="prezzo" name="prezzo" value="Inserire un prezzo..." onclick="Wbar('prezzo');" onblur="Bbar('prezzo');"/></div>
                    <label for="email"> Email </label>
                    <div><input type="text" id="email" name="email" value="Inserire il proprio indirizzo e-mail..." onclick="Wbar('email');" onblur="Bbar('email');"/></div>
                    <label for="telefono">Numero di telefono </label>
                    <div><input type="text" id="telefono" name="telefono" value="Inserire il numero di telefono..." onclick="Wbar('telefono');" onblur="Bbar('telefono');"/></div>
                    <input type="hidden" name="tipo" id="tipo" value="e" />
                    <input type="submit" value="Inserisci Intervista" />
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
            <form action="$path/cgi-bin/inspost.cgi" enctype="multipart/form-data" method='post' onsubmit="return checkSubmit();">
                <fieldset id="formfield">
                    <label for="titoloIntervista">Titolo </label>
                    <div><input type="text" name="titolo" id="titolo" value="Inserire un titolo..." onclick="Wbar('titolo');" onblur="Bbar('titolo');" /></div>
                    <label for="src">Immagine </label>
                    <input type="file" name="src" id="src"/>
                    <label for="alt">Alternativa testuale all'immagine </label>
                    <div><textarea name="alt" id="alt" rows="4" value="Inserire una descrizione testuale dell'immagine..." onclick="Wbar('alt');" onblur="Bbar('alt');">Inserire una descrizione testuale dell'immagine...</textarea></div>
                    <label for="excerpt">Breve didascalia (max 50 parole) </label>
                    <div><textarea name="excerpt" id="excerpt" rows="3" value="Inserire una breve didascalia testuale..." onclick="Wbar('excerpt');" onblur="Bbar('excerpt');" >Inserire una breve didascalia testuale...</textarea></div>
                    <label for="descrizione">Descrizione Completa </label>
                    <div><textarea name="descrizione" id="descrizione" rows="10" value="Inserire il testo completo dell'articolo..." onclick="Wbar('descrizione');" onblur="Bbar('descrizione');">Inserire il testo completo dell'articolo...</textarea></div>
                    <label for="tags">Elenco di tag, separati da virgola</label>
                    <div><textarea name="tags" id="tags" rows="2" value="Inserire dei tags separandoli con una virgola..." onclick="Wbar('tags');" onblur="Bbar('tags');">Inserire dei tags separandoli con una virgola...</textarea></div>
                    <label for="intervistato">Intervistato </label>
                    <div><input type="text" name="intervistato" id="intervistato" value="Inserire il nome dell'artista..." onclick="Wbar('intervistato');" onblur="Bbar('intervistato');"/></div>
                    <p>Foto Per Gallery </p>
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
                    <input type="submit" value="Inserisci Intervista" />
                </fieldset>
            </form>
    </div>
EOF
} elsif ($type eq 'n') {
	print <<EOF;
      <div class="common_box">
        <h1>Gestione News</h1>
      </div>
      <div class="common_box">
            <form action="$path/cgi-bin/inspost.cgi" enctype="multipart/form-data" method='post' onsubmit="return checkSubmit();">
                <fieldset id="formfield">
                    <label for="titoloNews">Titolo </label>
                    <div><input type="text" name="titolo" id="titolo" value="Inserire un titolo..." onclick="Wbar('titolo');" onblur="Bbar('titolo');"/></div>
                    <label for="src">Immagine</label>
                    <input type="file" name="src" id="src"/>
                    <label for="alt">Alternativa testuale all'immagine </label>
                    <div><textarea name="alt" id="alt" rows="4" value="Inserire una descrizione testuale dell'immagine..." onclick="Wbar('alt');" onblur="Bbar('alt');">Inserire una descrizione testuale dell'immagine...</textarea></div>
                    <label for="excerpt">Breve didascalia (max 50 parole) </label>
                    <div><textarea name="excerpt" id="excerpt" rows="3" value="Inserire una breve didascalia testuale..." onclick="Wbar('excerpt');" onblur="Bbar('excerpt');" >Inserire una breve didascalia testuale...</textarea></div>
                    <label for="descrizione">Descrizione Completa </label>
                    <div><textarea name="descrizione" id="descrizione" rows="10" value="Inserire il testo completo dell'articolo..." onclick="Wbar('descrizione');" onblur="Bbar('descrizione');">Inserire il testo completo dell'articolo...</textarea></div>
                    <label for="tags">Elenco di tag, separati da virgola</label>
                    <div><textarea name="tags" id="tags" rows="2" value="Inserire dei tags separandoli con una virgola..." onclick="Wbar('tags');" onblur="Bbar('tags');">Inserire dei tags separandoli con una virgola...</textarea></div>
                    <input type="hidden" name="tipo" id="tipo" value="n" />
                    <input type="submit" value="Inserisci News"/>
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
           <form action="$path/cgi-bin/inspost.cgi" enctype="multipart/form-data" method='post' onsubmit="return checkSubmit();">
                <fieldset id="formfield">
                    <label for="titoloRecensione">Titolo </label>
                    <div><input type="text" name="titolo" id="titolo" value="Inserire un titolo..." onclick="Wbar('titolo');" onblur="Bbar('titolo');" /></div>
                    <label for="src">Immagine </label>
                    <input type="file" name="src" id="src"/>
                    <label for="alt">Alternativa testuale all'immagine </label>
                    <div><textarea name="alt" id="alt" rows="4" value="Inserire una descrizione testuale dell'immagine..." onclick="Wbar('alt');" onblur="Bbar('alt');">Inserire una descrizione testuale dell'immagine...</textarea></div>
                    <label for="excerpt">Breve didascalia (max 50 parole) </label>
                    <div><textarea name="excerpt" id="excerpt" rows="3" value="Inserire una breve didascalia testuale..." onclick="Wbar('excerpt');" onblur="Bbar('excerpt');" >Inserire una breve didascalia testuale...</textarea></div>
                    <label for="descrizione">Descrizione Completa </label>
                    <div><textarea name="descrizione" id="descrizione" rows="10" value="Inserire il testo completo dell'articolo..." onclick="Wbar('descrizione');" onblur="Bbar('descrizione');">Inserire il testo completo dell'articolo...</textarea></div>
                    <label for="tags">Elenco di tag, separati da virgola</label>
                    <div><textarea name="tags" id="tags" rows="2" value="Inserire dei tags separandoli con una virgola..." onclick="Wbar('tags');" onblur="Bbar('tags');">Inserire dei tags separandoli con una virgola...</textarea></div>
                    <input type="hidden" name="tipo" id="tipo" value="r" />
                    <input type="submit" value="Inserisci Recensione" />
                </fieldset>
            </form>
    </div>
EOF
}
print CFUN::printFooter;
