# Карьера: материалы

| Файл | Что внутри |
|---|---|
| [01-market-research-2026-10.md](01-market-research-2026-10.md) | Анализ рынка финтеха на октябрь 2026: что горячо и почему выбраны эти проекты |
| [02-job-search-plan-30-days.md](02-job-search-plan-30-days.md) | План на 30 дней: воронка откликов, куда откликаться, что учить по неделям |
| [03-interview-prep.md](03-interview-prep.md) | Рассказ о себе, питчи проектов, каверзные вопросы с ответами, кейсы, сопроводительные письма |
| [04-internship-plan.md](04-internship-plan.md) | Где и когда подаваться на стажировки, календарь до лета 2027 |
| [profile_assets.py](profile_assets.py) | Генератор шапки и карточек проектов для профиля GitHub |
| [resume/](resume/) | Генератор резюме (HTML → PDF). Полная версия с телефоном — только здесь, в приватном репозитории |

## Как пересобрать резюме

```bash
cd career/resume
python build_resume.py                  # → resume_ru.html, resume_en.html
npm i playwright && npx playwright install chromium
node render_pdf.js                      # → Anton_Shkel_Resume_RU.pdf / _EN.pdf + проверка, что всё влезает в 1 страницу
```

Текст правится в `content_*.json`; `**жирный**` превращается в выделение.
