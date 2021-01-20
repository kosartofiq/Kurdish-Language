from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver

from global_functions import is_same
from .models import Language, LanguageHistory, Dialect, DialectHistory


@receiver(post_save, sender=Language)
def create_language_history(instance, created):
    # if new object created then make history
    if created:
        # create history
        LanguageHistory.objects.create(
            editor=instance.creator,
            language=instance,
            name=instance.name,
            native_name=instance.native_name,
            iso_639_1=instance.iso_639_1,
            iso_639_2=instance.iso_639_2,
            description=instance.description
        )
        # create sub object
        Dialect.objects.create(
            language=instance,
            creator=instance.creator,
            super_dialect=None,
            name='Standard',
            native_name='Standard',
            description=instance.description
        )


@receiver(pre_save, sender=Language)
def update_language_history(instance):
    # check if any change happen or only clicked save without change, to not make history
    # get object if is not first time creation
    old_record = Language.objects.filter(pk=instance.pk).first()

    # if exist , it means we create history for updated changes
    # we will create history only in update
    if old_record:
        # check for similarity
        if is_same(old_record, instance):
            # it means just clicked save without modification, so pass signal and do nothing
            pass
        else:
            # create history
            LanguageHistory.objects.create(
                editor=instance.creator,
                language=instance,
                name=instance.name,
                native_name=instance.native_name,
                iso_639_1=instance.iso_639_1,
                iso_639_2=instance.iso_639_2,
                description=instance.description
            )


@receiver(post_save, sender=Dialect)
def create_dialect_history(instance, created):
    # if new object created then make history
    if created:
        # create history
        DialectHistory.objects.create(
            editor=instance.creator,
            language=instance.language,
            dialect=instance,
            super_dialect=instance.super_dialect,
            name=instance.name,
            native_name=instance.native_name,
            description=instance.description
        )


@receiver(pre_save, sender=Dialect)
def update_dialect_history(instance):
    # check if any change happen or only clicked save without change, to not make history
    # get object if is not first time creation
    old_record = Dialect.objects.filter(pk=instance.pk).first()

    # if exist , it means we create history for updated changes
    # we will create history only in update
    if old_record:
        # check for similarity
        if old_record.is_same(instance):
            # it means just clicked save without modification, so pass signal and do nothing
            pass
        else:
            # create history
            DialectHistory.objects.create(
                editor=instance.creator,
                language=instance.language,
                dialect=instance,
                super_dialect=instance.super_dialect,
                name=instance.name,
                native_name=instance.native_name,
                description=instance.description
            )
