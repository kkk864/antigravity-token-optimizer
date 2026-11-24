# Antigravity Token Optimizer

Модернизированный набор правил и плагин для Google Antigravity, снижающий расход токенов при сохранении максимальной скорости и точности работы.

## Структура

- [`rules/token-saver.md`](rules/token-saver.md) — глобальное правило экономии токенов и высокой продуктивности (параллельные вызовы инструментов, точечный поиск перед чтением, делегирование широкого ресёрча субагенту, точечные правки, сжатый вывод терминала и гигиена контекста).
- [`plugins/antigravity-token-optimizer/`](plugins/antigravity-token-optimizer/) — плагин с AST-скелетонизатором кода (`skeletonize.py`) для быстрого обзора структуры незнакомых файлов `>200` строк без чтения лишнего кода:
  - [`rules/AGENTS.md`](plugins/antigravity-token-optimizer/rules/AGENTS.md) — правило использования `skeletonize.py`
  - [`skills/code-skeletonizer/SKILL.md`](plugins/antigravity-token-optimizer/skills/code-skeletonizer/SKILL.md) — инструкция навыка
  - [`skills/code-skeletonizer/scripts/skeletonize.py`](plugins/antigravity-token-optimizer/skills/code-skeletonizer/scripts/skeletonize.py) — скрипт извлечения AST-структуры (`.py`, `.js`, `.ts`, `.go`, `.rs`, `.java`, `.cpp`)

## Установка

Скопируйте файлы в конфигурацию Antigravity (`~/.gemini/config/`):

```powershell
# Глобальное правило
Copy-Item .\rules\token-saver.md "$env:USERPROFILE\.gemini\config\rules\token-saver.md" -Force

# Плагин
Copy-Item .\plugins\antigravity-token-optimizer "$env:USERPROFILE\.gemini\config\plugins\antigravity-token-optimizer" -Recurse -Force
```
