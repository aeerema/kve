from django.core.management.base import BaseCommand
from django.db.utils import IntegrityError
from tqdm import tqdm

from databank.models.family import Family
from databank.models.genus import Genus
from databank.models.language import Language


def fill_families():
    with open("databank/management/csvs/families.csv", "r", encoding="utf-8") as f:
        for line in tqdm(f):
            try:
                Family.objects.create(name=line.strip())
            except IntegrityError:
                pass
def fill_genuses():
    with open("databank/management/csvs/genuses.csv", "r", encoding="utf-8") as f:
        for line in tqdm(f):
            try:
                Genus.objects.create(name=line.strip())
            except IntegrityError:
                pass
def fill_languages():
    with open("databank/management/csvs/languages.csv", "r", encoding="utf-8") as f:
        for line in tqdm(f):
            code, name, genus, family = line.strip().split(",")
            try:
                Language.objects.create(code=code,
                                      name=name, 
                                      genus=Genus.objects.get(name=genus),
                                      family=Family.objects.get(name=family))
            except IntegrityError:
                pass


class Command(BaseCommand):
    help = 'Fill database'

    def add_arguments(self, parser):
        parser.add_argument('--family', action='store_true')
        parser.add_argument('--genus', action='store_true')
        parser.add_argument('--language', action='store_true')
    
    def handle(self, *args, **options):
        if options["family"]: fill_families()
        if options["genus"]: fill_genuses()
        if options["language"]: fill_languages()