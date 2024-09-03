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

## 4.1 Realizar un request sin stream

Para realizar una consulta a la API REST sin stream se hace de la siguiente forma: 

````bash
curl -X POST http://localhost:11434/api/generate -d '{
"model": "tinyllama",
"prompt": "Why is the sky blue?",
"stream": false
}'
````

## Para guardar en GitHub

````bash
git add .
````

````bash
git commit -m "UPDATE REAMDE.md"
````

````bash
git push -u origin main
````

## 5. Consultar a groq
estructura basica para realizar una consulta a groq mediante su API REST

### Comando completo

````bash
curl "https://api.groq.com/openai/v1/chat/completions" \
  -X POST \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer ${GROQ_API_KEY}" \
  -d '{
         "messages": [
           {
             "role": "user",
             "content": ""
           }
         ],
         "model": "llama3-8b-8192",
         "temperature": 1,
         "max_tokens": 1024,
         "top_p": 1,
         "stream": true,
         "stop": null
       }'
  ````

### Comando que usamos en clase

````bash
  curl "https://api.groq.com/openai/v1/chat/completions" \
  -X POST \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer ${GROQ_API_KEY}" \
  -d '{
         "messages": [
           {
             "role": "user",
             "content": "¿por que el cielo es azul?"
           }
         ],
         "model": "llama3-8b-8192",
         "stream": false
       }'
````
