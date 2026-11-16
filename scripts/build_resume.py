"""Build the RU/EN resumes. Requires reportlab and the Arial font family."""
from pathlib import Path
import os
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak, KeepTogether
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.colors import HexColor
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.enums import TA_LEFT

ROOT=Path(__file__).resolve().parents[1]
FONT=Path(os.environ.get('RESUME_FONT_DIR','C:/Windows/Fonts'))
pdfmetrics.registerFont(TTFont('Resume',str(FONT/'arial.ttf')))
pdfmetrics.registerFont(TTFont('ResumeBold',str(FONT/'arialbd.ttf')))
pdfmetrics.registerFontFamily('Resume',normal='Resume',bold='ResumeBold')
styles={
 'name':ParagraphStyle('name',fontName='ResumeBold',fontSize=30,leading=35,textColor=HexColor('#6f091d'),spaceAfter=7),
 'role':ParagraphStyle('role',fontName='ResumeBold',fontSize=11.7,leading=17,spaceAfter=8),
 'contact':ParagraphStyle('contact',fontName='Resume',fontSize=9,leading=14,textColor=HexColor('#66545a'),spaceAfter=14),
 'section':ParagraphStyle('section',fontName='ResumeBold',fontSize=12,leading=17,textColor=HexColor('#960e29'),spaceBefore=15,spaceAfter=7),
 'title':ParagraphStyle('title',fontName='ResumeBold',fontSize=10.3,leading=14,spaceBefore=8,spaceAfter=4),
 'body':ParagraphStyle('body',fontName='Resume',fontSize=10.1,leading=14.6,spaceAfter=5),
 'small':ParagraphStyle('small',fontName='Resume',fontSize=8.3,leading=12,textColor=HexColor('#66545a'),spaceAfter=6),
}
RU=[
('name','Антон Шкель'),
('role','Product / Business Analyst · Python / SQL · AI-интеграции'),
('contact','Москва · anton.shkel06@mail.ru · Telegram: @antonshkelll'),
('body','Ищу стажировку в продуктовой, бизнес- или антифрод-аналитике. Учусь на программной инженерии в Финансовом университете. Соединяю анализ данных и разработку: от требований и пользовательских сценариев до интерфейса, интеграций и проверки результата.'),
('section','ХАКАТОНЫ И ПРОДУКТОВАЯ РАБОТА'),
('title','ОПОРА V5 · Hack&amp;Change 2026 / ПСБ · VIBESECURITY'),
('body','Юридический RAG-ассистент: поиск по предоставленной базе знаний, ответы с указанием источников и обработка недостаточности информации.'),
('body','<b>Мой вклад:</b> анализ требований и критерии приёмки; продуктовые сценарии; архитектура и интеграция RAG; веб-интерфейс и демонстрация; проверка качества, упаковка сабмита, презентация и общая приёмка решения.'),
('small','Итоговая версия: V5. Репозиторий, веб-демонстрация, презентация и архив для автоматической проверки подготовлены.'),
('title','Умный кредитный кабинет · Альфа-Будущее Хакатон 2026'),
('body','Продуктовая проработка MVP для предпринимателя: требования, пользовательские сценарии и тексты интерфейса. WireMock-моки ЕГРЮЛ, ФНС, БКИ и банка; синтетические профили и сценарии сбоев для интеграции и демонстрации.'),
('section','ОПЫТ РАЗРАБОТКИ'),
('title','Разработчик · IT-комитет студсовета ФИТиАБД, Финуниверситет | 2024 - н. в.'),
('body','Бот и Mini App «Спроси ССт НАБ»: обращения руководству, фотографии неисправностей, поиск по FAQ из 27 страниц, карта кампуса примерно на 350 помещений. Поддержка студенческих цифровых сервисов и канала F&amp;U на 4 тыс. подписчиков.'),
('body','Python, aiogram 3, aiohttp; HMAC-SHA256 для авторизации Mini App, антиспам, тесты, nginx, systemd, Docker. Событийная аналитика и SQL: DAU/MAU, удержание, воронки и время ответа.'),
('title','Python / Web-разработчик · проектная работа | 2024 - н. в.'),
('body','Сайты и API на Django / Flask, PostgreSQL, формы заявок, интеграции и развёртывание. В работе над личным портфолио: структура, тексты, интерфейс, адаптивная вёрстка и публикация.'),
('small','Дополнительно: оргкомитет игрового фестиваля «Аркадиум», 200–300 участников; 2024 - н. в.'),
('page',''),
('section','АНАЛИТИЧЕСКИЕ ПРОЕКТЫ'),
('small','Ниже: результаты учебных и исследовательских проектов на использованных наборах данных. Это не показатели внедрения в действующем банке.'),
('title','SplitLab · продуктовая аналитика BNPL | SQL, DuckDB, Python'),
('body','Витрины на 1 млн событий: активность, воронки, когортное удержание и винтажная юнит-экономика. DiD-анализ ограничения оплаты частями: доля BNPL снизилась на 32 п. п.; 83% покупателей выбрали другой способ оплаты.'),
('body','A/B-анализ: SRM, MDE, CUPED, bootstrap и delta method. В проектном эксперименте: +15,1% к конверсии в BNPL, p &lt; 0,001; контроль защитных метрик. Симуляция ежедневного подглядывания: 27% ложных побед.'),
('title','Uplift Targeting · причинный ML | Python, scikit-learn'),
('body','Реальный рандомизированный эксперимент на 64 тыс. клиентов. Проверка SRM и баланса признаков; S/T-learners, class transformation, Qini, uplift@k и IPW. Наблюдаемый эффект: +7,7 п. п. к визитам; вывод о неокупаемости денежного таргетинга при условиях выборки.'),
('title','DropHunter · антифрод | SQL, Python, градиентный бустинг'),
('body','Признаки на 1,57 млн переводов: скорость вывода через ASOF JOIN, транзитность, новые отправители. Временное разделение данных; PR-AUC 0,81 против 0,36 у правил. Экономический порог: +46% к расчётному чистому эффекту при той же нагрузке на проверку.'),
('title','Продукты и AI-инструменты'),
('body','Subly: Android-трекер подписок и сервер на Ktor. TxGPT: языковая модель с нуля на PyTorch. finpilot: MCP-инструменты для анализа банковской выписки. «Пульс рынка»: автоматическое обновление данных Московской биржи.'),
('section','ОБРАЗОВАНИЕ'),
('title','Финансовый университет при Правительстве РФ | 2024–2028'),
('body','Бакалавриат, 09.03.04 «Программная инженерия». Профиль: разработка и внедрение информационно-аналитических систем.'),
('section','НАВЫКИ'),
('body','<b>Данные:</b> SQL (PostgreSQL, DuckDB, SQLite, MySQL), CTE, оконные функции; Python, pandas, NumPy, SciPy, statsmodels; Excel и Google Sheets.'),
('body','<b>Аналитика:</b> метрики и воронки, когортный анализ, юнит-экономика, A/B-тесты, SRM, MDE, CUPED, bootstrap, DiD, uplift, экономическая оценка моделей.'),
('body','<b>Продукт и разработка:</b> требования, сценарии и критерии приёмки; AI / RAG-интеграции; REST API, aiogram, Django / Flask, Docker, nginx, Git; scikit-learn и PyTorch.'),
('small','Языки: русский: родной; английский: B1. Обучение: Т-Образование, SQL / backend (2025); Академия Яндекса, Python / анализ данных (2025).'),
]
EN=[
('name','Anton Shkel'),
('role','Product / Business Analyst · Python / SQL · AI integrations'),
('contact','Moscow · anton.shkel06@mail.ru · Telegram: @antonshkelll'),
('body','Seeking an internship in product, business or fraud analytics. Software Engineering student at Financial University. I combine analysis and development: requirements and user journeys, interfaces and integrations, then validation of the result.'),
('section','HACKATHONS &amp; PRODUCT WORK'),
('title','OPORA V5 · Hack&amp;Change 2026 / PSB · VIBESECURITY'),
('body','Legal RAG assistant: retrieval from the supplied knowledge base, source-backed answers and handling of insufficient evidence.'),
('body','<b>My contribution:</b> requirements analysis and acceptance criteria; product scenarios; RAG architecture and integration; web interface and demo; quality checks, submission packaging, presentation and overall acceptance.'),
('small','Final version: V5. Delivered repository, web demo, presentation and automatic-evaluation archive.'),
('title','Smart Credit Workspace · Alfa Future Hackathon 2026'),
('body','Product requirements, user journeys and interface copy for an SME lending MVP. WireMock services for company, tax, credit bureau and bank data; synthetic profiles and failure scenarios for integration and demonstration.'),
('section','DEVELOPMENT EXPERIENCE'),
('title','Developer · Student Council IT Committee, Financial University | 2024 - present'),
('body','Student Council bot and Mini App: requests to faculty management, maintenance photos, search across a 27-page FAQ and a campus map covering approximately 350 rooms. Supported student digital services and the F&amp;U channel with 4,000 subscribers.'),
('body','Python, aiogram 3, aiohttp; HMAC-SHA256 Mini App authentication, anti-spam, tests, nginx, systemd and Docker. Event instrumentation and SQL analysis: DAU/MAU, retention, funnels and response times.'),
('title','Python / Web Developer · project work | 2024 - present'),
('body','Django / Flask websites and APIs, PostgreSQL, lead forms, integrations and deployment. Personal portfolio work includes information structure, copy, interface, responsive layout and publishing.'),
('small','Also: organising committee of the Arkadium gaming festival, 200–300 attendees; 2024 - present.'),
('page',''),
('section','ANALYTICS PROJECTS'),
('small','The results below come from educational and research projects on their respective datasets. They are not claimed as production banking outcomes.'),
('title','SplitLab · BNPL product analytics | SQL, DuckDB, Python'),
('body','SQL marts over 1M events: activity, funnels, cohort retention and vintage unit economics. Difference-in-differences analysis of a BNPL restriction: BNPL share fell by 32 pp; 83% of buyers switched to other payment methods.'),
('body','A/B analysis: SRM, MDE, CUPED, bootstrap and delta method. Project experiment: +15.1% BNPL conversion, p &lt; 0.001, with guardrail checks. Daily-peeking simulation: 27% false wins.'),
('title','Uplift Targeting · causal ML | Python, scikit-learn'),
('body','Real randomised experiment with 64,000 customers. SRM and covariate balance checks; S/T-learners, class transformation, Qini, uplift@k and IPW. Observed visit effect: +7.7 pp. Assessed why monetary targeting did not pay off under the sample conditions.'),
('title','DropHunter · fraud analytics | SQL, Python, gradient boosting'),
('body','Features from 1.57M transfers: cash-out speed via ASOF JOIN, pass-through behaviour and new senders. Out-of-time validation: PR-AUC 0.81 vs 0.36 for rules. Economic threshold selection: +46% estimated net effect at the same review workload.'),
('title','Products &amp; AI tools'),
('body','Subly: Android subscription tracker with a Ktor backend. TxGPT: a language model built from scratch in PyTorch. finpilot: MCP tools for bank-statement analysis. Market Pulse: automated Moscow Exchange data updates.'),
('section','EDUCATION'),
('title','Financial University under the Government of the Russian Federation | 2024–2028'),
('body','BSc, Software Engineering (09.03.04). Track: development and implementation of information and analytical systems.'),
('section','SKILLS'),
('body','<b>Data:</b> SQL (PostgreSQL, DuckDB, SQLite, MySQL), CTEs and window functions; Python, pandas, NumPy, SciPy, statsmodels; Excel and Google Sheets.'),
('body','<b>Analytics:</b> metrics and funnels, cohort analysis, unit economics, A/B testing, SRM, MDE, CUPED, bootstrap, DiD, uplift and economic model evaluation.'),
('body','<b>Product &amp; engineering:</b> requirements, user scenarios and acceptance criteria; AI / RAG integration; REST APIs, aiogram, Django / Flask, Docker, nginx and Git; scikit-learn and PyTorch.'),
('small','Languages: Russian: native; English: B1. Courses: T-Education, SQL / backend (2025); Yandex Academy, Python / data analysis (2025).'),
]
def build(lang,content):
    path=ROOT/'resume'/f'Anton_Shkel_Resume_{lang}.pdf';path.parent.mkdir(exist_ok=True)
    def page(canvas,doc):
        canvas.setFillColor(HexColor('#960e29'));canvas.rect(42,811,511,4,fill=1,stroke=0)
        canvas.setFont('Resume',8);canvas.setFillColor(HexColor('#79666b'))
        canvas.drawString(42,27,'Антон Шкель' if lang=='RU' else 'Anton Shkel')
        canvas.drawRightString(553,27,f'{doc.page} / 2')
    doc=SimpleDocTemplate(str(path),pagesize=(595.28,841.89),leftMargin=42,rightMargin=42,topMargin=44,bottomMargin=42,title=('Антон Шкель' if lang=='RU' else 'Anton Shkel')+' | Product / Business Analyst',author='Anton Shkel')
    story=[PageBreak() if kind=='page' else Paragraph(text,styles[kind]) for kind,text in content]
    doc.build(story,onFirstPage=page,onLaterPages=page)
    return path
if __name__=='__main__':
    for lang,content in [('RU',RU),('EN',EN)]:print(build(lang,content))
