# -*- coding: utf-8 -*-
import logging

FORMAT = u'[%(asctime)s] %(name)-8s %(levelname)-8s %(filename)s[LINE:%(lineno)d] %(message)s'
# Запись логов в файл
logging.basicConfig(format = FORMAT, filename = u'logfile.log')
# Отображать только логи klika-tech
logging.Filter(name = 'klika-tech')

# Создать лог autotest
log = logging.getLogger('klika-tech')
log.setLevel(logging.DEBUG)
#log.setLevel(logging.INFO)
#log.setLevel(logging.WARNING)
#log.setLevel(logging.ERROR)
#logging.disable(logging.NOTSET)
# log.debug("DEBUG 10")
# log.info("INFO 20")
# log.warning("WARNING 30")
# log.error("ERROR 40")
# log.critical("CRITICAL 50")
