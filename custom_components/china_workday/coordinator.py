import datetime
import json
import logging
import os

from homeassistant.helpers.update_coordinator import DataUpdateCoordinator, UpdateFailed

_LOGGER = logging.getLogger(__name__)

class ChinaWorkdayCoordinator(DataUpdateCoordinator):

    def __init__(self, hass):
        super().__init__(
            hass,
            _LOGGER,
            name="ChinaWorkday Coordinator",
            update_interval=datetime.timedelta(minutes=1)
        )
        self._hass = hass

    async def _async_update_data(self):
        now = datetime.datetime.now()

        holidays = await self.hass.async_add_executor_job(self._load_datasource_from_file, str(now.year))
        if holidays is None:
            raise UpdateFailed('数据源不可用')

        date_key = now.strftime('%Y-%m-%d')
        if date_key in holidays:
            holiday = holidays[date_key]
            return {
                'workday': not holiday['isOffDay'],
                'holiday': holiday['name']
            }

        return {
            'workday': now.weekday() not in [5, 6],
            'holiday': '',
        }

    @staticmethod
    def _load_datasource_from_file(year):
        file_path = os.path.join(os.path.dirname(__file__), f"data/{year}.json")

        if not os.path.isfile(file_path):
            _LOGGER.error("未找到数据源文件: %s", file_path)
            return None

        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                data = json.load(f)

                return {d['date']: d for d in data.get('days', [])}
        except (json.JSONDecodeError, KeyError) as e:
            _LOGGER.error("数据源格式错误: %s", e)
            return None
