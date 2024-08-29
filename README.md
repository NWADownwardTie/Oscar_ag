# Oscar_ag
Repositorio de prueba para implementar LLM y una aplicacion web
documentacion para saber que hacer

# 1. Instalacion

Como primer paso descargamos [ollama](https://ollama.com/download/linux) de su pagina web. y ejecutamos el siguiente comando:

````bash
$ curl -fsSL https://ollama.com/install.sh | sh
````

## 2. Ejecutar el servidor

Ejercutar el servidor de API REST de ollama con el siguiente comando:

````bash
& ollama serve
````

## 3. Descargar un modelo

En la pagina de ollama descargar un [Modelo](https://ollama.com/library) utilizando el siguiente comando: 

````bash
$ ollama pull tinyllama
````

## 4. Realizar un request a la API REST

para realizar una consulta utilizamos el comando curl como se muestra en el siguiente ejemplo:

````bash
curl -X POST http://localhost:11434/api/generate -d '{
"model": "tinyllama",
"prompt": "Why is the sky blue?"
}'
````

## 5. Realizar un request sin stream

Para realizar una consulta a la API REST sin stream se hace de la siguiente forma: 

````bash
curl -X POST http://localhost:11434/api/generate -d '{
"model": "tinyllama",
"prompt": "Why is the sky blue?",
"stream": false
}'
````
