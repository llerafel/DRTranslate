import requests
import json
import os
from pathlib import Path
import sys
import re
import logging

# Настройка логирования
logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")

# Константы
FILE_STRUCTURES = {
    'ContextMenu_RU.txt': {
        'table_name': 'ContextMenu_RU',
        'header_comments': ['////DRTranslate Team////']
    },
    'Farming_UA.txt': {
        'table_name': 'Farming_RU',
        'header_comments': ['////DRTranslate Team////']
    },
    'IG_UI_RU.txt': {
        'table_name': 'IGUI_RU',
        'header_comments': ['////DRTranslate Team////']
    },
    'ItemName_UA.txt': {
        'table_name': 'ItemName_RU',
        'header_comments': ['////DRTranslate Team////']
    },
    'Items_RU.txt': {
        'table_name': 'Items_RU',
        'header_comments': ['////DRTranslate Team////']
    },
    'Recipes_RU.txt': {
        'table_name': 'Recipes_RU',
        'header_comments': ['////DRTranslate Team////']
    },
    'Tooltip_RU.txt': {
        'table_name': 'Tooltip_RU',
        'header_comments': ['////DRTranslate Team////']
    },
    'UI_RU.txt': {
        'table_name': 'UI_RU',
        'header_comments': ['////DRTranslate Team////']
    },
    'Moodles_RU.txt': {
        'table_name': 'Moodles_RU',
        'header_comments': ['////DRTranslate Team////']
    },
}


def fetch_data(api_url):
    """
    Получение данных из Google Sheets через POST запрос.
    """
    # try:
    #     response = requests.post(api_url)
    #     response.raise_for_status()
    #     return response.json()
    # except requests.RequestException as e:
    #     logging.error(f"Ошибка при запросе данных: {e}")
    #     sys.exit(1)
    return json.loads("""{"data":[{"path":"mods\\\\More Traits\\\\media\\\\lua\\\\shared\\\\Translate\\\\EN\\\\Moodles_EN.txt","key":"Moodles_MTAlcoholism_Good_lvl1","string":"Чуточку бахнул"},{"path":"mods\\\\More Traits\\\\media\\\\lua\\\\shared\\\\Translate\\\\EN\\\\Moodles_EN.txt","key":"Moodles_MTAlcoholism_Good_desc_lvl1","string":"Успокоил жажду выпивки"},{"path":"mods\\\\More Traits\\\\media\\\\lua\\\\shared\\\\Translate\\\\EN\\\\Moodles_EN.txt","key":"Moodles_MTAlcoholism_Good_lvl2","string":"Выпил"},{"path":"mods\\\\More Traits\\\\media\\\\lua\\\\shared\\\\Translate\\\\EN\\\\Moodles_EN.txt","key":"Moodles_MTAlcoholism_Good_desc_lvl2","string":"Хорошенько бахнул"},{"path":"mods\\\\More Traits\\\\media\\\\lua\\\\shared\\\\Translate\\\\EN\\\\Moodles_EN.txt","key":"Moodles_MTAlcoholism_Good_lvl3","string":"Насытился бухлишком"},{"path":"mods\\\\More Traits\\\\media\\\\lua\\\\shared\\\\Translate\\\\EN\\\\Moodles_EN.txt","key":"Moodles_MTAlcoholism_Good_desc_lvl3","string":"Чувствую себя очень здорово!"},{"path":"mods\\\\More Traits\\\\media\\\\lua\\\\shared\\\\Translate\\\\EN\\\\Moodles_EN.txt","key":"Moodles_MTAlcoholism_Good_lvl4","string":"Нажрался"},{"path":"mods\\\\More Traits\\\\media\\\\lua\\\\shared\\\\Translate\\\\EN\\\\Moodles_EN.txt","key":"Moodles_MTAlcoholism_Good_desc_lvl4","string":"Какое-то время лучше обойтись без выпивки!"},{"path":"mods\\\\More Traits\\\\media\\\\lua\\\\shared\\\\Translate\\\\EN\\\\Moodles_EN.txt","key":"Moodles_MTAlcoholism_Bad_lvl1","string":"Тоска по алкашке"},{"path":"mods\\\\More Traits\\\\media\\\\lua\\\\shared\\\\Translate\\\\EN\\\\Moodles_EN.txt","key":"Moodles_MTAlcoholism_Bad_desc_lvl1","string":"Прошло уже некоторое время без бухла. <br>Пока никаких негативных эффектов"},{"path":"mods\\\\More Traits\\\\media\\\\lua\\\\shared\\\\Translate\\\\EN\\\\Moodles_EN.txt","key":"Moodles_MTAlcoholism_Bad_lvl2","string":"Ломка по алкоголю"},{"path":"mods\\\\More Traits\\\\media\\\\lua\\\\shared\\\\Translate\\\\EN\\\\Moodles_EN.txt","key":"Moodles_MTAlcoholism_Bad_desc_lvl2","string":"Трудновато игнорировать жажду бухла.<br>Стал раздражительнее."},{"path":"mods\\\\More Traits\\\\media\\\\lua\\\\shared\\\\Translate\\\\EN\\\\Moodles_EN.txt","key":"Moodles_MTAlcoholism_Bad_lvl3","string":"Жажда алкашки"},{"path":"mods\\\\More Traits\\\\media\\\\lua\\\\shared\\\\Translate\\\\EN\\\\Moodles_EN.txt","key":"Moodles_MTAlcoholism_Bad_desc_lvl3","string":"Хотя бы глоток...<br>Увеличен стресс."},{"path":"mods\\\\More Traits\\\\media\\\\lua\\\\shared\\\\Translate\\\\EN\\\\Moodles_EN.txt","key":"Moodles_MTAlcoholism_Bad_lvl4","string":"Я что, бросаю?"},{"path":"mods\\\\More Traits\\\\media\\\\lua\\\\shared\\\\Translate\\\\EN\\\\Moodles_EN.txt","key":"Moodles_MTAlcoholism_Bad_desc_lvl4","string":"Сделал бы что угодно ради выпивки.<br>Будет становится все более больным каждый день, пока не выпьет."},{"path":"mods\\\\More Traits\\\\media\\\\lua\\\\shared\\\\Translate\\\\EN\\\\Sandbox_EN.txt","key":"Sandbox_MoreTraits_IndefatigableOneUse","string":"Неутомимый (одноразовый)"},{"path":"mods\\\\More Traits\\\\media\\\\lua\\\\shared\\\\Translate\\\\EN\\\\Sandbox_EN.txt","key":"Sandbox_MoreTraits_IndefatigableOneUse_tooltip","string":"Если истинно, черта \\\"Неутомимый\\\" может быть использована только один раз на персонажа.<br> Если ложно, она будет восстанавливаться в соответствии с указанным ниже параметром.<br> Примечание: Если ложно, она излечит зомбификацию только один раз."},{"path":"mods\\\\More Traits\\\\media\\\\lua\\\\shared\\\\Translate\\\\EN\\\\Sandbox_EN.txt","key":"Sandbox_MoreTraits_EvasiveAnimation","string":"Отмена анимации уклонения."},{"path":"mods\\\\More Traits\\\\media\\\\lua\\\\shared\\\\Translate\\\\EN\\\\Sandbox_EN.txt","key":"Sandbox_MoreTraits_EvasiveAnimation_tooltip","string":"Если включено, \\\"Уклонение\\\" не имеет анимации получения удара при активации."},{"path":"mods\\\\More Traits\\\\media\\\\lua\\\\shared\\\\Translate\\\\EN\\\\Sandbox_EN.txt","key":"Sandbox_MoreTraits_HoarderCompatibility_tooltip","string":"Если у вас активированы и More Traits, и Expended Traits, оба они имеют бонусы, которые обновляют переносимый вес.<br>Если этот параметр включён, бонус \\\"Жадина(Скряга?)\\\" (из Expended Traits) и переносимый вес от этого мода (Вьючный мул/мышь) будут суммироваться. Это означает, что любой переносимый вес, полученный с Вьючного мула/Вьючной мыши, будет умножен на 1,25.<br>Если этот параметр выключен и у вас есть оба бонуса (\\\"Жадина(Скряга?)\\\" и Вьючный мул/мышь), либо \\\"Жадина(Скряга?)\\\", либо Вьючный мул/мышь запустит свой код первым. Честно говоря, в таком случае неизвестно, будет ли ваш максимальный вес рассчитан по коду \\\"Жадины\\\" или по коду перков Вьючный мул/мышь."},{"path":"mods\\\\More Traits\\\\media\\\\lua\\\\shared\\\\Translate\\\\EN\\\\Sandbox_EN.txt","key":"Sandbox_MoreTraits_SuperImmuneMinimum","string":"Минимальное количество дней для Супериммунного"},{"path":"mods\\\\More Traits\\\\media\\\\lua\\\\shared\\\\Translate\\\\EN\\\\Sandbox_EN.txt","key":"Sandbox_MoreTraits_SuperImmuneMinimum_tooltip","string":"Минимальное количество дней, за которое персонаж с Супериммунным вылечится от болезни."},{"path":"mods\\\\More Traits\\\\media\\\\lua\\\\shared\\\\Translate\\\\EN\\\\Sandbox_EN.txt","key":"Sandbox_MoreTraits_SuperImmuneMaximum","string":"Максимальное количество дней для Супериммунного"},{"path":"mods\\\\More Traits\\\\media\\\\lua\\\\shared\\\\Translate\\\\EN\\\\Sandbox_EN.txt","key":"Sandbox_MoreTraits_SuperImmuneMaximum_tooltip","string":"Максимальное количество дней, за которое персонаж с Супериммунным вылечится от болезни."},{"path":"mods\\\\More Traits\\\\media\\\\lua\\\\shared\\\\Translate\\\\EN\\\\Sandbox_EN.txt","key":"Sandbox_MoreTraits_SuperImmuneFirstInfectionBonus","string":"Меньше времени после лечения для Супериммунного"},{"path":"mods\\\\More Traits\\\\media\\\\lua\\\\shared\\\\Translate\\\\EN\\\\Sandbox_EN.txt","key":"Sandbox_MoreTraits_SuperImmuneFirstInfectionBonus_tooltip","string":"Если включено, то все инфекции после первой будут длиться вдвое меньше.<br>Примечание: если подцепили несколько инфекций, то время лечения всё ещё может достичь максимального количества дней."},{"path":"mods\\\\More Traits\\\\media\\\\lua\\\\shared\\\\Translate\\\\EN\\\\Sandbox_EN.txt","key":"Sandbox_MoreTraits_QuickSuperImmune","string":"Быстрый Супериммунный"},{"path":"mods\\\\More Traits\\\\media\\\\lua\\\\shared\\\\Translate\\\\EN\\\\Sandbox_EN.txt","key":"Sandbox_MoreTraits_QuickSuperImmune_tooltip","string":"Если включено, то Супериммунный будет работать в 6 раз быстрее.<br>Предпочтительно использовать в мультиплеере, где нет возможности быстро промотать время"},{"path":"mods\\\\More Traits\\\\media\\\\lua\\\\shared\\\\Translate\\\\EN\\\\Sandbox_EN.txt","key":"Sandbox_MoreTraits_ProwessGunsAmmoRestore","string":"Мастерство: Огнестрельное оружие"},{"path":"mods\\\\More Traits\\\\media\\\\lua\\\\shared\\\\Translate\\\\EN\\\\Sandbox_EN.txt","key":"Sandbox_MoreTraits_ProwessGunsAmmoRestore_tooltip","string":"Если включено, \\\"Мастерство: огнестрельное оружие\\\" имеет шанс не затратить боеприпасы для выстрела. Не очень реалистично, но весело"},{"path":"mods\\\\More Traits\\\\media\\\\lua\\\\shared\\\\Translate\\\\EN\\\\Sandbox_EN.txt","key":"Sandbox_MoreTraits_EvasiveBlocksPVP","string":"\\\"Уклонение\\\" работает для ПВП"},{"path":"mods\\\\More Traits\\\\media\\\\lua\\\\shared\\\\Translate\\\\EN\\\\Sandbox_EN.txt","key":"Sandbox_MoreTraits_EvasiveBlocksPVP_tooltip","string":"Если включено, то \\\"Уклонение\\\" работает против атак других игроков."},{"path":"mods\\\\More Traits\\\\media\\\\lua\\\\shared\\\\Translate\\\\EN\\\\Sandbox_EN.txt","key":"Sandbox_MoreTraits_BurnedDistance","string":"Расстояние для \\\"Жертвы пожара\\\""},{"path":"mods\\\\More Traits\\\\media\\\\lua\\\\shared\\\\Translate\\\\EN\\\\Sandbox_EN.txt","key":"Sandbox_MoreTraits_BurnedDistance_tooltip","string":"Расстояние от огня, на котором активируется \\\"Жертва пожара\\\".<br>Помните, что чем больше значение, тем больше паники и тревоги вы получите, пока будете при приближении.<br>Предупреждение: высокие значения могут привести к потере FPS"},{"path":"mods\\\\More Traits\\\\media\\\\lua\\\\shared\\\\Translate\\\\EN\\\\Sandbox_EN.txt","key":"Sandbox_MoreTraits_BurnedPanic","string":"Паника для \\\"Жертвы пожара\\\""},{"path":"mods\\\\More Traits\\\\media\\\\lua\\\\shared\\\\Translate\\\\EN\\\\Sandbox_EN.txt","key":"Sandbox_MoreTraits_BurnedPanic_tooltip","string":"Паника, которую вы будете получать от \\\"Жертвы пожара\\\"<br>Скалирование работает таким образом: постоянно добавляет панику, пока не достигнуто максимальное расстояние от огня (расстояние стартует от ближайшего огня).<br>Это значит, если огонь на расстоянии 1 тайла от вас, а максимальное расстояние 20 тайлов, то вы получите в 20 раз больше паники, чем значение этого параметра. Это происходит каждую игровую минуту."},{"path":"mods\\\\More Traits\\\\media\\\\lua\\\\shared\\\\Translate\\\\EN\\\\Sandbox_EN.txt","key":"Sandbox_MoreTraits_BurnedStress","string":"Тревога от \\\"Жертвы пожара\\\""},{"path":"mods\\\\More Traits\\\\media\\\\lua\\\\shared\\\\Translate\\\\EN\\\\Sandbox_EN.txt","key":"Sandbox_MoreTraits_BurnedStress_tooltip","string":"Тревога, которую вы будете получать от \\\"Жертвы пожара\\\"<br>Скалирование работает таким образом: постоянно добавляет тревогу, пока не достигнуто максимальное расстояние от огня (расстояние стартует от ближайшего огня).<br>Это значит, если огонь на расстоянии 1 тайла от вас, а максимальное расстояние 20 тайлов, то вы получите в 20 раз больше тревоги, чем значение этого параметра. Это происходит каждую игровую минуту."},{"path":"mods\\\\More Traits\\\\media\\\\lua\\\\shared\\\\Translate\\\\EN\\\\Sandbox_EN.txt","key":"Sandbox_MoreTraits_BatteringRamMartial","string":"Таран + Мастер боевых искусств"},{"path":"mods\\\\More Traits\\\\media\\\\lua\\\\shared\\\\Translate\\\\EN\\\\UI_EN.txt","key":"UI_trait_hardyrest","string":"Продолжайте отдыхать"},{"path":"mods\\\\More Traits\\\\media\\\\lua\\\\shared\\\\Translate\\\\EN\\\\UI_EN.txt","key":"UI_progunammo","string":"Мастерство сохранило ваши боеприпасы!"},{"path":"mods\\\\More Traits\\\\media\\\\lua\\\\shared\\\\Translate\\\\EN\\\\UI_EN.txt","key":"UI_trait_antigun","string":"Активист против оружия"},{"path":"mods\\\\More Traits\\\\media\\\\lua\\\\shared\\\\Translate\\\\EN\\\\UI_EN.txt","key":"UI_trait_antigundesc","string":"Вы против огнестрельного оружия и не имеете опыта в обращении с ним, что делает вас менее эффективным с огнестрелом.<br>Вы дольше прицеливаетесь, стреляете на меньшее расстояние и испытываете грусть, когда используете огнестрел.<br>Вы получаете на 25% меньше опыта в точности."},{"path":"mods\\\\More Traits\\\\media\\\\lua\\\\shared\\\\Translate\\\\EN\\\\UI_EN.txt","key":"UI_burnedcannotequip","string":"Ваша боязнь огня не позволяет держать этот предмет!"},{"path":"mods\\\\More Traits\\\\media\\\\lua\\\\shared\\\\Translate\\\\EN\\\\UI_EN.txt","key":"UI_burnedstop","string":"Ваша боязнь огня не позволяет разжечь огонь!"},{"path":"mods\\\\More Traits\\\\media\\\\lua\\\\shared\\\\Translate\\\\EN\\\\UI_EN.txt","key":"UI_trait_unwavering","string":"Непоколебимый"},{"path":"mods\\\\More Traits\\\\media\\\\lua\\\\shared\\\\Translate\\\\EN\\\\UI_EN.txt","key":"UI_trait_unwaveringdesc","string":"Штраф к скорости от травм уменьшен.<br>Вы выходите из стана после атак зомби вдвое быстрее."},{"path":"mods\\\\More Traits\\\\media\\\\lua\\\\shared\\\\Translate\\\\EN\\\\UI_EN.txt","key":"UI_trait_idealweight","string":"Идеальный вес"},{"path":"mods\\\\More Traits\\\\media\\\\lua\\\\shared\\\\Translate\\\\EN\\\\UI_EN.txt","key":"UI_trait_idealweightdesc","string":"Вы следите за своим весом.<br>Вы получаете в 1.5 раза больше калорий, когда вас вес меньше 78.<br>Вы получаете 0.75 калорий, когда ваш вес больше 82."},{"path":"mods\\\\More Traits\\\\media\\\\lua\\\\shared\\\\Translate\\\\EN\\\\UI_EN.txt","key":"UI_trait_quickrest","string":"Быстрый отдых"},{"path":"mods\\\\More Traits\\\\media\\\\lua\\\\shared\\\\Translate\\\\EN\\\\UI_EN.txt","key":"UI_trait_quickrestdesc","string":"Сидя на стуле, вы быстрее отдыхаете. Вы получите уведомление, когда полностью отдохнете "},{"path":"mods\\\\More Traits\\\\media\\\\lua\\\\shared\\\\Translate\\\\EN\\\\UI_EN.txt","key":"UI_quickrestfullendurance","string":"Вы отдохнули."},{"path":"mods\\\\More Traits\\\\media\\\\lua\\\\shared\\\\Translate\\\\EN\\\\UI_EN.txt","key":"UI_MoreTraits_Options_ProwessGunsAmmo","string":"Уведолмять, когда \\\"Мастерство: огнестрельное оружие\\\" сохраняет боеприпасы"},{"path":"mods\\\\More Traits\\\\media\\\\lua\\\\shared\\\\Translate\\\\EN\\\\UI_EN.txt","key":"UI_MoreTraits_Options_ProwessGunsAmmo_ToolTip","string":"Если у вас есть перк \\\"Мастерство: огнестрельное оружие\\\", будет показываться уведомление, когда он срабатывает и сохраняет боеприпасы."},{"path":"mods\\\\Authentic Z - Current\\\\media\\\\lua\\\\shared\\\\Translate\\\\EN\\\\ContextMenu_EN.txt","key":"ContextMenu_WearSideways","string":"Носить сбоку"},{"path":"mods\\\\Authentic Z - Current\\\\media\\\\lua\\\\shared\\\\Translate\\\\EN\\\\ContextMenu_EN.txt","key":"ContextMenu_UntieBonnet","string":"Развязать шляпку"},{"path":"mods\\\\Authentic Z - Current\\\\media\\\\lua\\\\shared\\\\Translate\\\\EN\\\\ContextMenu_EN.txt","key":"ContextMenu_TieBonnet","string":"Завязать шляпку"},{"path":"mods\\\\Authentic Z - Current\\\\media\\\\lua\\\\shared\\\\Translate\\\\EN\\\\ContextMenu_EN.txt","key":"ContextMenu_Wear1XS","string":"Носить как XS"},{"path":"mods\\\\Authentic Z - Current\\\\media\\\\lua\\\\shared\\\\Translate\\\\EN\\\\ContextMenu_EN.txt","key":"ContextMenu_Wear1XL","string":"Носить как XL"},{"path":"mods\\\\Authentic Z - Current\\\\media\\\\lua\\\\shared\\\\Translate\\\\EN\\\\ContextMenu_EN.txt","key":"ContextMenu_Wear2XL","string":"Носить как 2XL"},{"path":"mods\\\\Authentic Z - Current\\\\media\\\\lua\\\\shared\\\\Translate\\\\EN\\\\ContextMenu_EN.txt","key":"ContextMenu_Wear3XL","string":"Носить как 3XL"},{"path":"mods\\\\Authentic Z - Current\\\\media\\\\lua\\\\shared\\\\Translate\\\\EN\\\\ContextMenu_EN.txt","key":"ContextMenu_Stopping_Chainsaw","string":"Остановить бензопилу"},{"path":"mods\\\\Authentic Z - Current\\\\media\\\\lua\\\\shared\\\\Translate\\\\EN\\\\ContextMenu_EN.txt","key":"ContextMenu_Fuel_Left","string":"Остаток топлива"},{"path":"mods\\\\Authentic Z - Current\\\\media\\\\lua\\\\shared\\\\Translate\\\\EN\\\\ContextMenu_EN.txt","key":"ContextMenu_RetrieveFuel_Chainsaw","string":"Слить топливо"},{"path":"mods\\\\Authentic Z - Current\\\\media\\\\lua\\\\shared\\\\Translate\\\\EN\\\\IG_UI_EN.txt","key":"IGUI_HotbarAttachment_DufflebagBottleRight","string":"Спортивная сумка отсек для бутылки"},{"path":"mods\\\\Authentic Z - Current\\\\media\\\\lua\\\\shared\\\\Translate\\\\EN\\\\IG_UI_EN.txt","key":"IGUI_HotbarAttachment_ARVNBottleRight","string":"Рюкзак отсек для бутылки"},{"path":"mods\\\\Authentic Z - Current\\\\media\\\\lua\\\\shared\\\\Translate\\\\EN\\\\IG_UI_EN.txt","key":"IGUI_HotbarAttachment_ARVNBottleLeft","string":"Рюкзак отсек для бутылки"},{"path":"mods\\\\Authentic Z - Current\\\\media\\\\lua\\\\shared\\\\Translate\\\\EN\\\\IG_UI_EN.txt","key":"IGUI_HotbarAttachment_ARVNPlushie","string":"Рюкзак отсек для игрушки"},{"path":"mods\\\\Authentic Z - Current\\\\media\\\\lua\\\\shared\\\\Translate\\\\EN\\\\IG_UI_EN.txt","key":"IGUI_HotbarAttachment_ARVNUmbrellaRight","string":"Рюкзак вспомогательный отсек"},{"path":"mods\\\\Authentic Z - Current\\\\media\\\\lua\\\\shared\\\\Translate\\\\EN\\\\IG_UI_EN.txt","key":"IGUI_HotbarAttachment_ARVNItemSlot1","string":"Рюкзак отсек 1"},{"path":"mods\\\\Authentic Z - Current\\\\media\\\\lua\\\\shared\\\\Translate\\\\EN\\\\IG_UI_EN.txt","key":"IGUI_HotbarAttachment_ARVNItemSlot2","string":"Рюкзак отсек 2"},{"path":"mods\\\\Authentic Z - Current\\\\media\\\\lua\\\\shared\\\\Translate\\\\EN\\\\IG_UI_EN.txt","key":"IGUI_HotbarAttachment_ARVNItemSlot3","string":"Рюкзак отсек 3"},{"path":"mods\\\\Authentic Z - Current\\\\media\\\\lua\\\\shared\\\\Translate\\\\EN\\\\IG_UI_EN.txt","key":"IGUI_HotbarAttachment_ARVNItemSlot4","string":"Рюкзак отсек 4"},{"path":"mods\\\\Authentic Z - Current\\\\media\\\\lua\\\\shared\\\\Translate\\\\EN\\\\IG_UI_EN.txt","key":"IGUI_HotbarAttachment_ARVNItemSlot5","string":"Рюкзак отсек 5"},{"path":"mods\\\\Authentic Z - Current\\\\media\\\\lua\\\\shared\\\\Translate\\\\EN\\\\IG_UI_EN.txt","key":"IGUI_HotbarAttachment_ARVNFlashlight","string":"Рюкзак отсек для фонарика"},{"path":"mods\\\\Authentic Z - Current\\\\media\\\\lua\\\\shared\\\\Translate\\\\EN\\\\IG_UI_EN.txt","key":"IGUI_HotbarAttachment_ARVNSecondary","string":"Рюкзак запасной карман"},{"path":"mods\\\\Authentic Z - Current\\\\media\\\\lua\\\\shared\\\\Translate\\\\EN\\\\IG_UI_EN.txt","key":"IGUI_HotbarAttachment_AZWebbingLeft","string":"Лямка левый отсек"},{"path":"mods\\\\Authentic Z - Current\\\\media\\\\lua\\\\shared\\\\Translate\\\\EN\\\\IG_UI_EN.txt","key":"IGUI_HotbarAttachment_AZWebbingRight","string":"Лямка правый отсек"},{"path":"mods\\\\Authentic Z - Current\\\\media\\\\lua\\\\shared\\\\Translate\\\\EN\\\\IG_UI_EN.txt","key":"IGUI_HotbarAttachment_DufflebagBalloonLeft","string":"Отсек для шарика"},{"path":"mods\\\\Authentic Z - Current\\\\media\\\\lua\\\\shared\\\\Translate\\\\EN\\\\IG_UI_EN.txt","key":"IGUI_CraftCategory_Tailoring","string":"Шитье"},{"path":"mods\\\\Authentic Z - Current\\\\media\\\\lua\\\\shared\\\\Translate\\\\EN\\\\IG_UI_EN.txt","key":"IGUI_HotbarAttachment_HikingbagSleepingRoll","string":"Походная сумка спальный мешок"},{"path":"mods\\\\Authentic Z - Current\\\\media\\\\lua\\\\shared\\\\Translate\\\\EN\\\\IG_UI_EN.txt","key":"IGUI_HotbarAttachment_BigHikingbagSleepingRoll","string":"Большая походная сумка спальный мешок"},{"path":"mods\\\\Authentic Z - Current\\\\media\\\\lua\\\\shared\\\\Translate\\\\EN\\\\IG_UI_EN.txt","key":"IGUI_HotbarAttachment_AlicepackSleepingRoll","string":"Разгрузка спальный мешок"},{"path":"mods\\\\Authentic Z - Current\\\\media\\\\lua\\\\shared\\\\Translate\\\\EN\\\\IG_UI_EN.txt","key":"IGUI_AuthenticZ_Manage_Slots","string":"AuthenticZ Управление навесами"},{"path":"mods\\\\Authentic Z - Current\\\\media\\\\lua\\\\shared\\\\Translate\\\\EN\\\\IG_UI_EN.txt","key":"IGUI_ItemCat_Chainsaw","string":"Бензопила"},{"path":"mods\\\\Authentic Z - Current\\\\media\\\\lua\\\\shared\\\\Translate\\\\EN\\\\IG_UI_EN.txt","key":"IGUI_ItemEditor_FuelConsumption","string":"Потребление топлива"},{"path":"mods\\\\Authentic Z - Current\\\\media\\\\lua\\\\shared\\\\Translate\\\\EN\\\\IG_UI_EN.txt","key":"IGUI_ItemEditor_CurrentFuel","string":"Текущий запас топлива"},{"path":"mods\\\\Authentic Z - Current\\\\media\\\\lua\\\\shared\\\\Translate\\\\EN\\\\IG_UI_EN.txt","key":"IGUI_ItemEditor_FuelCapacity","string":"Максимальный запас топлива"},{"path":"mods\\\\Authentic Z - Current\\\\media\\\\lua\\\\shared\\\\Translate\\\\EN\\\\IG_UI_EN.txt","key":"IGUI_ItemEditor_RetrieveFuel","string":"Слить топливо"},{"path":"mods\\\\Authentic Z - Current\\\\media\\\\lua\\\\shared\\\\Translate\\\\EN\\\\Recipes_EN.txt","key":"Recipe_Revert_Attachable","string":"Прикрепить обратно"},{"path":"mods\\\\Authentic Z - Current\\\\media\\\\lua\\\\shared\\\\Translate\\\\EN\\\\Recipes_EN.txt","key":"Recipe_Restart_Chainsaw","string":"Перезапустить бензопилу"},{"path":"mods\\\\Authentic Z - Current\\\\media\\\\lua\\\\shared\\\\Translate\\\\EN\\\\Recipes_EN.txt","key":"fixing_Fix_Chainsaw","string":"Починить бензопилу"},{"path":"mods\\\\Authentic Z - Current\\\\media\\\\lua\\\\shared\\\\Translate\\\\EN\\\\Tooltip_EN.txt","key":"Tooltip_OpenJacket","string":"Расстегивает куртку для меньшей теплоизоляции"},{"path":"mods\\\\Authentic Z - Current\\\\media\\\\lua\\\\shared\\\\Translate\\\\EN\\\\Tooltip_EN.txt","key":"Tooltip_TacticalWebbing","string":"Добавить 2 навесных отсека"},{"path":"mods\\\\Authentic Z - Current\\\\media\\\\lua\\\\shared\\\\Translate\\\\EN\\\\Tooltip_EN.txt","key":"Tooltip_AddWalkieTV110","string":"Прикрепить армейскую рацию TV-110"},{"path":"mods\\\\Authentic Z - Current\\\\media\\\\lua\\\\shared\\\\Translate\\\\EN\\\\Tooltip_EN.txt","key":"Tooltip_AddWalkieTV110Bag","string":"Прикрепить армейскую рацию TV-110, предварительно достав магазины."},{"path":"mods\\\\Authentic Z - Current\\\\media\\\\lua\\\\shared\\\\Translate\\\\EN\\\\Tooltip_EN.txt","key":"Tooltip_RemoveWalkieTV110","string":"Снять армейскую рацию TV-110"},{"path":"mods\\\\Authentic Z - Current\\\\media\\\\lua\\\\shared\\\\Translate\\\\EN\\\\Tooltip_EN.txt","key":"Tooltip_RemoveWalkieTV110Bag","string":"Снять армейскую рацию TV-110, предварительно достав магазины."},{"path":"mods\\\\Authentic Z - Current\\\\media\\\\lua\\\\shared\\\\Translate\\\\EN\\\\Tooltip_EN.txt","key":"Tooltip_TV110Bag","string":"Предварительно достать все предметы."},{"path":"mods\\\\Authentic Z - Current\\\\media\\\\lua\\\\shared\\\\Translate\\\\EN\\\\Tooltip_EN.txt","key":"Tooltip_JPCane","string":"Жизнь найдет способ."},{"path":"mods\\\\Authentic Z - Current\\\\media\\\\lua\\\\shared\\\\Translate\\\\EN\\\\Tooltip_EN.txt","key":"Tooltip_TagillaHelmet","string":"UBEY"},{"path":"mods\\\\Authentic Z - Current\\\\media\\\\lua\\\\shared\\\\Translate\\\\EN\\\\Tooltip_EN.txt","key":"Tooltip_AZSleepingBag","string":"Распаковать и поставить."},{"path":"mods\\\\Authentic Z - Current\\\\media\\\\lua\\\\shared\\\\Translate\\\\EN\\\\Tooltip_EN.txt","key":"Tooltip_AZSleepingBag2","string":"ПКМ чтобы спать."},{"path":"mods\\\\Authentic Z - Current\\\\media\\\\lua\\\\shared\\\\Translate\\\\EN\\\\Tooltip_EN.txt","key":"Tooltip_GlowStickPack","string":"Открой чтобы получить 3 случайные светящиеся палочки!"},{"path":"mods\\\\Authentic Z - Current\\\\media\\\\lua\\\\shared\\\\Translate\\\\EN\\\\Tooltip_EN.txt","key":"Tooltip_RotaryPhone","string":"Скажи привет тёте Алисии, приятель!"},{"path":"mods\\\\Authentic Z - Current\\\\media\\\\lua\\\\shared\\\\Translate\\\\EN\\\\Tooltip_EN.txt","key":"Tooltip_SizeXS","string":"Размер: S"},{"path":"mods\\\\Authentic Z - Current\\\\media\\\\lua\\\\shared\\\\Translate\\\\EN\\\\Tooltip_EN.txt","key":"Tooltip_SizeXL","string":"Размер: XL"},{"path":"mods\\\\Authentic Z - Current\\\\media\\\\lua\\\\shared\\\\Translate\\\\EN\\\\Tooltip_EN.txt","key":"Tooltip_Size2XL","string":"Размер: 2XL"},{"path":"mods\\\\Authentic Z - Current\\\\media\\\\lua\\\\shared\\\\Translate\\\\EN\\\\Tooltip_EN.txt","key":"Tooltip_Size3XL","string":"Размер: 3XL"},{"path":"mods\\\\Authentic Z - Current\\\\media\\\\lua\\\\shared\\\\Translate\\\\EN\\\\Tooltip_EN.txt","key":"Tooltip_SubstitutionDoll","string":"Кукла обмана"},{"path":"mods\\\\Authentic Z - Current\\\\media\\\\lua\\\\shared\\\\Translate\\\\EN\\\\UI_EN.txt","key":"UI_Fuel_Remaining","string":"Остаток топлива:"},{"path":"mods\\\\FWO Treadmill & BenchPress\\\\media\\\\lua\\\\shared\\\\Translate\\\\EN\\\\IG_UI_EN.txt","key":"IGUI_BenchPress_Tooltip","string":"Делать жим лежа"},{"path":"mods\\\\FWO Treadmill & BenchPress\\\\media\\\\lua\\\\shared\\\\Translate\\\\EN\\\\IG_UI_EN.txt","key":"IGUI_Treadmill_Tooltip","string":"Тренироваться на беговой дорожке"},{"path":"mods\\\\FWO Treadmill & BenchPress\\\\media\\\\lua\\\\shared\\\\Translate\\\\EN\\\\IG_UI_EN.txt","key":"IGUI_need_barbell","string":"Мне нужна штанга, чтобы сделать это упражнение"},{"path":"mods\\\\FWO Treadmill & BenchPress\\\\media\\\\lua\\\\shared\\\\Translate\\\\EN\\\\IG_UI_EN.txt","key":"IGUI_low_endurance","string":"Я слишком измотан"},{"path":"mods\\\\FWO Treadmill & BenchPress\\\\media\\\\lua\\\\shared\\\\Translate\\\\EN\\\\IG_UI_EN.txt","key":"IGUI_pain","string":"Мне слишком больно"},{"path":"mods\\\\FWO Treadmill & BenchPress\\\\media\\\\lua\\\\shared\\\\Translate\\\\EN\\\\IG_UI_EN.txt","key":"IGUI_heavy","string":"Слишком тяжелая, чтобы использовать ее прямо сейчас"}],"hash":"5da90143e2b110a11d8c71428c822e3e22ca5f83"}""")


def read_last_checksum(checksum_file):
    """
    Чтение последнего хеша из файла.
    """
    try:
        if os.path.exists(checksum_file):
            with open(checksum_file, 'r', encoding='utf-8') as f:
                return f.read().strip()
    except Exception as e:
        logging.error(f"Ошибка чтения файла хеша: {e}")
    return ""


def write_checksum(checksum_file, checksum):
    """
    Запись нового хеша в файл.
    """
    try:
        with open(checksum_file, 'w', encoding='utf-8') as f:
            f.write(checksum)
    except Exception as e:
        logging.error(f"Ошибка записи файла хеша: {e}")


def build_mod(data, output_dir):
    """
    Сборка мода из данных в соответствующие файлы с Lua-таблицами.
    """
    os.makedirs(output_dir, exist_ok=True)
    translations = {}

    # Регулярные выражения для преобразования пути
    mod_name_pattern = re.compile(r'^mods/[^/]+/')
    en_pattern = re.compile(r'/EN/([^/]+)_EN\.txt$')

    # Группировка данных по файлам
    for entry in data.get('data', []):
        original_path = entry['path'].replace('\\', '/')
        key = entry['key']
        string = entry['string']

        # Преобразование пути
        new_path = mod_name_pattern.sub('mods/DRTranslate/', original_path)
        new_path = en_pattern.sub(r'/RU/\1_RU.txt', new_path)

        if new_path == original_path:
            logging.warning(f"Путь не преобразован, возможно некорректный формат: {original_path}")
            continue

        translations.setdefault(new_path, []).append({
            'original_path': original_path,
            'key': key,
            'string': string
        })

    # Запись переводов в соответствующие файлы
    for new_path, entries in translations.items():
        full_path = Path(output_dir) / new_path
        full_path.parent.mkdir(parents=True, exist_ok=True)

        filename = full_path.name
        file_structure = FILE_STRUCTURES.get(filename, {
            'table_name': filename.replace('_RU.txt', '_Unknow_RU'),
            'header_comments': []
        })
        table_name = file_structure['table_name']
        header_comments = file_structure['header_comments']

        grouped_by_original = {}
        for entry in entries:
            grouped_by_original.setdefault(entry['original_path'], []).append((entry['key'], entry['string']))

        try:
            with open(full_path, 'w', encoding='cp1251', errors='replace') as f:
                f.write(f"{table_name} = {{\n")
                for comment in header_comments:
                    f.write(f"\t{comment}\n")
                if header_comments:
                    f.write("\n")

                # Запись данных
                for orig_path, key_string_pairs in grouped_by_original.items():
                    f.write(f"\t////Original path: {orig_path}////\n")
                    for key, string in key_string_pairs:
                        clean_string = string.replace('"', '\\"')
                        f.write(f'\t{key} = "{clean_string}",\n')
                    f.write("\n")
                f.write("}\n")
            logging.info(f"Файл создан: {full_path}")
        except Exception as e:
            logging.error(f"Ошибка записи файла {full_path}: {e}")

    if not translations:
        logging.warning("Нет данных для записи")
    logging.info(f"Мод собран в {output_dir}")


def main():
    """
    Основная функция для запуска скрипта.
    """
    api_url = os.getenv("GOOGLE_SHEETS_API_URL")
    checksum_file = "github/workspace/hash.txt"
    output_dir = "github/workspace/Contents/"

    # if not api_url:
    #     logging.error("Переменная окружения GOOGLE_SHEETS_API_URL не установлена.")
    #     sys.exit(1)

    data = fetch_data(api_url)
    new_checksum = data.get('hash', '')

    if not new_checksum:
        logging.error("Ошибка: checksum отсутствует в данных.")
        sys.exit(1)

    old_checksum = read_last_checksum(checksum_file)

    if old_checksum == new_checksum:
        logging.info("Хеш не изменился, сборка не требуется.")
        print("::set-output name=BUILD_REQUIRED::false")
        return

    build_mod(data, output_dir)
    write_checksum(checksum_file, new_checksum)
    logging.info("Сборка завершена.")
    print("::set-output name=BUILD_REQUIRED::true")


if __name__ == "__main__":
    main()