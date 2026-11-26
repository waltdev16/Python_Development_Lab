# Banco de preguntas original del ejercicio.
QUESTIONS = {
    'arte' : {
        '1' : ['¿Cuál de los siguientes elementos es esencial en las artes visuales?', {
            'a' : 'Ritmo',
            'b' : 'Línea',
            'c' : 'Sabor',
            'd' : 'Color'
        }, 'b', 20],
        '2' : ['¿Qué es el arte?', {
            'a' : 'Un conjunto de técnicas científicas',
            'b' : 'Una forma de expresión humana',
            'c' : 'Un medio de entretenimiento sin valor cultural',
            'd' : 'Una técnica limitada a la pintura',
            'e' : 'Un lenguaje simbólico y creativo'
        }, 'b', 10],
        '3' : ['El arte abstracto busca representar fielmente la realidad visible.', {
            'a' : 'Verdadero',
            'b' : 'Falso'
        }, 'b', 10],
        '4' : ['¿Cuál de estos artistas fue parte del movimiento impresionista?', {
            'a' : 'Claude Monet',
            'b' : 'Pablo Picasso',
            'c' : 'Andy Warhol'
        }, 'a', 20],
        '5' : ['¿Qué técnicas se emplean en la escultura?', {
            'a' : 'Tallado',
            'b' : 'Fundición',
            'c' : 'Modelado',
            'd' : 'Esmaltado',
            'e' : 'Acuarela',
            'f' : 'Ensamblaje'
        }, 'a', 10],
        '6' : ['¿Cuál de los siguientes movimientos artísticos surgió en el siglo XX?', {
            'a' : 'Renacimiento',
            'b' : 'Barroco',
            'c' : 'Surrealismo',
            'd' : 'Romanticismo'
        }, 'c', 20],
        '7' : ['¿En qué país surgió el Renacimiento?', {
            'a' : 'Francia',
            'b' : 'Italia',
            'c' : 'Alemania'
        }, 'b', 10],
        '8' : ['¿Qué características definen al arte barroco?', {
            'a' : 'Uso de la abstracción',
            'b' : 'Emoción y dramatismo',
            'c' : 'Exceso de ornamento',
            'd' : 'Simetría minimalista',
            'e' : 'Contrastes de luz y sombra'
        }, 'b', 10],
        '9' : ['¿Qué disciplinas forman parte de las llamadas “bellas artes”?', {
            'a' : 'Pintura',
            'b' : 'Escultura',
            'c' : 'Arquitectura',
            'd' : 'Gastronomía',
            'e' : 'Música',
            'f' : 'Danza'
        }, 'a', 20],
        '10' : ['¿Cuál de los siguientes artistas pintó "Guernica"?', {
            'a' : 'Salvador Dalí',
            'b' : 'Pablo Picasso',
            'c' : 'Diego Velázquez'
        }, 'b', 10]
    },
    'ciencia' : {
        '1': ['¿Cuál es la unidad básica de la vida?', {
            'a': 'Átomo',
            'b': 'Célula',
            'c': 'Molécula',
            'd': 'Tejido'
        }, 'b', 10],
        '2': ['¿El agua está compuesta por dos átomos de hidrógeno y uno de oxígeno?', {
            'a': 'Verdadero',
            'b': 'Falso'
        }, 'a', 20],
        '3': ['¿Cuál de los siguientes planetas es el más cercano al Sol?', {
            'a': 'Venus',
            'b': 'Tierra',
            'c': 'Mercurio'
        }, 'c', 10],
        '4': ['¿Qué tipo de energía se obtiene del sol?', {
            'a': 'Eólica',
            'b': 'Térmica',
            'c': 'Solar',
            'd': 'Cinética'
        }, 'c', 10],
        '5': ['¿Todos los metales son líquidos a temperatura ambiente?', {
            'a': 'Verdadero',
            'b': 'Falso'
        }, 'b', 10],
        '6': ['¿Cuáles de los siguientes son estados de la materia?', {
            'a': 'Sólido',
            'e': 'Radiante',
            'f': 'Vibrante'
        }, 'a', 20],
        '7': ['¿Cuál es el planeta más grande del sistema solar?', {
            'a': 'Saturno',
            'b': 'Júpiter',
            'c': 'Neptuno',
            'd': 'Urano'
        }, 'b', 10],
        '8': ['¿El ADN se encuentra en el núcleo de la célula?', {
            'a': 'Sí',
            'b': 'No'
        }, 'a', 10],
        '9': ['¿Cuál de los siguientes órganos es responsable de bombear la sangre en el cuerpo humano?', {
            'a': 'Pulmón',
            'b': 'Riñón',
            'c': 'Corazón',
            'd': 'Hígado'
        }, 'c', 20],
        '10': ['¿La Tierra gira alrededor del Sol?', {
            'a': 'Verdadero',
            'b': 'Falso'
        }, 'a', 10]
    },
    'deporte' : {
        '1': ['¿Cuál de los siguientes es un deporte olímpico?', {
            'a': 'Ajedrez',
            'b': 'Tenis',
            'c': 'Póker',
            'd': 'Dominó'
        }, 'b', 10],
        '2': ['¿Qué país ha ganado más Copas Mundiales de fútbol masculino?', {
            'a': 'Italia',
            'b': 'Argentina',
            'c': 'Brasil',
            'd': 'Alemania',
            'e': 'Francia'
        }, 'c', 20],
        '3': ['¿El atletismo es una disciplina deportiva?', {
            'a': 'Sí',
            'b': 'No'
        }, 'a', 10],
        '4': ['¿El baloncesto se juega con una pelota ovalada?', {
            'a': 'Verdadero',
            'b': 'Falso'
        }, 'b', 10],
        '5': ['¿Cuántos jugadores tiene un equipo de voleibol en cancha?', {
            'a': '5',
            'b': '6',
            'c': '7',
            'd': '11'
        }, 'b', 10],
        '6': ['¿El golf es un deporte de contacto físico?', {
            'a': 'Verdadero',
            'b': 'Falso'
        }, 'b', 10],
        '7': ['¿Quién ganó el mayor número de medallas olímpicas en natación?', {
            'a': 'Caeleb Dressel',
            'b': 'Mark Spitz',
            'c': 'Ian Thorpe',
            'd': 'Michael Phelps'
        }, 'd', 20],
        '8': ['¿Cuál de los siguientes deportes se practica sobre hielo?', {
            'a': 'Esquí alpino',
            'b': 'Hockey sobre hielo',
            'c': 'Ciclismo',
            'd': 'Remo'
        }, 'b', 10],
        '9': ['¿El boxeo y la esgrima son considerados deportes de combate?', {
            'a': 'Verdadero',
            'b': 'Falso'
        }, 'a', 10],
        '10': ['¿Qué implemento se usa en el béisbol?', {
            'a': 'Raqueta',
            'b': 'Bate',
            'c': 'Arco',
            'd': 'Palo de golf'
        }, 'b', 10]
    },
    'entretenimiento' : {
        '1': ['¿Cuál de estos personajes pertenece al universo de Marvel?', {
            'a': 'Batman',
            'b': 'Iron Man',
            'c': 'Superman',
            'd': 'Flash'
        }, 'b', 20],
        '2': ['¿La serie "Stranger Things" fue producida por Netflix?', {
            'a': 'Verdadero',
            'b': 'Falso'
        }, 'a', 10],
        '3': ['¿Cuál de las siguientes películas ganó el Óscar a Mejor Película en 1997?', {
            'a': 'Titanic',
            'b': 'Gladiador',
            'c': 'Forrest Gump',
            'd': 'El paciente inglés'
        }, 'a', 20],
        '4': ['¿Quién es el creador de la saga de "Star Wars"?', {
            'a': 'George Lucas',
            'b': 'Steven Spielberg',
            'c': 'James Cameron'
        }, 'a', 10],
        '5': ['¿El videojuego "Minecraft" fue lanzado antes que "Fortnite"?', {
            'a': 'Sí',
            'b': 'No'
        }, 'a', 10],
        '6': ['¿Cuál de estos cantantes es conocido por usar un guante blanco en sus presentaciones?', {
            'a': 'Freddie Mercury',
            'b': 'Michael Jackson',
            'c': 'Bruno Mars',
            'd': 'Elvis Presley'
        }, 'b', 10],
        '7': ['¿Cuál de las siguientes películas pertenece al género de ciencia ficción?', {
            'a': 'Matrix',
            'b': 'El diario de una pasión',
            'c': 'Coco',
            'd': 'Titanic'
        }, 'a', 10],
        '8': ['¿El anime "Naruto" se originó en Corea del Sur?', {
            'a': 'Verdadero',
            'b': 'Falso'
        }, 'b', 10],
        '9': ['¿Cuál de los siguientes formatos es utilizado para escuchar música digitalmente?', {
            'a': 'MP3',
            'b': 'DOCX',
            'c': 'JPEG',
            'd': 'TXT'
        }, 'a', 20],
        '10': ['¿Cuáles de los siguientes son plataformas de streaming?', {
            'a': 'Netflix',
            'b': 'Snapchat',
            'c': 'Spotify',
            'd': 'YouTube',
            'e': 'TikTok',
            'f': 'Word'
        }, 'a', 10]
    },
    'historia' : {
        '1': ['¿En qué año comenzó la Primera Guerra Mundial?', {
            'a': '1914',
            'b': '1918',
            'c': '1939',
            'd': '1945'
        }, 'a', 20],
        '2': ['¿La Revolución Francesa ocurrió en el siglo XVIII?', {
            'a': 'Verdadero',
            'b': 'Falso'
        }, 'a', 10],
        '3': ['¿Quién fue el primer presidente de Estados Unidos?', {
            'a': 'Thomas Jefferson',
            'b': 'George Washington',
            'c': 'Abraham Lincoln',
            'd': 'John Adams'
        }, 'b', 20],
        '4': ['¿La caída del Imperio Romano de Occidente ocurrió en el año 476 d.C.?', {
            'a': 'Sí',
            'b': 'No'
        }, 'a', 10],
        '5': ['¿Qué imperio construyó Machu Picchu?', {
            'a': 'Imperio Azteca',
            'b': 'Imperio Inca',
            'c': 'Imperio Maya',
            'd': 'Imperio Romano'
        }, 'b', 10],
        '6': ['¿El Renacimiento fue un movimiento cultural que comenzó en Italia?', {
            'a': 'Verdadero',
            'b': 'Falso'
        }, 'a', 10],
        '7': ['¿Quién descubrió América en 1492?', {
            'a': 'Vasco da Gama',
            'b': 'Cristóbal Colón',
            'c': 'Ferdinand Magellan',
            'd': 'James Cook'
        }, 'b', 20],
        '8': ['¿La Revolución Industrial comenzó en el siglo XIX?', {
            'a': 'Verdadero',
            'b': 'Falso'
        }, 'a', 10],
        '9': ['¿Cuál de los siguientes países fue parte de las Potencias Centrales en la Primera Guerra Mundial?', {
            'a': 'Francia',
            'b': 'Alemania',
            'c': 'Reino Unido',
            'd': 'Estados Unidos'
        }, 'b', 10],
        '10': ['¿La Carta Magna fue firmada en Inglaterra?', {
            'a': 'Sí',
            'b': 'No'
        }, 'a', 20]
    },
    'geografia' : {
        '1': ['¿Cuál es el río más largo del mundo?', {
            'a': 'Nilo',
            'b': 'Amazonas',
            'c': 'Yangtsé',
            'd': 'Misisipi'
        }, 'a', 20],
        '2': ['¿El Monte Everest es la montaña más alta del mundo?', {
            'a': 'Verdadero',
            'b': 'Falso'
        }, 'a', 10],
        '3': ['¿En qué continente se encuentra Egipto?', {
            'a': 'Asia',
            'b': 'África',
            'c': 'Europa',
            'd': 'Oceanía'
        }, 'b', 10],
        '4': ['¿Cuál es la capital de Australia?', {
            'a': 'Sydney',
            'b': 'Melbourne',
            'c': 'Canberra'
        }, 'c', 20],
        '5': ['¿Cuál es el océano más grande del planeta?', {
            'a': 'Atlántico',
            'b': 'Pacífico',
            'c': 'Índico',
            'd': 'Ártico'
        }, 'b', 10],
        '6': ['¿La línea ecuatorial divide la Tierra en dos hemisferios?', {
            'a': 'Sí',
            'b': 'No'
        }, 'a', 10],
        '7': ['¿Cuál es el país más grande en superficie?', {
            'a': 'Canadá',
            'b': 'China',
            'c': 'Rusia',
            'd': 'Estados Unidos'
        }, 'c', 20],
        '8': ['¿Qué país tiene la mayor cantidad de islas en el mundo?', {
            'a': 'Filipinas',
            'b': 'Indonesia',
            'c': 'Suecia',
            'd': 'Canadá'
        }, 'c', 10],
        '9': ['¿El desierto del Sahara está en América?', {
            'a': 'Verdadero',
            'b': 'Falso'
        }, 'b', 10],
        '10': ['¿Cuál de los siguientes países no pertenece a América del Sur?', {
            'a': 'Colombia',
            'b': 'Perú',
            'c': 'México',
            'd': 'Chile'
        }, 'c', 20]
    },
}

