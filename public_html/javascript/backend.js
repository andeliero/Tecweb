// BACKEND
//-----FORM-----

var def=new Array(),check=new Array();//def conterrà il valore di default dato come help,check contiene gli id degli elementi della form
//FUNZIONI ONLOAD

function setArray(){//def è un array associativo del tipo def[id]="valore di default del placeholder"
var a=document.getElementById("formfield");
a=removeBlankspace(a);
a=a.getElementsByTagName("div");
for(var i=0;i<a.length;++i)
{
	check[i]=a[i].firstChild.id;//non è inutile come può sembrare,mi serve nella funzione checkSubmit
	def[a[i].firstChild.id]=a[i].firstChild.value;
}
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
    if(child.nodeType == 1)//document
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
if(document.getElementById(x).value == def[x])
	document.getElementById(x).value= "";
}

function checkSonNum(u){
	if(u.childNodes.length<=1)
		return true;
	else
		return false;
}

function insertHelp(x){
	var node=document.createElement("span");//node globale,lo creo qui per la prima volta
	node.className="jsHelp";
	node.appendChild(document.createTextNode(def[x]));
	document.getElementById(x).parentNode.appendChild(node);
}

//FUNZIONI ONBLUR

function Bbar(x){
//controllo che siano diversi perchè altrimenti selezionando tutto il valore di default di un input(senza fare onclick) e poi facendo onblur l'utente può distruggere i campi input
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
//funzione che richiama i controlli sui singoli campi della form all'interno del ciclo for
function checkSubmit(){
var state=true;
for(var i=0;i< check.length;++i)
	{
		var y="C"+check[i];
		var txt=window[y]();//trasformo la stringa in una chiamata a funzione e il valore ritornato lo salvo in txt
		var parent=document.getElementById(check[i]).parentNode;
		if(checkSonNum(parent)&&txt){
			parent.appendChild(createErr(txt));
		}
		if(txt)//devo usare un if aggiuntivo e non posso inserirlo nel precedente perchè l'utente potrebbe inserire più volte un form non valido senza cliccare realmente su nessun elemento
			state=false;
	}
return state;
}

function Ctitolo(){
	var t="titolo";
	var string=document.getElementById(t).value;
	if(string.length<2 || string.length>75 || string==def[t])
		return document.createTextNode("inserire un minimo di 2 e un massimo di 75 caratteri");
	else
		return false;
}

function Calt(){
	var t="alt";
	var string=document.getElementById(t).value;
	var n=countWords(string,' ');
	if(n<2 || n>50 || string==def[t])
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
	if(n<5 || n>50 || string==def[t])
		return document.createTextNode("inserire un minimo di 5 e un massimo di 50 parole");
	else
		return false;
}

function Cdescrizione(){
	var t="descrizione";
	var string=document.getElementById(t).value;
	var n=countWords(string,' ');
	if(n<50 || n>500 || string==def[t])
		return document.createTextNode("inserire un minimo di 50 e un massimo di 500 parole");
	else
		return false;
}

function Ctags(){
	var t="tags";
	var string=document.getElementById(t).value;
	var n=countWords(string,',');
	if(n<1 || n>20 || string==def[t])
		return document.createTextNode("inserire un minimo di 1 e un massimo di 20 tag,se più di uno allora separarli usando la virgola.");
	else
		return false;
}

//SUBMIT DI INTERVISTE

function Cintervistato(){
	var t="intervistato";
	var string=document.getElementById(t).value;
	var n=countWords(string,' ');
	if(n<1 || n>5 || string==def[t])
		return document.createTextNode("inserire un minimo di 1 e un massimo di 5 parole");
	else
		return false;
}

//SUBMIT DI EVENTI

//^([02]\/[0-2][0-9]\/[20](((0|2|4|6|8)(0|4|8))|((1|3|5|7|9)(2|6))))|([02]\/[0-2][0-8]\/[20](([0-9](13|5|7|9))|((1|3|5|7|9)(0|4|8))|((0|2|4|6|8)(2|6))))|((01|03|05|07|08|10|12)\/[0-31]\/[20]\d{2})|((04|06|09|11)\/[0-30]\/[20]\d{2})$/
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
	if(string.length<1 || string.length>58 || string==def[t])
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
	if(num<2 || num>15 || string==def[t])
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
	if(bool)
	{	for(var i=0; i<check.length; ++i)
			setCookie(check[i],document.getElementById(check[i]).value,365);
		}
	return bool;
}
//funzioni invocate da checksubmit()
function Cusername(){
	var t="username";
	var string=document.getElementById(t).value;
	if(string.length<1 || string.length>20 || string==def[t])
		return document.createTextNode("inserire uno username valido di al massimo 20 caratteri");
	else
		return false;
}

function Cpassword(p){//se chiamata senza parametri-->p="undefined"
	p= (typeof(p) === "undefined") ? "password" : p ;
	var string=document.getElementById(p).value;
	if(string.length<7 || string.length>20 || string==def[p])
		return document.createTextNode("inserire una password di 7-20 caratteri");
	else
		return false;
}

//----REGISTRAZIONE---

function CconfermaPass(){
	if(!(Cpassword("confermaPass")) && (document.getElementById("confermaPass").value == document.getElementById("password").value))
	//sicuramente password è valida,altrimenti l'uguaglianza tra i valori di confermaPass e password fallirebbe
		return false;
	else
		return document.createTextNode("le password non corrispondono oppure la password non é valida");
}