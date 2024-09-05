function request(){

var prompt = document.forms.datos.prompt.value;

var datos = {
model: "tinyllama",
prompt: prompt,
stream: false
};


var url = "http://localhost:11434/api/generate";
var request = new XMLHttpRequest();
request.open("POST",url);
request.send(JSON.stringify(datos));

request.onload = () => {
if(request.status === 200){
alert("RESPONSE");
}else{
alert("algo fallo");
};