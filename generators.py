from typing import Dict, Iterator, Optional


def generator_commands(params: Dict[str, str | int]) -> Iterator:
    """ Генерирует команды """

    total_commands = len([i for i in params.keys() if "cmd" in i]) + 1  # получаем количество команд
    for i in range(1, total_commands):
        result: Dict[str, Optional[str | int]] = {
            "cmd": None,
            "value": None
        }

        # поиск команды и значения с одинаковым префиксом
        for key in params.keys():
            if f"cmd{i}" == key:
                result["cmd"] = params[key]
            elif f"value{i}" == key:
                result["value"] = params[key]
            elif None not in result.values():
                yield result
                break
