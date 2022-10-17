from PrimerApp.models import Familiar

Familiar(nombre="Paula", direccion="Maipu 156", numero_pasaporte=95623).save()
Familiar(nombre="Javier", direccion="Maipu 156", numero_pasaporte=563114).save()
Familiar(nombre="Silvia", direccion="Maipu 156", numero_pasaporte=75423).save()
Familiar(nombre="Sebastian", direccion="Congreso 1123", numero_pasaporte=35428).save()

print("Se cargo con exito los usuarios de pruebas")