##tipe data standar

#tipe data : Angka (integer)
data_integer = 10
print ("data : ", data_integer)
print ("tipe data : ", type(data_integer))

#tipe data : Angka dengan koma (float)
data_float = 5.5
print ("data : ", data_float)
print ("tipe data : ", type(data_float))

#tipe data : kumpulan char (string)
data_string = "ini adalah string"
print ("data : ", data_string)
print ("tipe data : ", type(data_string))

#tipe data : biner True/False (boolean)
data_bool = True
print ("data : ", data_bool)
print ("tipe data : ", type(data_bool))

##tipe data khusus
#tipe data : bilangan kompleks
data_complex = complex(5,6)
print ("data : ", data_complex)
print ("tipe data : ", type(data_complex))

#tipe data : import dari bahasa C
from ctypes import c_double
data_c_double = c_double(10.5)
print ("data : ", data_c_double)
print ("tipe data : ", type(data_c_double))