/* SEARCHBAR */

function searchbar(){
 document.getElementById("text_field").value="";
}
 function defsearch(){
 document.getElementById("text_field").value="Cerca...";
}

/* GALLERY */

var index=1,last,last0;
var li= document.getElementsByClassName("slide");

function next() {
    document.getElementById("img"+index).setAttribute("class", "hidden");
    document.getElementById("t"+index).setAttribute("class","");
    if( index == li.length)// .length inizia a contare da 1
        index=1;
    else
        index++;
    document.getElementById("img"+index).setAttribute("class", "active");
    document.getElementById("t"+index).setAttribute("class","activenav");
    return true;
}

function previous() {
 document.getElementById("img"+index).setAttribute("class", "hidden");
 document.getElementById("t"+index).setAttribute("class","");
    if(index == 1)
        index= li.length;
    else
        index--;
   document.getElementById("img"+index).setAttribute("class", "active");
   document.getElementById("t"+index).setAttribute("class","activenav");
    return true;
}
function change(i){
    document.getElementById("img"+index).setAttribute("class","hidden");
    document.getElementById("t"+index).setAttribute("class","");
    index= i;
    document.getElementById("img"+index).setAttribute("class", "active");
    document.getElementById("t"+index).setAttribute("class","activenav");
    return true;
}