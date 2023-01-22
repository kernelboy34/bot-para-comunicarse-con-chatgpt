import tkinter as tk
import pyttsx3
import openai

voz=pyttsx3.init()
voice_id ='spanish-latin-am'
voz.setProperty('voice',voice_id)
rate=voz.getProperty('rate')
voz.setProperty('rate',rate-50)
openai.api_key = "tuapixd"
modelo = "text-davinci-002"
prompt = "Hola, soy bebe ¿En qué puedo ayudarte hoy?"
completado = openai.Completion.create( model=modelo,prompt=prompt, max_tokens=1024, n=1, stop=None, temperature=0.5)
mensaje = completado.choices[0].text
voz.say(prompt)
voz.runAndWait()
ventana = tk.Tk()
ventana.title("Asistente")
ventana.geometry("400x400")
etiqueta = tk.Label(ventana, text="Hola, soy bebe. ¿En qué puedo ayudarte hoy?")
etiqueta.pack()
caja_texto = tk.Entry(ventana)
caja_texto.pack()
boton = tk.Button(ventana, text="Enviar", command=mensaje)
boton.pack()
etiqueta_respuesta = tk.Label(ventana)
etiqueta_respuesta.pack()
#hecho por kernelboy34
