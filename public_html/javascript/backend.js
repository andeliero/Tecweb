// BACKEND
//-----FORM-----

var def=new Array(),check=new Array();//def conterrà il valore di default dato come aiuto,check contiene gli id degli elementi della form
//FUNZIONI ONLOAD

function setArray(){//def è un array associativo del tipo def[id]="valore di default del placeholder"
var a=document.getElementById("formfield");
a=removeBlankspace(a);
var b=a.lastChild.value;//prendo il valore del pulsante di submit per identificare la pagina
a=a.getElementsByTagName("div");
for(var i=0;i<a.length;++i)
{
	check[i]=a[i].firstChild.id;//mi serve nella funzione checkSubmit
}
var c=b.replace(/\s/g,'');
var str="set"+c;
window[str]();//chiamo la funzione che setta i valori di default per gli aiuti
if(b == "Accedi")//se e' la pagina di login allora inserisco il valore del coockie
	readCookie();
}

function setAccedi(){
def['username']=("inserire un nome utente...");
def['password']=("inserire una password...");
}

function setInserisciNews(){//funzione che setta i valori standard di alcuni campi comuni a molte pagine
def['titolo']=("Inserire un titolo...");
def['alt']=("Inserire una descrizione testuale dell'immagine...");
def['excerpt']=("Inserire una breve didascalia testuale...");
def['descrizione']=("Inserire il testo completo dell'articolo...");
def['tags']=("Inserire dei tags separandoli con una virgola...");
}

function setInserisciIntervista(){
setInserisciNews();
def['intervistato']=("Inserire il nome dell'artista...");
}

function setInserisciRecensione(){
setInserisciNews();
}

function setInserisciEvento(){
setInserisciNews();
def['intervistato']=("Inserire il nome dell'artista...");
def['dataEvento']=("gg/mm/aaaa");
def['numGiorni']=("inserire la durata dell'evento in giorni..");
def['luogo']=("Inserire il luogo dell'evento...");
def['oraInizio']=("Inserire un orario nel formato oo:mm");
def['oraFine']=("Inserire un orario oo:mm");
def['indirizzo']=("Inserire il nome della via...");
def['prezzo']=("Inserire un prezzo...");
def['email']=("Inserire il proprio indirizzo e-mail...");
def['telefono']=("Inserire il numero di telefono...");
}


//funzione di utilità per setArray()
function removeBlankspace(n)
{
  for (var i=0; i< n.childNodes.length; i++)
  {
    var child = n.childNodes[i];
    if(child.nodeType == 3 && !/\S/.test(child.nodeValue))//nodeType==3 significa se è un nodo che ha un contenuto di tipo testuale,controllo che non contenga spazi
    {
      n.removeChild(child);//riduco in questo modo childNodes.length
      i--;
    }
    if(child.nodeType == 1)//nodeType==1 controlla se e' un nodo di tipo element
    {
      removeBlankspace(child);
    }
  }
  return n;
}

//FUNZIONI ONCLICK

function Wbar(x){
if(document.getElementById(x).parentNode.lastChild.className == "jsErr")
	Bbar(x);
if(checkSonNum(document.getElementById(x).parentNode))
	insertHelp(x);
/*if(document.getElementById(x).value == def[x])
	document.getElementById(x).value= "";*/
}

function checkSonNum(u){//se non e' stato inserito nessun aiuto ritorna true,altrimenti ritorna false
	if(u.childNodes.length<=1)
		return true;
	else
		return false;
}

function insertHelp(x){
	var node=document.createElement("span");
	node.className="jsHelp";
	node.appendChild(document.createTextNode(def[x]));
	document.getElementById(x).parentNode.appendChild(node);
}

//FUNZIONI ONBLUR

function Bbar(x){
//controllo che siano diversi perchè altrimenti selezionando tutto il valore di default di un input(senza fare onclick) e poi facendo onblur l'utente può distruggere i campi di input
	if(document.getElementById(x).parentNode.lastChild != document.getElementById(x).parentNode.firstChild) 
		document.getElementById(x).parentNode.removeChild(document.getElementById(x).parentNode.lastChild);
}








//FUNZIONI ONSUBMIT

function createErr(txt){
	var node=document.createElement("span");
	node.className="jsErr";
	node.appendChild(txt);
	return node;
}


//funzione che richiama i controlli sui singoli campi della form (vedi ciclo for interno)
function checkSubmit(){
	var state=true;
	for(var i=0;i< check.length;++i)
		{
			var y="C"+check[i];
			var txt=window[y]();//trasformo la stringa in una chiamata a funzione e il valore ritornato lo salvo in txt
			var parent=document.getElementById(check[i]).parentNode;
			if(checkSonNum(parent)&&txt){//se non ci sono aiuti e l'input inserito e' errato
				parent.appendChild(createErr(txt));
			}
			if(txt)	//devo usare un if aggiuntivo e non posso inserirlo nel precedente perchè l'utente potrebbe 	
					//inserire più volte un form non valido senza cliccare realmente su nessun elemento
				state=false;
		}
	if(!state)//se ci sono errori avviso l'utente
	{
		var d=document.getElementById("formfield").lastChild;
		if(!(d.tagName.toLowerCase() == 'span'))//se non l'ho gia' avvisato precedentemente
		{	var n=document.createElement("span");
			n.className="jsErr";
			n.id="submitErr";
			n.innerHTML= "Attenzione!ci sono degli errori di compilazione!";
			d.parentNode.insertBefore(n,d.nextSibling);
		}
	}
	return state;
}







function Ctitolo(){
	var t="titolo";
	var string=document.getElementById(t).value;
	if(string.length<2 || string.length>75)
		return document.createTextNode("inserire un minimo di 2 e un massimo di 75 caratteri");
	else
		return false;
}

function Calt(){
	var t="alt";
	var string=document.getElementById(t).value;
	var n=countWords(string,' ');
	if(n<2 || n>50)
		return document.createTextNode("inserire un minimo di 2 e un massimo di 50 parole");
	else
		return false;
}

function countWords(u,Vtrim){
var num = 0;
if(Vtrim == ' ')
	u=u.replace(/\s/g,Vtrim);//se il divisore è uno spazio allora è un testo generico
else
	u=u.replace(/\s/g,'');//altrimenti è un testo particolare che utilizza un suo divisore specifico per le parole
u=u.split(Vtrim);
for(var j=0;j<u.length;++j) {
	if (u[j].length > 0) 
		++num;
}
return num;
}

function Cexcerpt(){
	var t="excerpt";
	var string=document.getElementById(t).value;
	var n=countWords(string,' ');
	if(n<5 || n>50)
		return document.createTextNode("inserire un minimo di 5 e un massimo di 50 parole");
	else
		return false;
}

function Cdescrizione(){
	var t="descrizione";
	var string=document.getElementById(t).value;
	var n=countWords(string,' ');
	if(n<50 || n>500)
		return document.createTextNode("inserire un minimo di 50 e un massimo di 500 parole");
	else
		return false;
}

function Ctags(){
	var t="tags";
	var string=document.getElementById(t).value;
	var n=countWords(string,',');
	if(n<1 || n>20)
		return document.createTextNode("inserire un minimo di 1 e un massimo di 20 tag,se più di uno allora separarli usando la virgola.");
	else
		return false;
}

//SUBMIT DI INTERVISTE

function Cintervistato(){
	var t="intervistato";
	var string=document.getElementById(t).value;
	var n=countWords(string,' ');
	if(n<1 || n>5)
		return document.createTextNode("inserire un minimo di 1 e un massimo di 5 parole");
	else
		return false;
}

//SUBMIT DI EVENTI


function CdataEvento(){
	var t="dataEvento";
	var string=document.getElementById(t).value;
	if(/^(0[1-9]|1[0-2])\/(0[1-9]|1\d|2\d|3[01])\/(20|21)\d{2}$/.test(string))
		return false;
	else
		return document.createTextNode("inserire una data valida(compresa tra gli anni 2000 e 2199) nel formato mm/gg/aaaa");
} 

function CnumGiorni(){
	var t="numGiorni";
	var num=document.getElementById(t).value;
	if(/^([0-9]|[1-9][0-9]|[1-9][0-9][0-9])$/.test(num))
		return false;
	else
		return document.createTextNode("inserire un numero positivo <= 999");
}

function Cluogo(){
	var t="luogo";
	var string=document.getElementById(t).value;
	if(string.length<1 || string.length>58)
		return document.createTextNode("inserire un nome di città con al massimo 58 caratteri");
	else
		return false;
}

function CoraInizio(t){
	if(typeof t === "undefined")
		t="oraInizio";
	var h=document.getElementById(t).value;
	if(/^([2][0-3]|[0-1][0-9]):[0-5][0-9]$/.test(h))
		return false;
	else
		return document.createTextNode("inserire un ora compresa tra 00:00 e 23:59");
}

function CoraFine(){
	return CoraInizio("oraFine");
}

function Cindirizzo(){
	var t="indirizzo";
	var string=document.getElementById(t).value;
	num=countWords(string,' ');
	if(num<2 || num>15)
		return document.createTextNode("inserire un minimo di 2 e un massimo di 15 parole");
	else
		return false;	
}

function Cprezzo(){
	var t="prezzo";
	var p=document.getElementById(t).value;
	if(/^([1-9]{0,2}[0-9])\.[0-9][0-9]$/.test(p))
		return false;
	else
		return document.createTextNode("inserire un prezzo nel formato $$$.$$ oppure $$.$$ oppure $.$$");
}

function Cemail(){
	var t="email";
	var string=document.getElementById(t).value;
	if(/^([\w\-\+\.]+)@([\w\-\+\.]+).([\w\-\+\.]+)$/.test(string))
		return false;
	else
		return document.createTextNode("inserire una mail valida");
}

function Ctelefono(){
	var t="telefono";
	var n=document.getElementById(t).value;
	if(/^[0-9]{10,10}$/.test(n))
		return false;
	else
		return document.createTextNode("inserire un numero telefonico composto da 10 cifre");
}

//-----LOGIN-----

function readCookie(){
	for(var i=0; i<check.length; ++i)
	{	var string=getCookie(check[i]);
		if(string)
			document.getElementById(check[i]).value=string;
		}
}

function setCookie(cname,cvalue,exdays)
{
var d = new Date();
d.setTime(d.getTime()+(exdays*24*60*60*1000));
var expires = "expires="+d.toGMTString();
document.cookie=cname+"="+cvalue+"; "+expires+"; path=/";
}

function getCookie(cname)
{
var name = cname + "=";
var ca = document.cookie.split(';');
for(var i=0; i<ca.length; i++) 
  {
  c=ca[i].trim();
  if (c.indexOf(name) == 0) 
  	return c.substring(name.length,c.length);
  }
return "";
}

function checkLogin(){
	var bool=checkSubmit();
	if(bool)//se i dati inseriti sono in un formato valido
	{
		var r= confirm("Vuoi salvare un cookie? \n Questo ti permetterà di ricordare le tue credenziali in futuro. \nQueste informazioni resteranno nel tuo computer.");	
		for(var i=0; i<check.length; ++i)
		{
			if(r)
				setCookie(check[i],document.getElementById(check[i]).value,365);
			else
				setCookie(check[i],'');
		}
	}
	return bool;
}
//funzioni invocate da checksubmit()
function Cusername(){
	var t="username";
	var string=document.getElementById(t).value;
	if(string.length<1 || string.length>20)
		return document.createTextNode("inserire uno username valido di al massimo 20 caratteri");
	else
		return false;
}

function Cpassword(p){//se chiamata senza parametri-->p="undefined"
	p= (typeof(p) === "undefined") ? "password" : p ;
	var string=document.getElementById(p).value;
	if(string.length<7 || string.length>32 /*|| string==def[p]*/)
		return document.createTextNode("inserire una password di 7-32 caratteri");
	else
		return false;
}


//---jQuery
$(document).ready(function() {

 	$("#BoxTitoloBk").append("<input type='button' value='Parola inglese' class='tradLink' id='linkEnTitle'></input>");
	$("#linkEnTitle").click(function(){$('#titolo').val($('#titolo').val()+"<span lang='en'></span>");});
	$("#BoxTitoloBk").append("<input type='button' value='Parola tedesca' class='tradLink' id='linkDeTitle'></input>");
	$("#linkDeTitle").click(function(){$('#titolo').val($('#titolo').val()+"<span lang='de'></span>");});
	$("#BoxTitoloBk").append("<input type='button' value='Parola francese' class='tradLink' id='linkFrTitle'></input>");
	$("#linkFrTitle").click(function(){$('#titolo').val($('#titolo').val()+"<span lang='fr'></span>");});

//----------------------------

	$("#BoxExcerptBk").append("<input type='button' value='Parola inglese' class='tradLink' id='linkEnexcerpt'></input>");
	$("#linkEnexcerpt").click(function(){$('#excerpt').val($('#excerpt').val()+"<span lang='en'></span>");});
	$("#BoxExcerptBk").append("<input type='button' value='Parola tedesca' class='tradLink' id='linkDeexcerpt'></input>");
	$("#linkDeexcerpt").click(function(){$('#excerpt').val($('#excerpt').val()+"<span lang='de'></span>");});
	$("#BoxExcerptBk").append("<input type='button' value='Parola francese' class='tradLink' id='linkFrexcerpt'></input>");
	$("#linkFrexcerpt").click(function(){$('#excerpt').val($('#excerpt').val()+"<span lang='fr'></span>");});



//----------------------------

	$("#BoxDescrizioneBk").append("<input type='button' value='Parola inglese' class='tradLink' id='linkEndescrizione'></input>");
	$("#linkEndescrizione").click(function(){$('#descrizione').val($('#descrizione').val()+"<span lang='en'></span>");});
	$("#BoxDescrizioneBk").append("<input type='button' value='Parola tedesca' class='tradLink' id='linkDedescrizione'></input>");
	$("#linkDedescrizione").click(function(){$('#descrizione').val($('#descrizione').val()+"<span lang='de'></span>");});
	$("#BoxDescrizioneBk").append("<input type='button' value='Parola francese' class='tradLink' id='linkFrdescrizione'></input>");
	$("#linkFrdescrizione").click(function(){$('#descrizione').val($('#descrizione').val()+"<span lang='fr'></span>");});



//----------------------------

	$("#BoxTagsBk").append("<input type='button' value='Parola inglese' class='tradLink' id='linkEntags'></input>");
	$("#linkEntags").click(function(){$('#tags').val($('#tags').val()+"<span lang='en'></span>");});
	$("#BoxTagsBk").append("<input type='button' value='Parola tedesca' class='tradLink' id='linkDetags'></input>");
	$("#linkDetags").click(function(){$('#tags').val($('#tags').val()+"<span lang='de'></span>");});
	$("#BoxTagsBk").append("<input type='button' value='Parola francese' class='tradLink' id='linkFrtags'></input>");
	$("#linkFrtags").click(function(){$('#tags').val($('#tags').val()+"<span lang='fr'></span>");});



//----------------------------

	$("#BoxluogoBk").append("<input type='button' value='Parola inglese' class='tradLink' id='linkEnluogo'></input>");
	$("#linkEnluogo").click(function(){$('#luogo').val($('#luogo').val()+"<span lang='en'></span>");});
	$("#BoxluogoBk").append("<input type='button' value='Parola tedesca' class='tradLink' id='linkDeluogo'></input>");
	$("#linkDeluogo").click(function(){$('#luogo').val($('#luogo').val()+"<span lang='de'></span>");});
	$("#BoxluogoBk").append("<input type='button' value='Parola francese' class='tradLink' id='linkFrluogo'></input>");
	$("#linkFrluogo").click(function(){$('#luogo').val($('#luogo').val()+"<span lang='fr'></span>");});



//----------------------------

	$("#BoxIndirizzoBk").append("<input type='button' value='Parola inglese' class='tradLink' id='linkEnindirizzo'></input>");
	$("#linkEnindirizzo").click(function(){$('#indirizzo').val($('#indirizzo').val()+"<span lang='en'></span>");});
	$("#BoxIndirizzoBk").append("<input type='button' value='Parola tedesca' class='tradLink' id='linkDeindirizzo'></input>");
	$("#linkDeindirizzo").click(function(){$('#indirizzo').val($('#indirizzo').val()+"<span lang='de'></span>");});
	$("#BoxIndirizzoBk").append("<input type='button' value='Parola francese' class='tradLink' id='linkFrindirizzo'></input>");
	$("#linkFrindirizzo").click(function(){$('#indirizzo').val($('#indirizzo').val()+"<span lang='fr'></span>");});


//inserisco div push jquery per lo sticky-footer
$( "#container" ).append( $( "<div id='push'></div>"));

$('body').attr('onload', 'setArray()');

//GESTIONE CHIAMATE CONTROLLO FORMS
//titolo
$('#titolo').click(function(){Wbar('titolo');});
$('#titolo').blur(function(){Bbar('titolo');});
//Alternativa Testuale
$('#alt').click(function(){Wbar('alt');});
$('#alt').blur(function(){Bbar('alt');});
//Didascalia
$('#excerpt').click(function(){Wbar('excerpt');});
$('#excerpt').blur(function(){Bbar('excerpt');});
//Descrizione
$('#descrizione').click(function(){Wbar('descrizione');});
$('#descrizione').blur(function(){Bbar('descrizione');});
//Tags
$('#tags').click(function(){Wbar('tags');});
$('#tags').blur(function(){Bbar('tags');});
//Intervistato
$('#intervistato').click(function(){Wbar('intervistato');});
$('#intervistato').blur(function(){Bbar('intervistato');});
//Intervistato
$('#intervistato').click(function(){Wbar('intervistato');});
$('#intervistato').blur(function(){Bbar('intervistato');});
//DataEvento
$('#dataEvento').click(function(){Wbar('dataEvento');});
$('#dataEvento').blur(function(){Bbar('dataEvento');});
//Numero giorni
$('#numGiorni').click(function(){Wbar('numGiorni');});
$('#numGiorni').blur(function(){Bbar('numGiorni');});
//Luogo
$('#luogo').click(function(){Wbar('luogo');});
$('#luogo').blur(function(){Bbar('luogo');});
//Ora Inizio
$('#oraInizio').click(function(){Wbar('oraInizio');});
$('#oraInizio').blur(function(){Bbar('oraInizio');});
//Ora Fine
$('#oraFine').click(function(){Wbar('oraFine');});
$('#oraFine').blur(function(){Bbar('oraFine');});
//Indirizzo
$('#indirizzo').click(function(){Wbar('indirizzo');});
$('#indirizzo').blur(function(){Bbar('indirizzo');});
//Prezzo
$('#prezzo').click(function(){Wbar('prezzo');});
$('#prezzo').blur(function(){Bbar('prezzo');});
//Email
$('#email').click(function(){Wbar('email');});
$('#email').blur(function(){Bbar('email');});
//Telefono
$('#telefono').click(function(){Wbar('telefono');});
$('#telefono').blur(function(){Bbar('telefono');});

//SUBMISSION
$('#insertPost').attr('onsubmit','return checkSubmit();');

//fine document ready
});

