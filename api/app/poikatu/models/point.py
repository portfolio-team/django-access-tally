from django.db import models


def get_deleted_point():
    return Point.objects.get_or_create(name="deleted_point")[0]

class Point(models.Model):

    """"
    User's point
    """

    # Amount points
    amount_points = models.IntegerField(default=0)

    # Who?
    user = models.ForeignKey(
        'User',
        related_name='point',
        on_delete=models.CASCADE,
    )

    # POINT_TYPE_FREE = 1
    # POINT_TYPE_PAID = 2
    # POINT_TYPES = (
    #     (POINT_TYPE_FREE, 'free points'),
    #     (POINT_TYPE_PAID, 'paid points'),
    # )

    # # Free or Paid points
    # point_type = models.IntegerField(choices=POINT_TYPES,
    #                             verbose_name='POINT TYPE',
    #                             default=POINT_TYPE_FREE)

    # # Expiry date of this point (In case of paid points, null)
    # expired = models.DateTimeField(null=True,)

    class Meta:
        default_permissions = ()
        # constraints = [
        #     models.UniqueConstraint(fields=['user', 'point_type'], name='points_unique')
        # ]


class ChargedPointLog(models.Model):

    """"
    point が取得された時のlogを保存するためのmodel
    """

    # how to get user's point. (ex) 'user_click' | 'user_paid' | 'batch'
    charged_method = models.CharField(max_length=64, null=True, blank=True)

    # When?
    created = models.DateTimeField()

    # who?
    user = models.ForeignKey(
        'User',
        related_name='charged_point_log',
        on_delete=models.SET(get_deleted_point),
    )

    # Number of charged points
    charged_points = models.IntegerField()

    # # Amount paid for points (free points = 0)
    # amount_paid = models.IntegerField(default=0)

    class Meta:
        default_permissions = ()
        indexes = [
            models.Index(fields=['created'])
        ]


# class UsedPointLog(models.Model):

#     # What used points for? (ex) 'game' | 'option'
#     used_target = models.CharField(max_length=64, null=True, blank=True)

#     # When?
#     created = models.DateTimeField()

#     # who?
#     user = models.ForeignKey(
#         'app.User',
#         related_name='used_point_log',
#         on_delete=models.SET(get_deleted_point),
#     )

#     # Number of used points
#     used_points = models.IntegerField()

#     class Meta:
#         default_permissions = ()
#         permissions = (
#             ("view_pointLog", "Can view used point log"),
#         )
#         indexes = [
#             models.Index(fields=['created'])
#         ]
