import pandas as pd
import sqlite3 as sql
#from google.colab import drive
from IPython.display import clear_output
import glob
import random
import os
import time
from .models import Condicionales

class Log(pd.DataFrame):
  def __init__(self):
    super().__init__()
    '''Crear un doble condicional general y particular. con AND. Para activar/desactivar LOG'''
    self.log_general = True
    self.log_parcial = False

  def clase(self):
    'Que clase es'
    self.descripcion = pd.DataFrame(data=[self.fila],columns=self.columnas)

  def salida(self):
    'Muestra en pantalla el pd.datafarame que contine la info de la clase'
    self.salida = pd.DataFrame(data=[self.fila],columns=self.columnas)

  def atributos(self):
    'df cada columna es un atributo'
    if (len(self.fila) > 0) and (len(self.columnas) > 0):
      self.atributos = pd.DataFrame(data=[self.fila],columns=self.columnas)
    else:
      self.atributos = pd.DataFrame()

  def lista_dfs(self, lista_dfs):
    'Imprime los dfs uno bajo otro'
    self.lista_dfs = lista_dfs

  def pantalla(self):
    'Imprime todo en orden'
    #clear_output()
    self.info = [
        self.descripcion,
        self.atributos
    ]

    if self.log_general == True and self.log_parcial == True:
      try:
        
        print('8888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888')
      
        for n in range(len(self.info)):
          if len(self.info[n]) > 0:
            #display(self.info[n])
            print(self.ingo[n])
          else:
            print('Atributos : ',len(self.info[n]),' len()')
          print('-------------------------------------------------------------------')
          print('')
        i = 1
        if len(self.lista_dfs)>0:
          for n in range(len(self.lista_dfs)):
            i = i * -1
            if i < 0:
              print(self.lista_dfs[n])
              print('Len: ',len(self.lista_dfs[n]))
            else:
              #display(self.lista_dfs[n].head(3))
              print('-------------------------------------------------------------------')
              print('')
        else:
          print('DFS : ',len(self.lista_dfs),' len()')
          print('')
        
         
        print('8888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888')
        print('8888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888')


      except TypeError as e:
        print('error en Log: ',e)
   

  def limpiar_log():
    '''Limpia la consola'''
    clear_output()
    
class Estructura(Log):
  def __init__(self):
    '''Contiene todas las variables en comun entre las clases.'''
    super().__init__()
    self.columnas = ['Clase','Funcion','Desctipcion']
    self.fila = ['EStructura.','__init__()','Contiene todas las variables en comun entre las clases']
    Log.clase(self)


    self.django = True
    #DF
    self.df_lista_porcentajes = pd.DataFrame(columns=['Nuevo','id','Anterior'])
    self.df_pll = pd.DataFrame(columns= ['id', 'Codigo', 'Relacional',
                                         'Nombre', 'Precio', 'Porcentaje',
                                         'Trabajado', 'Actualizado', 'Fecha',
                                         'Stock', 'Proveedores', 'Calidad',
                                         'Imagen'])
    self.df_bdd = pd.DataFrame(columns= ['id', 'Codigo', 'Relacional',
                                         'Nombre', 'Precio', 'Porcentaje',
                                         'Trabajado', 'Actualizado', 'Fecha',
                                         'Stock', 'Proveedores', 'Calidad',
                                         'Imagen'])
    self.df_tabla = pd.DataFrame({'0,1,2':['Codigo','Nombre','Precio'],
                                  '0,2,1':['Codigo','Precio','Nombre'],
                                  '1,0,2':['Nombre','Codigo','Precio'],
                                  '1,2,0':['Nombre','Precio','Codigo'],
                                  '2,0,1':['Precio','Codigo','Nombre'],
                                  '2,1,0':['Precio','Nombre','Codigo']})
    self.df_valor = pd.DataFrame(columns=['Valor'])
    self.df_fila_condiciones = pd.DataFrame()
    self.df = pd.DataFrame()
    self.df_bdd = CSV.cargar(self, 'bdd/', 'bdd')
    self.df_condiciones = CSV.cargar(self, 'csv/', 'condiciones')

    lista_dfs = ['DataFrame : df_lista_porcentajes', self.df_lista_porcentajes,
                 'DataFrame : df_pll', self.df_pll,
                 'DataFrame : df_bdd', self.df_bdd,
                 'DataFrame : df_tabla', self.df_tabla,
                 'DataFrame : df_valor', self.df_valor,
                 'DataFrame : df_fila_condiciones', self.df_fila_condiciones,
                 'DataFrame : df', self.df
                 ]
    Log.lista_dfs(self, lista_dfs)

    
    #Variables
    self.lista_relleno = ['plat-agosto.xls','HERSOL 7-9.xls']
    self.lista_nombres_columnas = ['Codigo','Nombre','Precio']
    self.carpeta_raiz = '/srcs/'
    self.carpeta_Planillas_a_cargar = self.carpeta_raiz + 'planillas_a_cargar/'
    self.carpeta = '/srcs/'
    self.nombre_archivo = ''
    self.extencion = '.csv'
    self.ruta_completa = self.carpeta_raiz + self.carpeta + self.nombre_archivo + self.extencion
    self.es_viejo = False
    self.xls = self.carpeta_Planillas_a_cargar + "*.xls"
    self.xlsx = self.xls + "x"
    self.rutas = [self.xls, self.xlsx]
    self.tipo_de_planilla = 'Bauen'
    self.condiciones_columnas = ''
    self.condiciones_rango = ''
    self.tabla_posicion = ''

    self.columnas = ['lista_relleno', 'lista_nombres_columnas', 'carpeta_raiz',
                 'carpeta_Planillas_a_cargar', 'carpeta', 'nombre_archivo',
                 'extencion', 'ruta_completa', 'es_viejo', 'xls', 'xlsx',
                 'rutas', 'tipo_de_planilla', 'condiciones_columnas',
                 'condiciones_rango', 'tabla_posicion'
                 ]
    self.fila = [self.lista_relleno, self.lista_nombres_columnas, self.carpeta_raiz,
                 self.carpeta_Planillas_a_cargar, self.carpeta, self.nombre_archivo,
                 self.extencion, self.ruta_completa, self.es_viejo, self.xls, self.xlsx,
                 self.rutas, self.tipo_de_planilla, self.condiciones_columnas,
                 self.condiciones_rango, self.tabla_posicion
                 ]
    Log.atributos(self)
    Log.pantalla(self)
  
  def actualizar_ruta_completa(self):
    ''' Cada instancia se carga con su ruta actualizada. De ser necesario invocar esta funcion '''
    self.columnas = ['Clase','Funcion','Desctipcion']
    self.fila = ['Estructura.','actualizar_ruta_completa()','Cada instancia se carga con su ruta actualizada. De ser necesario invocar esta funcion ']
    Log.clase(self)

    self.carpeta_raiz = '/srcs/'
    self.extencion = '.csv'
    self.ruta_completa = self.carpeta_raiz + self.carpeta + self.nombre_archivo + self.extencion
    self.columnas = ['carpeta_raiz', 'exrencion', 'ruta_completa', 'carpeta', 'nombre_archivo']
    self.fila = [self.carpeta_raiz, self.extencion, self.ruta_completa, self.carpeta, self.nombre_archivo]
    Log.atributos(self)
    lista_dfs = []
    Log.lista_dfs(self, lista_dfs)
    Log.pantalla(self)
    pass

class CSV(Estructura):
  def __init__(self):
    '''Gestiona los archivos de tipo .csv'''
    self.columnas = ['Clase','Funcion','Desctipcion']
    self.fila = ['CSV.','__init__()','Gestiona los archivos de tipo .csv']
    Log.clase(self)

    super().__init__()
    self.columnas = []
    self.fila = []
    Log.atributos(self)
    lista_dfs = []
    Log.lista_dfs(self, lista_dfs)
    Log.pantalla(self)
    pass

  def cargar(self, carpeta, nombre):
    '''Carga un nuevo csv ( carpeta='str', nombre='str' )'''
    self.columnas = ['Clase','Funcion','Desctipcion']
    self.fila = ['CSV.','cargar(self, carpeta, nombre)',"Carga un nuevo csv ( carpeta='str', nombre='str' )"]
    Log.clase(self)
    
    self.carpeta = carpeta
    self.nombre_archivo = nombre
    if self.django == False:
      Estructura.actualizar_ruta_completa(self)
      self.df = pd.read_csv(self.ruta_completa, sep=';')
    elif self.nombre_archivo == 'condiciones.csv':
      self.df = Condicionales.objects.all()
    
    
    self.columnas = ['carpeta', 'nombre_archivo']
    self.fila = [self.carpeta, self.nombre_archivo]
    Log.atributos(self)
    lista_dfs = ['DataFrame : df', self.df]
    Log.lista_dfs(self, lista_dfs)
    Log.pantalla(self)
    return self.df

  def guardar(self, carpeta, nombre, df):
    '''Guardar un nuevo csv ( carpeta='str', nombre='str' , df=pd.DataFrame)'''
    self.columnas = ['Clase','Funcion','Desctipcion']
    self.fila = ['CSV.','guardar(self, carpeta, nombre, df)',"Guardar un nuevo csv ( carpeta='str', nombre='str' , df=pd.DataFrame)"]
    Log.clase(self)

    self.carpeta = carpeta
    self.nombre_archivo = nombre
    if self.django == False:
      Estructura.actualizar_ruta_completa(self)
      self.df = df
      self.df.to_csv(self.ruta_completa, sep=';', index=False)
    elif self.nombre_archivo == 'condiciones.csv':
      self.df.to_sql(Condicionales.__meta.actualizador_condicionales, index=False)
      
      
    self.columnas = ['carpeta', 'nombre_archivo']
    self.fila = [self.carpeta, self.nombre_archivo]
    Log.atributos(self)
    lista_dfs = ['DataFrame : df', self.df]
    Log.lista_dfs(self, lista_dfs)
    Log.pantalla(self)
    pass

class PLL(Estructura):
  def __init__(self):
    '''Gestiona las planillas xls y xlsx'''
    self.columnas = ['Clase','Funcion','Desctipcion']
    self.fila = ['Estructura.','__init__()',"Gestiona las planillas xls y xlsx"]
    Log.clase(self)

    super().__init__()

    self.columnas = []
    self.fila = []
    Log.atributos(self)
    lista_dfs = []
    Log.lista_dfs(self, lista_dfs)
    Log.pantalla(self)
    pass

  def es_viejo(self, tipo_de_planilla, viejo_si_o_no):
    '''Chequeamos si la planilla es vieja'''
    self.columnas = ['Clase','Funcion','Desctipcion']
    self.fila = ['PLL.','es_viejo()',"Chequeamos si la planilla es vieja"]
    Log.clase(self)

    print(self.ruta.replace(self.carpeta_raiz,''))
    self.tipo_de_planilla = tipo_de_planilla
    condicion = True
    while condicion:
      pregunta = viejo_si_o_no
      if pregunta == 'si':
        self.es_viejo = True
        condicion = False
        #print('condicion: ',condicion)
      elif pregunta == 'no':
        self.es_viejo = False
        condicion = False
        #print('condicion: ',condicion)
      else:
        print('Valor fuera de rango!!')

    self.columnas = ['tipo_de_planilla', 'pregunta', 'es_viejo']
    self.fila = [self.tipo_de_planilla, pregunta, self.es_viejo]
    Log.atributos(self)
    lista_dfs = []
    Log.lista_dfs(self, lista_dfs)
    Log.pantalla(self)
    pass

  def condiciones(self):
    '''Carga el csv condiciones'''
    self.columnas = ['Clase','Funcion','Desctipcion']
    self.fila = ['PLL.','condiciones()',"Carga el csv condiciones"]
    Log.clase(self)

    self.df_condiciones = CSV.cargar(self, 'csv/', 'condiciones')
    #print('df_condiciones:\n', self.df_condiciones)
    es_tipo = self.df_condiciones.loc[:,'4'] == self.tipo_de_planilla
    #print('es_tipo: ', es_tipo)
    self.df_fila_condiciones = self.df_condiciones.loc[es_tipo]
    self.df_fila_condiciones = self.df_fila_condiciones.reset_index(drop=True)
    #print('df_fila_condiciones\n',self.df_fila_condiciones)
    self.condiciones_columnas = self.df_fila_condiciones.loc[0,'1']
    self.condiciones_rango = self.df_fila_condiciones.loc[0,'3']

    self.columnas = ['condiciones_columnas', 'condiciones_rango', 'es_tipo', 'tipo_de_planilla']
    self.fila = [self.condiciones_columnas, self.condiciones_rango, es_tipo, self.tipo_de_planilla]
    Log.atributos(self)
    lista_dfs = ['DataFrame : df_condiciones', self.df_condiciones]
    Log.lista_dfs(self, lista_dfs)
    Log.pantalla(self)
    pass

  def cargar_pll(self):
    '''Carga el pll'''
    self.columnas = ['Clase','Funcion','Desctipcion']
    self.fila = ['PLL.','cargar_pll()',"Carga el pll"]
    Log.clase(self)
    
    self.df_pll = pd.read_excel(self.ruta,  
                            header=None, 
                            usecols=self.condiciones_columnas, 
                            skiprows=[i for i in range(0,int(self.condiciones_rango))],
                            sheet_name=0)
    
    self.columnas = ['ruta', 'condiciones_columnas', 'condiciones_rango']
    self.fila = [self.ruta, self.condiciones_columnas, self.condiciones_rango]
    Log.atributos(self)
    lista_dfs = ['DataFrame : df_pll', self.df_pll]
    Log.lista_dfs(self, lista_dfs)
    Log.pantalla(self)
    pass

  def rellenar_codigo(self):
    '''Rellena con 0 la columna codigo si esta vacia o no existe'''
    self.columnas = ['Clase','Funcion','Desctipcion']
    self.fila = ['PLL.','rellenar_codigo()',"Rellena con 0 la columna codigo si esta vacia o no existe"]
    Log.clase(self)
    
    if self.ruta in self.lista_relleno:
            self.df_pll.insert(0,'zero',0,allow_duplicates=True)
    
    self.columnas = ['ruta', 'lista_relleno']
    self.fila = [self.ruta, self.lista_relleno]
    Log.atributos(self)
    lista_dfs = ['DataFrame : df_pll', self.df_pll]
    Log.lista_dfs(self, lista_dfs)
    Log.pantalla(self)
    pass

  def ordenar_segun_tabla(self):
    '''CARGAR Y ORDENAR LAS COLUMNAS 0,1,2'''
    self.columnas = ['Clase','Funcion','Desctipcion']
    self.fila = ['PLL.','ordenar_segun_tabla()',"CARGAR Y ORDENAR LAS COLUMNAS 0,1,2"]
    Log.clase(self)

    self.columnas = ['condiciones_nombre', 'tabla_posicion', 'fila_condiciones']
    self.fila = ['undefined', 'undefined', 'undefined']
    Log.atributos(self)
    lista_dfs = ['DataFrame : df_fila_condiciones', self.df_fila_condiciones,
                 'DataFrame : df_pll', self.df_pll
                 ]
    Log.lista_dfs(self, lista_dfs)
    Log.pantalla(self)
    #-------------------------------------------------------------------------#
    self.df_fila_condiciones = self.df_fila_condiciones.reset_index(drop=True)
    #print('DataFrame : df_fila_condiciones',self.df_fila_condiciones)
    self.condiciones_nombre = self.df_fila_condiciones.loc[0,'5'] 
    self.tabla_posicion = self.df_tabla[self.condiciones_nombre].tolist()
    self.df_pll.columns = self.tabla_posicion
    self.df_pll = self.df_pll[self.df_tabla['0,1,2']]
    self.df_pll = self.df_pll.dropna()
    
    self.df_pll['Relacional'] = '_'
    self.df_pll['Porcentaje'] = 0.0
    self.df_pll['Trabajado'] = 0
    self.df_pll['Stock'] = 0
    self.df_pll['Proveedores'] = self.df_fila_condiciones.loc[0,'4']
    self.df_pll['Calidad'] = '_'
    self.df_pll['Imagen'] = '_'
    if self.es_viejo == True:
      self.df_pll['Fecha'] = input('0000-12-30 \n')
      self.df_pll['Actualizado'] = 0
    else:
      self.df_pll['Fecha'] = input('0000-12-30 \n')
      self.df_pll['Actualizado'] = 1
    #-------------------------------------------------------------------------#
    self.columnas = ['condiciones_nombre', 'tabla_posicion']
    self.fila = [self.condiciones_nombre, self.tabla_posicion]
    Log.atributos(self)
    lista_dfs = ['DataFrame : df_fila_condiciones', self.df_fila_condiciones,
                 'DataFrame : df_pll', self.df_pll
                 ]
    Log.lista_dfs(self, lista_dfs)
    Log.pantalla(self)
    pass
  
  def feed_back(self):
    '''FEED BACK'''
    self.columnas = ['Clase','Funcion','Desctipcion']
    self.fila = ['PLL.','feed_back()',"FEED BACK"]
    Log.clase(self)
    
    ##################################################################################################################

    if len(self.df_pll) > 0:
        print('Cargar_nuevo_archivo ------------------------------------- Completado')
        print('Filas cargadas: ------------------------------------------',len(self.df_pll))
        print('Formato: ------------------------------------------------------------')
        print('')
    else:
        print('ruta --------------------------------------------------fallo la carga')
    self.cod = self.df_fila_condiciones.loc[0,'6']
    #   CREAMOS ID Y REORDENAMOS
    self.df_pll['Codigo'] = self.df_pll['Codigo'].astype(str)
    self.df_pll['id'] = self.df_pll['Codigo'] + self.cod
    self.df_pll = self.df_pll[['id', 'Codigo', 'Relacional', 'Nombre', 'Precio', 'Porcentaje',
      'Trabajado', 'Actualizado', 'Fecha', 'Stock', 'Proveedores', 'Calidad', 'Imagen']] 

    self.columnas = ['cod']
    self.fila = [self.cod]
    Log.atributos(self)  
    lista_dfs = ['DataFrame : df_pll', self.df_pll]
    Log.lista_dfs(self, lista_dfs)
    Log.pantalla(self)
    pass
    
class BDD(Estructura):
  def __init__(self):
    '''Controla la base de datos'''
    self.columnas = ['Clase','Funcion','Desctipcion']
    self.fila = ['BDD.','__init__()',"Controla la base de datos"]
    Log.clase(self)

    super().__init__()
    self.nombre_archivo = ''
    Estructura.actualizar_ruta_completa(self)
    self.resultado = pd.DataFrame()
    self.mascara = 'bool_df'

    self.columnas = ['nombre_archivo', 'mascara']
    self.fila = [self.nombre_archivo, self.mascara]
    Log.atributos(self)
    lista_dfs = ['DataFrame : resultado', self.resultado]
    Log.lista_dfs(self, lista_dfs)
    Log.pantalla(self)
    pass

  def cargar_pll(self):
    '''Agrega un nuevo pll procesado al bdd'''
    self.columnas = ['Clase','Funcion','Desctipcion']
    self.fila = ['BDD.','cargar_pll()',"Agrega un nuevo pll procesado al bdd"]
    Log.clase(self)

    if self.es_viejo == False:
      self.df_bdd = self.df_bdd.append(self.df_pll, ignore_index=True)
      lista_dfs = ['DataFrame : df_bdd', self.df_bdd]
    else:
      self.df_bdd = self.df_bdd.append(self.df_items_desactualizados, ignore_index=True)
      lista_dfs = ['DataFrame : df_bdd', self.df_bdd, 'DataFrame : df_items_desactualizados', self.df_items_desactualizados]
    self.columnas = ['es_viejo']
    self.fila = [self.es_viejo]
    Log.atributos(self)
    #
    Log.lista_dfs(self, lista_dfs)
    Log.pantalla(self)
    pass
  
  def agregar(self):
    '''Agrega un item nuevo a la base de datos'''
    self.columnas = ['Clase','Funcion','Desctipcion']
    self.fila = ['BDD.','agregar()',"Agrega un item nuevo a la base de datos"]
    Log.clase(self)

    if len(self.df_bdd) <= 0:
        self.df_bdd = self.df_pll
    else:
        self.df_bdd = self.bdd.append(self.df_pll,ignore_index=True)

    self.columnas = ['len(df_dbb)']
    self.fila = [len(self.df_bdd)]
    Log.atributos(self)
    lista_dfs = ['DataFrame : df_bdd', self.df_bdd]
    Log.lista_dfs(self, lista_dfs)
    Log.pantalla(self)
    pass

  def borrar(self):
    '''Borra un item de la base de datos'''
    self.columnas = ['Clase','Funcion','Desctipcion']
    self.fila = ['BDD.','agregar()',"Borra un item de la base de datos"]
    Log.clase(self)

    self.mascara = self.df_bdd[ self.df_bdd['id'] == self.resultado['id'].values ].index
    self.df_bdd = self.df_bdd.drop(self.mascara , inplace=True)

    self.columnas = []
    self.fila = []
    Log.atributos(self)
    lista_dfs = ['DataFrame : resultado', self.resultado,
                 'DataFrame : mascara',self.mascara,
                 'DataFrame : df_bdd', self.df_bdd]
    Log.lista_dfs(self, lista_dfs)
    Log.pantalla(self)
    pass

  def modificar(self):
    '''Modifica un item de la base de datos'''
    self.columnas = ['Clase','Funcion','Desctipcion']
    self.fila = ['BDD.','modificar()',"Modifica un item de la base de datos"]
    Log.clase(self)

    #vacio

    self.columnas = []
    self.fila = []
    Log.atributos(self)
    lista_dfs = []
    Log.lista_dfs(self, lista_dfs)
    Log.pantalla(self)
    pass

  def consultar(self):
    '''Para realizar una busqueda'''
    self.columnas = ['Clase','Funcion','Desctipcion']
    self.fila = ['BDD.','modificar()',"Modifica un item de la base de datos"]
    Log.clase(self)

    self.busqueda = input('Buscar por ID:\n')
    self.resultado = self.df_bdd
    #display(self.df_bdd)
    self.resultado = self.resultado[self.resultado['id'].str.contains(self.busqueda.strip(), case=False)].drop_duplicates()
    #display(self.resultado[['id','Nombre','Precio','Stock','Actualizado', 'Fecha']])

    


    self.columnas = ['busqueda']
    self.fila = [self.busqueda]
    Log.atributos(self)
    lista_dfs = ['DataFrame : busqueda',self.busqueda,
                 'DataFrame : resultado', self.resultado,
                 'DataFrame : df_bdd', self.df_bdd,
                 ]
    Log.lista_dfs(self, lista_dfs)
    Log.pantalla(self)
    pass

class DEUS_EX(Estructura):
  def __init__(self):
    super().__init__()
    '''Detras de camaras'''
    self.columnas = ['Clase','Funcion','Desctipcion']
    self.fila = ['DEUS_EX.','__init__()',"Detras de camaras"]
    Log.clase(self)

    #vacio

    self.columnas = []
    self.fila = []
    Log.atributos(self)
    lista_dfs = []
    Log.lista_dfs(self, lista_dfs)
    Log.pantalla(self)
    pass

  def primera_carga(self):
    '''Secuencia de acciones'''
    self.columnas = ['Clase','Funcion','Desctipcion']
    self.fila = ['DEUS_EX.','primera_carga()',"secuencia de acciones"]
    Log.clase(self)
    
    #Vacio

    self.columnas = []
    self.fila = []
    Log.atributos(self)
    lista_dfs = []
    Log.lista_dfs(self, lista_dfs)
    Log.pantalla(self)
    pass

  def carga_por_lotes(self, tipo_de_planilla, viejo_si_o_no):
    '''Cargamos los xls y xlsx por lotes en la carpeta planillas_a_cargar'''
    self.columnas = ['Clase','Funcion','Desctipcion']
    self.fila = ['DEUS_EX.','carga_por_lotes()',"Cargamos los xls y xlsx por lotes en la carpeta planillas_a_cargar"]
    Log.clase(self)
    #Log.log(self,'Cargamos los xls y xlsx por lotes en la carpeta planillas_a_cargar')
    CSV.cargar(self, 'csv/', 'condiciones')
    for x in self.rutas:
      '''Una por xls y otra por xlsx'''
      for f in glob.glob(x):
        '''Por cada ruta de cada archivo encontrado segun la extencion'''
        self.ruta = f
        
        PLL.es_viejo(self, tipo_de_planilla, viejo_si_o_no)
        PLL.condiciones(self)
        PLL.cargar_pll(self)
        PLL.rellenar_codigo(self)
        PLL.ordenar_segun_tabla(self)
        PLL.feed_back(self)

        self.df_pll = self.df_pll.reset_index(drop=True)
        print('len: ',len(self.df_pll),'\n',self.df_pll)
        ########################################################################
        self.df_bdd = self.df_bdd.append(self.df_pll)
        self.df_bdd = self.df_bdd.drop_duplicates()
        CSV.guardar(self,'bdd/', 'bdd', self.df_bdd)
        print('len df_bdd: ',len(self.df_bdd),'\nSe guardo con exito!!!')

        cont = 0
        if self.es_viejo == False:
          '''Crea una lista df_valor aleatorea y la usa para crear las columnas
          id y nuevo en df_lista_de_porcentajes'''
          for i in range(int(len(self.df_pll)*0.1)):
            '''Rellenar el df_valor[Valor] que contiene una lista de index aleatorios'''
            aleatorio = random.randint(0, len(self.df_pll))
            if aleatorio in self.df_valor['Valor'].values:
              i = i-1
            else:
              self.df_valor.loc[i,'Valor'] = aleatorio
          
          for valor in self.df_valor['Valor'].values:
            '''Rellena la lista de porcentajes con los items que coinciden en pll y lista df_valor[valor]'''
            #Log.log(self, 'valor: \n')
            self.df_lista_porcentajes.loc[cont,'Nuevo'] = self.df_pll.loc[valor,'Precio']
            self.df_lista_porcentajes.loc[cont,'id'] = self.df_pll.loc[valor,'id']
            self.df_lista_porcentajes.loc[cont,'Anterior'] = 0
            cont = cont+1
          CSV.guardar(self,'csv/', 'lista_porcentajes_'+self.tipo_de_planilla, self.df_lista_porcentajes)
          
          print('Creando un una nueva lista_porcentajes: \n', self.df_lista_porcentajes)

        else:
          'Si es viejo:'
          'Cargar df correspondiente'
          self.df_lista_porcentajes = CSV.cargar(self, 'csv/', 'lista_porcentajes_'+self.tipo_de_planilla)
          
          'Display df corespondiente'
          #display(self.df_lista_porcentajes)
          print('Aca esta el quilombo??')
          print('len: \n',len(self.df_lista_porcentajes))
          self.df_aux = self.df_pll[self.df_pll['id'].isin(self.df_lista_porcentajes['id'])]#################################
          self.df_aux = self.df_aux[['id','Precio']]
          print('ID y tambien PRECIO ??: \n')
          #display(self.df_aux)

          #self.df_lista_porcentajes = self.df_lista_porcentajes[self.df_lista_porcentajes.id.isin(self.df_aux.id)]
          #self.df_lista_porcentajes = self.df_lista_porcentajes.reset_index(drop=True)
          #self.df_aux = self.df_aux.reset_index(drop=True)
          #print('len_lista_porcentajes :',len(self.df_lista_porcentajes),'\nlen_aux: ',len(self.df_aux))

          #display(self.df_lista_porcentajes)
          #display(self.df_aux)
          
          
          'Rellena la lista ANTERIOR'
          self.df_aux = self.df_aux.loc[self.df_aux.id.isin(self.df_lista_porcentajes.id)]
          self.df_lista_porcentajes = self.df_lista_porcentajes.loc[self.df_lista_porcentajes.id.isin(self.df_aux.id)]
          self.df_lista_porcentajes = self.df_lista_porcentajes.sort_values('id')
          self.df_aux = self.df_aux.sort_values('id')
          self.df_lista_porcentajes = self.df_lista_porcentajes.reset_index(drop=True)
          self.df_aux = self.df_aux.reset_index(drop=True)
          self.df_lista_porcentajes['Anterior'] = self.df_aux['Precio']
          print('------------ESTEEEEEEEEEEEEEEEEE---------------')
          #display(self.df_lista_porcentajes)

        if self.df_lista_porcentajes['Anterior'].mean() != 0:
          '''Si hay items, sacamos el promedio'''
          #self.df_aux = self.df_pll[self.df_pll['id'].isin(self.df_lista_porcentajes['id'])]
          #print(len(self.df_aux))
          #display(self.df_aux)
          #print(len(self.df_lista_porcentajes))
          #isplay(self.df_lista_porcentajes)
          #print(len(self.df_lista_porcentajes[self.df_lista_porcentajes['id'].isin(self.df_aux['id'])]))
          #display(self.df_lista_porcentajes[self.df_lista_porcentajes['id'].isin(self.df_aux['id'])])
          #self.df_lista_porcentajes = self.df_lista_porcentajes[self.df_lista_porcentajes['id'].isin(self.df_aux['id'])] 
          #self.df_lista_porcentajes['Anterior'] = self.df_aux['Precio'].values
          self.df_lista_porcentajes['Nuevo'] = self.df_lista_porcentajes['Nuevo'].astype(float)
          self.df_lista_porcentajes['Anterior'] = self.df_lista_porcentajes['Anterior'].astype(float)
          self.df_lista_porcentajes = self.df_lista_porcentajes.dropna()
          self.df_lista_porcentajes['Aumento'] = self.df_lista_porcentajes['Nuevo']/self.df_lista_porcentajes['Anterior']
          self.aumento_promedio = self.df_lista_porcentajes['Aumento'].mean()

          ''' Se actualiza el atributo df_items_desactualizados'''
          self.df_items_desactualizados = self.df_pll[~self.df_pll['id'].isin(self.df_bdd['id'])]####################################
          print('self.df_items_desactualizados: \n',self.df_items_desactualizados)
          self.df_items_desactualizados['Precio'] = self.df_items_desactualizados['Precio'] * self.aumento_promedio

          #Log.log(self, 'items desactualizado: \n')
          print('--------------DESACTUALIZADOS------------')
          #display(self.df_items_desactualizados)
        # si es_viejo == False --> append df_pll
        # si es_viejo == True  --> append df_items_desactualizados
        BDD.cargar_pll(self)

        #######################################################################################################
        self.df_bdd = self.df_bdd.append(self.df_pll)
        self.df_bdd = self.df_bdd.drop_duplicates()
        CSV.guardar(self,'bdd/', 'bdd', self.df_bdd)
        self.df_bdd = CSV.cargar(self, 'bdd/', 'bdd')
    
    
    print('---CERRAR PROGRAMA---')
    self.columnas = []
    self.fila = []
    Log.atributos(self)
    lista_dfs = ['DataFrame : df_lista_porcentajes',self.df_lista_porcentajes,
                 'DataFrame : df_items_desactualizados', self.df_items_desactualizados,
                 'DataFrame : df_aux', self.df_aux,
                 'DataFrame : df_pll', self.df_pll,
                 'DataFrame : df_bdd', self.df_bdd,
                 ]
    Log.lista_dfs(self, lista_dfs)
    Log.pantalla(self)
    
  # completo = pll
  # tipo de planilla = pll.tipo_de_planilla
  # es nuevo = pll.es_viejo

  def consultas(self):
    ''''''
    self.columnas = ['Clase','Funcion','Desctipcion']
    self.fila = ['DEUS_EX.','consultas()',""]
    Log.clase(self)
    #Log.limpiar_log()
    BDD.consultar(self)
    lista_dfs = []
    Log.lista_dfs(self, lista_dfs)
    Log.pantalla(self)
    pass
    
def main(tipo_de_planilla, viejo_si_o_no):
    deus_ex = DEUS_EX()
    #Log.limpiar_log()
    print('-Numero de items cargados:')
    print(len(deus_ex.df_bdd))
    deus_ex.df_bdd = deus_ex.df_bdd.reset_index(drop=True)
    #display(deus_ex.df_bdd.head())
    print('')
    print('Seleccionar tipo de acciones: \n ')
    print('  Cargar_planillas = cp\n  Consultar_por_id = cid')
    print('')
    time.sleep(2)
    pantalla = 'cñ'
    if pantalla == 'cp':
      deus_ex.primera_carga()
      #print(deus_ex.carpeta_raiz)
      #print(deus_ex.carpeta_Planillas_a_cargar)
      #print(deus_ex.xls)
      #print(deus_ex.xlsx)
      #print(deus_ex.rutas)
      #print(deus_ex.df_tabla['0,1,2'])
      #print(deus_ex.ruta_completa)
      deus_ex.carga_por_lotes(tipo_de_planilla, viejo_si_o_no)
    elif pantalla == 'cid':
      bucle = True
      while bucle:
        deus_ex.consultas()
    pass
    
if __name__ == '__main__':
    main()