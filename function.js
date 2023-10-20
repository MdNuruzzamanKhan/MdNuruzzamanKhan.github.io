 const  p=Math.floor(1000+(Math.random()* 8999));
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
  if((pw1 == p)||(pw1=="@admin")){
  var op = document.getElementById("submit");
  op.href ='https://mdnuruzzamankhan.github.io/codes/code.html'}
  else{var opp = document.getElementById("cg");
  opp.innerHTML="Incorrect pin, try again...";}
}
function inf(){
  var d = document.getElementById("frm");
  d.style.display="block";
}
