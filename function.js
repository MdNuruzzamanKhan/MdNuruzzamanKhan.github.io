const  p=Math.floor(Math.random() * 100);
function pin(){
var b = document.getElementById("fn");
 let c=fn.value;
 alert(`Hey ${c}, Welcome to my first website!!!`);


const div=document.getElementById("frm");
div.innerHTML =`Your PIN=${p}` ;
}
function bio(){
  var a = document.getElementById("ame");
  a.style.display="block";}
function pw(){
  var pw = document.getElementById("pw");
  let pw1 = pw.value;
  if(pw1 = p){
  var op = document.getElementById("submit");
  op.href ='https://mdnuruzzamankhan.github.io/aboutme.html'}
  
}
function inf(){
  var d = document.getElementById("frm");
  d.style.display="block";
}
// Used to toggle the menu on small screens when clicking on the menu button
function myFunction() {
  var x = document.getElementById("navDemo");
  if (x.className.indexOf("w3-show") == -1) {
    x.className += " w3-show";
  } else { 
    x.className = x.className.replace(" w3-show", "");
  }
}
