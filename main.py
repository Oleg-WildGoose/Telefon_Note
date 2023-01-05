import user_interface as ui
import generator as gen
import logger as lg
import crud

crud.init_data_base('base_phone.csv')
lg.logging.info('Start')
ui.ls_menu()

 