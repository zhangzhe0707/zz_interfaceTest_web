"""
Django settings for ZZ_InterfaceTest_web project.

Generated by 'django-admin startproject' using Django 2.2.1.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

RESPORTS_DIR_PATH = os.path.join(BASE_DIR, 'reports')

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'y#02$kmsv%q3+7k@m4g1v-&=296dl7j61v+3gg5*wvext9c!2o'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

# Application definition

INSTALLED_APPS = [
    'simpleui',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'WebServer',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'ZZ_InterfaceTest_web.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'ZZ_InterfaceTest_web.wsgi.application'

# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'zh-hans'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = '/static/'
TEMPLATES_DIR = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'WebServer/templates').replace('\\', '/'),
        ],
    }
]

STATIC_ROOT = os.path.join(BASE_DIR, 'static')


BASE_LOG_DIR = os.path.join(BASE_DIR, "log")
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'standard': {
            'format': '[%(asctime)s][%(threadName)s:%(thread)d][task_id:%(name)s][%(filename)s:%(lineno)d]'
                      '[%(levelname)s][%(message)s]'
        },
        'simple': {
            'format': '[%(levelname)s][%(asctime)s][%(filename)s:%(lineno)d]%(message)s'
        },
        'collect': {
            'format': '%(message)s'
        }
    },
    'filters': {
        'require_debug_true': {
            '()': 'django.utils.log.RequireDebugTrue',
        },
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'filters': ['require_debug_true'],  # 只有在Django debug为True时才在屏幕打印日志
            'class': 'logging.StreamHandler',
            'formatter': 'simple'
        },
        'SF': {
            'level': 'INFO',
            'class': 'logging.handlers.RotatingFileHandler',  # 保存到文件，根据文件大小自动切换
            'filename': os.path.join(BASE_LOG_DIR, "InterfaceTest_info.log"),  # 日志文件
            'maxBytes': 1024 * 1024 * 50,  # 日志大小 50M
            'backupCount': 3,  # 备份数为3  xx.log --> xx.log.1 --> xx.log.2 --> xx.log.3
            'formatter': 'standard',
            'encoding': 'utf-8',
        },
        'TF': {
            'level': 'INFO',
            # 保存到文件，根据时间自动切换
            'class': 'logging.handlers.TimedRotatingFileHandler',
            # 日志文件
            'filename': os.path.join(BASE_LOG_DIR, "InterfaceTest_info.log"),
            # 备份数为3  xx.log --> xx.log.2018-08-23_00-00-00 --> xx.log.2018-08-24_00-00-00 --> ...
            'backupCount': 3,
            # 每天一切，可选值有S/秒 M/分 H/小时 D/天 W0-W6/周(0=周一) midnight/如果没指定时间就默认在午夜
            'when': 'D',
            'formatter': 'standard',
            'encoding': 'utf-8',
        },
        'error': {
            'level': 'ERROR',
            'class': 'logging.handlers.RotatingFileHandler',  # 保存到文件，自动切换
            'filename': os.path.join(BASE_LOG_DIR, "InterfaceTest_err.log"),  # 日志文件
            # 日志大小50M
            'maxBytes': 1024 * 1024 * 5,
            'backupCount': 5,
            'formatter': 'standard',
            'encoding': 'utf-8',
        },
        'collect': {
            'level': 'INFO',
            'class': 'logging.handlers.RotatingFileHandler',  # 保存到文件，自动切换
            'filename': os.path.join(BASE_LOG_DIR, "InterfaceTest_collect.log"),
            # 日志大小50M
            'maxBytes': 1024 * 1024 * 50,
            'backupCount': 5,
            'formatter': 'collect',
            'encoding': "utf-8"
        }
    },
    'loggers': {
        '': {
            # 默认的logger应用如下配置
            'handlers': ['SF', 'console', 'error'],  # 上线之后可以把'console'移除
            'level': 'DEBUG',
            'propagate': True,
        },
        'collect': {
            # 名为'collect'的logger还单独处理
            'handlers': ['console', 'collect'],
            'level': 'INFO',
        }
    },
}
