# 🚚 نظام ERP لإدارة شركة توزيع (جملة ونصف جملة)
# 🚚 ERP de Gestion pour une Entreprise de Distribution (Gros & Demi-gros)

---

## 📌 مقدمة / Introduction

**العربية:**  
يهدف هذا المشروع إلى تطوير نظام ERP متكامل داخل منصة **Odoo 17** مخصص لشركات التوزيع بالجملة ونصف الجملة.  
يتعامل النظام مع المنتجات، العملاء، الديون، المبيعات، الشراء، المخزون، وتخطيط جولات التوصيل.  
يوفر هذا النظام أدوات قوية لمراقبة النشاط التجاري بدقة عبر منصة واحدة.

**Français:**  
Ce projet consiste à développer un module ERP complet sous **Odoo 17** dédié aux entreprises de distribution en gros et demi-gros.  
Il gère les produits, les clients, les dettes, les ventes, les achats, le stock et les tournées de distribution.  
Le système permet une gestion centralisée, flexible et efficace des opérations commerciales.

---

## 🎯 أهداف المشروع / Objectifs du projet

### **العربية:**
- 🛒 إدارة المبيعات وإنشاء طلبات جديدة  
- 👥 إدارة العملاء ومتابعة الديون  
- 🧾 إدارة الفواتير والمدفوعات الجزئية  
- 📦 إدارة المنتجات والمخزون  
- 🚚 تنظيم جولات التوزيع للعملاء  
- 📊 تقارير مفصلة حول الديون والمبيعات والجولات  

### **Français :**
- 🛒 Gestion des ventes et création des commandes  
- 👥 Gestion des clients et suivi des dettes  
- 🧾 Gestion des factures et paiements partiels  
- 📦 Gestion des produits et du stock  
- 🚚 Organisation des tournées de distribution  
- 📊 Rapports détaillés (dettes, ventes, tournées)  

---

## 🧩 مكونات النظام / Composants du système

### **1️⃣ إدارة المبيعات (Sales Management)**  
- إنشاء وتتبع طلبات البيع  
- حساب الإجمالي والديون تلقائيًا  
- إدارة خطوط الطلب (المنتج، الكمية، السعر...)  

### **2️⃣ إدارة العملاء والديون (Customer & Debt Management)**  
- بطاقة لكل عميل  
- حساب الديون المتبقية  
- تتبع الدفعات الجزئية  

### **3️⃣ إدارة المنتجات والمخزون (Product & Stock Management)**  
- اسم المنتج، السعر، الكمية  
- حركات المخزون (دخول/خروج)  
- تنبيه عند انخفاض الكمية  

### **4️⃣ إدارة الشراء (Purchases)**  
- إنشاء أوامر شراء  
- تحديث المخزون تلقائيًا عند الاستلام  

### **5️⃣ جولات التوزيع (Delivery Routes)**  
- تحديد السائق والمركبة  
- قائمة العملاء في الجولة  
- المنتجات والكمية الموجهة للتوزيع  

---

## 🧱 نماذج البيانات (Models) / Modèles principaux

### **منتج / Product**
- `name`  
- `category`  
- `purchase_price`  
- `sale_price`  
- `quantity`  

### **عميل / Client**
- `partner_id`  
- `customer_type` (gros / demi-gros)  
- `current_debt`  

### **طلب بيع / Sale Order**
- `customer_id`  
- `order_date`  
- `order_line_ids`  
- `total_amount`  
- `paid_amount`  
- `remaining_debt`  

### **خط طلب / Order Line**
- `order_id`  
- `product_id`  
- `quantity`  
- `unit_price`  
- `subtotal`  

---

## 🖥️ الواجهات (Views) / Interfaces

- 📄 **شجرة + فورم للمنتجات**  
- 📄 **شجرة + فورم للعملاء**  
- 🧾 **واجهة إدارة الديون**  
- 🧾 **واجهة المبيعات + خطوط المبيعات**  
- 📦 **حركات المخزون**  
- 🚚 **شاشة جولات التوزيع**  
- 🧩 **تقارير QWeb للاستخراج PDF**  

---

## 🛠️ التقنيات المستعملة / Technologies utilisées

### **اللغات / Langages**
- 🐍 Python  
- 🟦 XML  
- 🟨 JavaScript  
- 🟥 HTML / CSS  
- 🗄️ SQL / PostgreSQL  

### **أدوات Odoo**
- `odoo.models`  
- `odoo.api`  
- `odoo.fields`  
- QWeb Reports  
- ORM  

### **منصات / Outils**
- Odoo 17  
- PostgreSQL  
- VS Code / PyCharm  
- pgAdmin  

---

## 📂 هيكلة المشروع / Structure du module


│
├── init.py
├── manifest.py
│
├── models/
│ ├── product.py
│ ├── client.py
│ ├── sale_order.py
│ ├── stock.py
│ └── routes.py
│
├── views/
│ ├── product_views.xml
│ ├── client_views.xml
│ ├── sale_views.xml
│ ├── stock_views.xml
│ └── route_views.xml
│
├── security/
│ ├── ir.model.access.csv
│ └── security_rules.xml
│
└── reports/
├── sale_report.xml
└── invoice_template.xml


---

## ▶️ كيفية التشغيل / Comment lancer le projet

1. تثبيت Odoo 17  
2. إضافة الموديول في مسار addons  
3. تحديث قائمة التطبيقات  
4. تثبيت الموديول  
5. بدء الاستخدام مباشرة  

Commandes :

```bash
python3 odoo-bin -c odoo.conf -d odoo17db

✅ خاتمة / Conclusion

هذا النظام يقدم حلًا ERP متكاملًا ومخصصًا لمؤسسات التوزيع بالجملة ونصف الجملة.
يسمح بإدارة احترافية للديون، المبيعات، المخزون، الجولات، وكل العمليات اليومية.

Ce module offre une solution ERP complète et adaptée pour les entreprises de distribution.
Il centralise et optimise toutes les opérations essentielles.


## 🧠 المطورون | Developers
MOUAZ Fatma Zohra,Ihtida limam, hizi bouchra,kadri rima,djihad darem ,Remoune imane , zineddine kedidi
ALgeria
