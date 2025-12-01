# ✅ **Worksheet — Øvelse 4**

## **Titel:** Oplev et agentic loop: Tests → kode → kørsel → rettelse → gentag

### **🎯 Formål**

* Se hvordan Copilot CLI kan arbejde i et testdrevet loop.
* Træne Copilot i at:

  * generere tests
  * skrive implementering
  * køre tests
  * analysere fejl
  * rette koden
  * gentage processen, indtil alt passer
* Forstå hvordan man giver Copilot *en hel opgave*, ikke bare små instruktioner.

---

## **🔧 Opgave**

I denne øvelse starter du fra scratch med en lille Python-fil.
**Du får kun strukturen — resten skal du få Copilot til at lave.**

Du skal *ikke* selv skrive tests eller implementering.
Det klarer Copilot gennem et agentisk loop.

---

### **1. Kig på den udleverede utils.py**

Du har fået en fil `utils.py`, der indeholder tre tomme funktioner, som ikke gør noget endnu.

**Din opgave:**

* Gennemse funktionerne og overvej, hvad de *bør* gøre.
* Tænk over, hvilke tests der burde findes.

Du skal ikke skrive noget selv endnu.

---

### **2. Få Copilot til at generere tests**

**Din opgave:**

* Brug Copilot CLI til at:

  * foreslå relevante tests for funktionerne
  * oprette en `test_utils.py` med pytest-tests
  * forklare sin teststrategi, før den implementerer den

Du bestemmer selv, hvordan du formulerer opgaven — men giv Copilot en *samlet opgave*, ikke et mikrotrin.

---

### **3. Få Copilot til at implementere funktionerne**

**Din opgave:**

* Bed Copilot om at skrive implementeringerne i `utils.py`, så testene burde kunne bestås.

Copilot må gerne opdatere flere funktioner i samme ændring.

---

### **4. Kør tests og lad Copilot rette fejl**

**Din opgave:**

* Brug Copilot CLI til at køre testene.
* Hvis der er fejl (det er forventet), så få Copilot til at:

  * forklare fejlen
  * rette koden
  * patch’e filen
  * køre loopet igen

Gentag, indtil alle tests er grønne.

---

### **5. Udvid eller forbedr**

Når alle tests passer:

**Din opgave:**

* Bed Copilot foreslå 2–3 forbedringer af enten tests eller implementering.
* Vælg én og få Copilot til at implementere den.

Dette viser, hvordan Copilot kan udføre et *reflection-improvement-loop*.

---

## **6. Refleksion**

Overvej:

* Hvordan reagerede Copilot, når du gav den en hel testdrevet opgave?
* Hvad var mest effektivt — detaljerede eller åbne prompts?
* Hvor meget “forstod” Copilot på egen hånd?
* Hvordan oplevede du agentic loop’et i praksis?

Notér 2–3 ting til senere.
