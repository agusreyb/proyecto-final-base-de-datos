import psycopg2
import pandas as pd
import customtkinter as ctk
import tkinter as tk
from pandasgui import show
import configparser
import os

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Consultas a PostgreSQL")
        self.geometry("900x600")
        
         # Frame principal
        frame = ctk.CTkFrame(self)
        frame.pack(pady=20, padx=60, fill="both", expand=True)

        # Titulo en la parte superior
        self.titulo = ctk.CTkLabel(frame, text="Gestión de base de datos universitaria", font=ctk.CTkFont(size=20, weight="bold"))
        self.titulo.grid(row=0, column=0, columnspan=2, pady=10, sticky="n")

        # Configurar las columnas para que se expandan y se centren
        frame.grid_columnconfigure(0, weight=1, uniform="equal")
        frame.grid_columnconfigure(1, weight=1, uniform="equal")

        # Botones en la primera fila, pero en dos columnas
        self.botonTablaAlumnos = ctk.CTkButton(
            frame, 
            text="SELECT * FROM ALUMNO;", 
            command=self.TablaAlumno,
            width=300,  
            height=40, 
            font=ctk.CTkFont(size=18) 
        )
        self.botonTablaAlumnos.grid(row=1, column=0, pady=5, padx=10, sticky="ew")

        self.botonTablaHobbies = ctk.CTkButton(
            frame, 
            text="SELECT * FROM HOBBIE;", 
            command=self.TablaHobbies,
            width=300,  
            height=40, 
            font=ctk.CTkFont(size=18) 
        )
        self.botonTablaHobbies.grid(row=1, column=1, pady=5, padx=10, sticky="ew")

        # Botones en la segunda fila, también en dos columnas
        self.botonTablaGrupo = ctk.CTkButton(
            frame, 
            text="SELECT * FROM GRUPO;", 
            command=self.TablaGrupo,
            width=300,  
            height=40, 
            font=ctk.CTkFont(size=18) 
        )
        self.botonTablaGrupo.grid(row=2, column=0, pady=5, padx=10, sticky="ew")

        self.botonTablaLocalidad = ctk.CTkButton(
            frame, 
            text="SELECT * FROM LOCALIDAD;", 
            command=self.TablaLocalidad,
            width=300,  
            height=40, 
            font=ctk.CTkFont(size=18) 
        )
        self.botonTablaLocalidad.grid(row=2, column=1, pady=5, padx=10, sticky="ew")
        
        self.botonTablaLocalidad = ctk.CTkButton(
            frame, 
            text="Parte 4 - 2)a);", 
            command=self.Parte4DosA,
            width=300,  
            height=40, 
            font=ctk.CTkFont(size=18) 
        )
        self.botonTablaLocalidad.grid(row=3, column=0, pady=5, padx=10, sticky="ew")
        
        self.botonTablaLocalidad = ctk.CTkButton(
            frame, 
            text="Parte 4 - 2)b)", 
            command=self.Parte4DosB,
            width=300,  
            height=40, 
            font=ctk.CTkFont(size=18) 
        )
        self.botonTablaLocalidad.grid(row=3, column=1, pady=5, padx=10, sticky="ew")
        
        self.botonTablaLocalidad = ctk.CTkButton(
            frame, 
            text="Parte 4 - 2)c)", 
            command=self.Parte4DosC,
            width=300,  
            height=40, 
            font=ctk.CTkFont(size=18) 
        )
        self.botonTablaLocalidad.grid(row=4, column=0, pady=5, padx=10, sticky="ew")
        
        self.botonTablaLocalidad = ctk.CTkButton(
            frame, 
            text="Parte 4 - 2)d)", 
            command=self.Parte4DosD,
            width=300,  
            height=40, 
            font=ctk.CTkFont(size=18) 
        )
        self.botonTablaLocalidad.grid(row=4, column=1, pady=5, padx=10, sticky="ew")
        
        self.botonTablaLocalidad = ctk.CTkButton(
            frame, 
            text="Parte 4 - 3)a)", 
            command=self.Parte4TresA,
            width=300,  
            height=40, 
            font=ctk.CTkFont(size=18) 
        )
        self.botonTablaLocalidad.grid(row=5, column=0, pady=5, padx=10, sticky="ew")
        
        self.botonTablaLocalidad = ctk.CTkButton(
            frame, 
            text="Parte 4 - 3)b)", 
            command=self.Parte4TresB,
            width=300,  
            height=40, 
            font=ctk.CTkFont(size=18) 
        )
        self.botonTablaLocalidad.grid(row=5, column=1, pady=5, padx=10, sticky="ew")
                
        self.botonTablaLocalidad = ctk.CTkButton(
            frame, 
            text="Consulta Personalizada", 
            command=self.abrir_ventana_input,
            width=300,  
            height=40, 
            font=ctk.CTkFont(size=18) 
        )
        self.botonTablaLocalidad.grid(row=6, column=0, pady=5, padx=10, sticky="ew")        
                
    def consultaSQL(self, consulta):
        try:
            #Conectar a la base de datos
            conn = psycopg2.connect(
                host=host,
                port=port,
                dbname=dbname,
                user=user,
                password=password
            )
            #Crear un cursor para ejecutar consultas
            cursor = conn.cursor()
            cursor.execute(consulta)

            #Obtener los nombres de las columnas
            columnas = [desc[0] for desc in cursor.description]

            #Obtener los resultados de la consulta
            resultados = cursor.fetchall()

            #Convertir los resultados en un DataFrame de Pandas
            df = pd.DataFrame(resultados, columns=columnas)

            #Mostrar el DataFrame en una ventana interactiva
            show(df)

            #Cerrar el cursor y la conexión
            cursor.close()
            conn.close()

        except Exception as e:
            tk.messagebox.showerror("Error", f"Error al conectar con la base de datos:\n{e}")
            print(f"Error al conectar con la base de datos: {e}")
            
    def TablaAlumno(self):
        self.consultaSQL("SELECT * FROM ALUMNO;")
        
    def TablaHobbies(self):
        self.consultaSQL("SELECT * FROM HOBBIE;")
        
    def TablaGrupo(self):
        self.consultaSQL("SELECT * FROM GRUPO;")        

    def TablaLocalidad(self):
        self.consultaSQL("SELECT * FROM LOCALIDAD;")   
        
    def Parte4DosA(self):
        query = """
        SELECT localidad, hobbie, total_alumnos
        FROM (
            SELECT DISTINCT ON (LOCALIDAD.nombre_localidad)
                LOCALIDAD.nombre_localidad AS localidad,
                HOBBIE.nombre_hobbie AS hobbie,
                COUNT(ALUMNO_TIENE_HOBBIE.alumno_id) AS total_alumnos
            FROM ALUMNO_TIENE_HOBBIE
            INNER JOIN HOBBIE ON ALUMNO_TIENE_HOBBIE.hobbie_id = HOBBIE.id_hobbie
            INNER JOIN ALUMNO ON ALUMNO_TIENE_HOBBIE.alumno_id = ALUMNO.id_alumno
            INNER JOIN LOCALIDAD ON ALUMNO.localidad_fk = LOCALIDAD.id_localidad
            GROUP BY LOCALIDAD.nombre_localidad, HOBBIE.nombre_hobbie
            ORDER BY LOCALIDAD.nombre_localidad, total_alumnos DESC
        ) AS subquery
        ORDER BY total_alumnos DESC;
        """
        self.consultaSQL(query)
        
    def Parte4DosB(self):
        query = """
        SELECT
        apellido ||', '|| nombre_alumno AS "Alumno" ,
        COUNT(ALUMNO_CURSA_MATERIA.materia_id) AS "Materias en curso",
        experiencia_relacional AS "Experiencia BD Relacional",
        experiencia_no_relacional AS "Experiencia BD No Relacional"
        FROM ALUMNO
        INNER JOIN ALUMNO_CURSA_MATERIA ON ALUMNO.id_alumno = ALUMNO_CURSA_MATERIA.alumno_id
        GROUP BY "Alumno", experiencia_relacional, experiencia_no_relacional
        ORDER BY "Materias en curso" DESC
        LIMIT 5;
        """
        self.consultaSQL(query)    
        
    def Parte4DosC(self):
        query = """
        SELECT DISTINCT ON (GRUPO.nombre_grupo)
        GRUPO.nombre_grupo AS "Grupo",
        MATERIA.nombre_materia AS "Materia",
        COUNT(ALUMNO_CURSA_MATERIA.alumno_id) AS "Alumnos inscriptos",
        (COUNT(ALUMNO_CURSA_MATERIA.alumno_id)*100/5)||'%' AS "% del Grupo"
        FROM ALUMNO
        INNER JOIN GRUPO ON GRUPO.id_grupo = ALUMNO.grupo_fk
        INNER JOIN ALUMNO_CURSA_MATERIA ON ALUMNO.id_alumno = ALUMNO_CURSA_MATERIA.alumno_id
        INNER JOIN MATERIA ON MATERIA.id_materia = ALUMNO_CURSA_MATERIA.materia_id
        GROUP BY "Grupo", "Materia"
        ORDER BY "Grupo","Alumnos inscriptos" DESC
        """
        self.consultaSQL(query)    
        
    def Parte4DosD(self):
        query = """
        SELECT 
        apellido ||', '|| nombre_alumno AS "Alumno",
        experiencia_relacional AS "Experiencia BD Relacional",
        experiencia_no_relacional AS "Experiencia BD No Relacional",
        TRABAJO.nombre_trabajo AS "Actividad"
        FROM ALUMNO
        INNER JOIN TRABAJO ON TRABAJO.id_trabajo = ALUMNO.trabajo_fk
        INNER JOIN RUBRO ON RUBRO.id_rubro = TRABAJO.rubro_fk
        WHERE RUBRO.id_rubro = 6 --"IT"
        ORDER BY experiencia_relacional DESC, experiencia_no_relacional DESC
        LIMIT 5;
        """
        self.consultaSQL(query)      
        
    def Parte4TresA(self):
        query = """
        SELECT 
        LOCALIDAD.nombre_localidad AS "Localidad",
        ROUND(AVG(alumno_materias.total_materias), 2) AS "Promedio de materias",
        COUNT(DISTINCT ALUMNO.id_alumno) AS "Total Alumnos"
        FROM ALUMNO
        INNER JOIN LOCALIDAD ON ALUMNO.localidad_fk = LOCALIDAD.id_localidad
        INNER JOIN (
        SELECT alumno_id, COUNT(materia_id) AS total_materias
        FROM ALUMNO_CURSA_MATERIA
        GROUP BY alumno_id
        ) AS alumno_materias ON ALUMNO.id_alumno = alumno_materias.alumno_id
        GROUP BY "Localidad"
        ORDER BY "Total Alumnos" DESC;
        """
        self.consultaSQL(query)      
    
    def Parte4TresB(self):
        query = """
        SELECT DISTINCT ON (A1.id_alumno)
    A1.apellido AS "Alumno",
    A2.apellido AS "Potencial Mentor",
    H1.nombre_hobbie AS "Interés Común",
    A2.experiencia_relacional AS "Experiencia Mentor BD Relacional",
    A2.experiencia_no_relacional AS "Experiencia Mentor BD NO Relacional"
FROM
    ALUMNO A1
INNER JOIN ALUMNO_TIENE_HOBBIE AH1 ON A1.id_alumno = AH1.alumno_id
INNER JOIN HOBBIE H1 ON AH1.hobbie_id = H1.id_hobbie
INNER JOIN ALUMNO_TIENE_HOBBIE AH2 ON H1.id_hobbie = AH2.hobbie_id
INNER JOIN ALUMNO A2 ON AH2.alumno_id = A2.id_alumno
WHERE
    A1.id_alumno <> A2.id_alumno -- Evitar que el alumno sea su propio mentor
    AND (
        A2.experiencia_relacional = TRUE
        OR A2.experiencia_no_relacional = TRUE
    )
ORDER BY 
    A1.id_alumno
LIMIT 10;
        """
        self.consultaSQL(query)         
    
    
    def abrir_ventana_input(self):
        ventana_input = tk.Toplevel(self)  
        ventana_input.title("Entrada de usuario")
        ventana_input.geometry("300x150")

        etiqueta = tk.Label(ventana_input, text="Ingrese su texto:")
        etiqueta.pack(pady=10)

        entrada_texto = tk.Entry(ventana_input, width=30)
        entrada_texto.pack(pady=10)
        
        def confirmar():
            texto = entrada_texto.get() 
            print(f"Texto ingresado: {texto}")
            self.consultaSQL(texto)
            ventana_input.destroy()  

        boton_confirmar = tk.Button(ventana_input, text="Confirmar", command=confirmar)
        boton_confirmar.pack(pady=10)



CONFIG_FILE = 'config.ini'

try:
    #Inicializa el objeto ConfigParser
    config = configparser.ConfigParser()

    #Obtén el directorio donde se encuentra el script actual
    script_dir = os.path.dirname(os.path.abspath(__file__))
    ruta_config = os.path.join(script_dir, CONFIG_FILE)
    #Lee el archivo de configuración
    config.read(ruta_config)

    #Obtén los parámetros de la sección [database]
    host = config['database']['host']
    port = config['database']['port']
    dbname = config['database']['dbname']
    user = config['database']['user']
    password = config['database']['password']

    #Lógica principal de tu aplicación
    print(f"Conectando a la base de datos en {host}:{port} con el usuario {user}")
    app = App()
    app.mainloop()

except FileNotFoundError as e:
    print(f"Error: {e}")
except KeyError as e:
    raise RuntimeError(f"Falta una clave en la configuración: {e}")
except Exception as e:
    raise RuntimeError(f"Error al leer el archivo de configuración: {e}")
