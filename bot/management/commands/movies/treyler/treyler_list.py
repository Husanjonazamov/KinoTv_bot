from treyler.models import Treyler



def get_treyler_all():
  return list(Treyler.objects.all())