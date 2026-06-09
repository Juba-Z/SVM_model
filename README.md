# AI & Python Projects Collection 🤖🧠

مجموعة من مشاريع الذكاء الاصطناعي وتطبيقات البايثون البرمجية، تشمل لعبة Puzzle-8 وحلول خوارزميات البحث، وحل المتاهات، ومعالجة اللغات الطبيعية (NLP).

## محتويات المشروع (Project Structure) 📁

المستودع يحتوي على المشاريع التالية:

### 1. لعبة 8-Puzzle وحلول خوارزميات البحث (8-Puzzle Solver) 🧩
* **`projectAI_V1.py`**: نسخة اللعبة بواجهة رسومية (GUI) تفاعلية باستخدام مكتبة `tkinter` ويتم حل اللعبة تلقائياً بالاعتماد على خوارزمية **A\* Search Algorithm**.
* **`greedy_functional.py`**: نسخة تعمل من خلال شاشة الأوامر (CLI) تتيح اللعب اليدوي أو الحل التلقائي بالاعتماد على خوارزمية **Greedy Search** مع استخدام حساب مسافة مانهاتن (Manhattan Distance) كـ Heuristic.
* **نسخ إضافية وتجارب**: مثل `projectAI_greedy.py` و `try2Wgemini.py` للبحث والتطوير.

### 2. مشروع المتاهة (Maze Project) 🌀
* **`Maze Project.ipynb`**: دفتر عمل Jupyter يحتوي على كود وتجارب لحل المتاهات وتطبيق خوارزميات البحث المختلفة عليها.

### 3. مشروع معالجة اللغات الطبيعية (NLP Project) 🗣️
* **مجلد `NLP Project`**: يحتوي على ملفات وأكواد لمعالجة النصوص واللغات الطبيعية.

### 4. أدوات إضافية (Utilities) 📊
* **`sync_prices.py`**: سكربت خاص بمزامنة وتحديث الأسعار بالاعتماد على ملفات Excel وقواعد البيانات.

---

## كيفية التشغيل (How to Run) 🚀

### متطلبات التشغيل
تأكد من تثبيت بايثون على جهازك والمكتبات المطلوبة:
```bash
pip install pandas openpyxl notebook
```

### تشغيل لعبة 8-Puzzle (الواجهة الرسومية)
```bash
python projectAI_V1.py
```

### تشغيل لعبة 8-Puzzle (شاشة الأوامر CLI)
```bash
python greedy_functional.py
```

---

## الخوارزميات المستخدمة 🛠️
* **A\* Search Algorithm**: للوصول للحل الأمثل في لعبة 8-Puzzle.
* **Greedy Best-First Search**: للحل السريع باستخدام Manhattan Distance.
