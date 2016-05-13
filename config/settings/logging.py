LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        # 输出日志级别、日志消息，以及时间、进程、线程和生成日志消息的模块。
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s'
        },
        # simple 只输出日志的级别（例如，DEBUG）和日志消息。
        'simple': {
            'format': '%(levelname)s %(message)s'
        },
    },
    'handlers': {
        # 传递DEBUG（和更高级）的消息给/dev/null。
        'null': {
            'level': 'DEBUG',
            'class': 'logging.NullHandler',
        },
        # 将打印DEBUG（和更高级）的消息到stderr。这个handler 使用simple 输出格式。
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'simple'
        },
        # 用邮件发送ERROR（和更高级）的消息到站点管理员。
        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler',
        }
    },
    'loggers': {
        'django': {
            'handlers': ['null'],
            'propagate': True,
            'level': 'INFO',
        },
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': False,
        },
        'myproject.custom': {
            'handlers': ['console', 'mail_admins'],
            'level': 'INFO',
        }
    }
}