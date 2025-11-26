# 🚀 نظام إدارة التوصيل باستخدام Odoo 17
# 🚀 Système de gestion de livraison avec Odoo 17

---

## 📄 الوصف العام / Description générale

**العربية:**  
هذا المشروع عبارة عن نظام لإدارة التوصيل باستخدام منصة **Odoo 17**.  
يمكن للمستخدمين إدارة الطلبات، تتبع مسارات التوصيل، إدارة المنتجات والعملاء، وإنشاء تقارير مفصلة حول الأداء.  
المشروع يعتمد على إطار **Odoo**، قاعدة بيانات **PostgreSQL**، ويستخدم **Python** كلغة برمجة أساسية.

**Français:**  
Ce projet est un système de gestion de livraison basé sur **Odoo 17**.  
Il permet aux utilisateurs de gérer les commandes, suivre les itinéraires de livraison, gérer les produits et clients, et générer des rapports détaillés sur les performances.  
Le projet est basé sur le framework **Odoo**, utilise **PostgreSQL** comme base de données et **Python** comme langage principal.

---

## ✨ المزايا الأساسية / Fonctionnalités principales

**العربية:**  
- 🛒 إدارة الطلبات وإضافة طلب جديد  
- 🗺️ تتبع مسار التوصيل لكل طلب  
- 👥 إدارة العملاء والمندوبين  
- 📦 إدارة المنتجات والفئات  
- 📊 تقارير إحصائية وتحليل الأداء  
- 🎨 واجهة سهلة الاستخدام (UI/UX)

**Français:**  
- 🛒 Gestion des commandes et ajout de nouvelles commandes  
- 🗺️ Suivi des itinéraires de livraison pour chaque commande  
- 👥 Gestion des clients et des livreurs  
- 📦 Gestion des produits et des catégories  
- 📊 Rapports statistiques et analyse de performance  
- 🎨 Interface conviviale (UI/UX)

---

## 🛠️ التقنيات المستخدمة / Technologies utilisées

| العنصر / Élément | التقنية / Technologie | اللغة / Langage |
|-----------------|--------------------|----------------|
| منصة / Plateforme | Odoo 17 | Python |
| قاعدة البيانات / Base de données | PostgreSQL | SQL |
| الواجهة / Interface | XML / QWeb / JS / HTML / CSS | XML, JavaScript, HTML, CSS |
| بيئة التطوير / Environnement | Python Virtual Environment | Python 3.11 |

---

## 📁 هيكل المشروع / Structure du projet

odoo17/
├─ addons/ # مجلد الإضافات / Dossier des modules
│ ├─ my_module/ # الموديول الخاص بك / Votre module personnalisé
│ │ ├─ init.py # ملف التهيئة / Fichier d'initialisation
│ │ ├─ manifest.py # ملف تعريف الموديول / Fichier de description du module
│ │ ├─ models/ # مجلد النماذج / Dossier des modèles
│ │ │ └─ *.py # ملفات النماذج / Fichiers des modèles
│ │ ├─ views/ # مجلد الواجهات / Dossier des vues
│ │ │ └─ *.xml # ملفات الواجهات / Fichiers des vues
│ │ └─ security/ # الصلاحيات والمجموعات / Droits et groupes d'accès
│ │ ├─ ir.model.access.csv
│ │ └─ ...
├─ odoo/ # ملفات النظام الأساسية / Fichiers système d'Odoo
├─ venv/ # بيئة Python الافتراضية / Environnement virtuel Python
├─ odoo-bin # الملف التنفيذي لتشغيل Odoo / Exécutable pour lancer Odoo
└─ odoo.conf # ملف الإعدادات / Fichier de configuration

---

## ▶️ كيفية تشغيل المشروع / Comment lancer le projet

**العربية:**  
1. إنشاء قاعدة بيانات PostgreSQL جديدة، على سبيل المثال `odoo17db`.  
2. إنشاء البيئة الافتراضية وتثبيت المتطلبات:
```bash
python3.11 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
