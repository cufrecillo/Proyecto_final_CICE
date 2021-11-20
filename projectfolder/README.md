 ### Pokemon

 1. Crear clase Pokemon con los siguientes atributos y métodos
	* name
	* type
	* HP
	* attacks []
	* Métodos: learn_attack, attack, receive_damage


 2. Crear clase Attack con los siguientes atributos
	 * name
	 * type
	 * damage

 3. Crear un pequeño menú que permita simular una batalla pokemon


 4. Permitir al usuario cambiar de Pokemon y que respete el HP disminuido en el combate.


 5. Permitir elegir lista de Pokemons.


6. Menu Usuario para alta y login
	* acceso mediante token al juego
	* si el usuario no esta logado y con un tiempo controlado, no permite el acceso


main.py
Menu principal con acceso a USUARIOS y JUEGO.
Se controla el alta y login de USUARIOS.


gba.py
Se desarrolla todo el juego, control de turnos y victoria.


funs.py
Todas las funciones necesarias para el desarrollo del proyecto.


pokemons.py
Clase pokemon, clase ataque y creacion de personajes.

requirements.tex
librerias necesarias

users.json
archivo con los usuarios creados