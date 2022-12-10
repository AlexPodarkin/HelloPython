import html_creater as hc
import xml_generator as xg  # импорт XML часто используют в ключе клиент сервер
import data_provider as dp

# print(hc.create())
# print(xg.create()) # запуск XML

hc.new_create(xg.new_create(dp.data_collection()))