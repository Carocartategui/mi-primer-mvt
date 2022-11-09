from PrimerApp.models import Familiar, Amigos

Familiar(nombre="Paula", direccion="Maipu 156", numero_pasaporte=95623).save()
Familiar(nombre="Javier", direccion="Maipu 156", numero_pasaporte=563114).save()
Familiar(nombre="Silvia", direccion="Maipu 156", numero_pasaporte=75423).save()
Familiar(nombre="Sebastian", direccion="Congreso 1123", numero_pasaporte=35428).save()

print("Se cargo con exito los usuarios de pruebas")

Amigos(nombre="Victoria", apellido="Aguirre", anios_de_amistad=12).save()
Amigos(nombre="Marcos", apellido="Franco", anios_de_amistad=15).save()



print("Se cargo con éxito los usuarios de pruebas")