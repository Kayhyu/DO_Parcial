use kaggle
go

--- crear tabla
if not exists(select * from sys.tables where object_id=object_id(N'dbo.starbucks') and type='U')
create table dbo.starbucks(
				baverage_categ varchar(50),
				beverage varchar (100),
				beverage_pre varchar(50),
				calories decimal(6,3),
				total_fat_g varchar(10),
				trans_fat_g decimal(6,3),
				saturated_fat_g decimal (6,3),
				sodium_mg decimal(6,3),
				total_carbohydrates_g decimal (6,3),
	|			cholesterol_mg decimal(6,3),
				dietary_fibre_g decimal(6,3),
				sugars_g decimal (6,3),
				protein_g decimal (6,3),
				vitamin_a_pct varchar(10),
				vitamin_c_pct varchar(10),
				calcium_pct varchar(10),
				iron_pct varchar(10),
				caffeine_mg varchar(10)
)

--- si y existe  la tabla starbusk la limpi
truncate table dbo.starbuck;
go

--- importar data desde archivo
bulk insert dbo.starbucks
from 'D:\Ejercicios_de_python\PROYECTO_PARCIAL\dataset\starbucks.csv'
with
(
	FIRSTROW=2, -- empieza en la 2fila, ya que la primera es la cabecera
	FIELDTERMINATOR=',' , --indicamos separador de clumnas
	ROWTERMINATOR='0x0a' -- hace referencia a un salto de linea
)
GO
