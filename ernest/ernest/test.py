import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
print(BASE_DIR)

STATIC_ROOT = os.path.join(os.path.dirname(__file__),'static')
print(STATIC_ROOT)

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
print(MEDIA_ROOT)

tem = os.path.join(BASE_DIR, 'template')
print(tem)

print('MEDIA_ROOT is ', os.path.join(BASE_DIR, 'media'))
print('STATIC_ROOT is ', os.path.join(os.path.dirname(__file__),'static'))